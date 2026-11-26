"""
Copiloto Industrial NLP & RAG — Pungo Academy (Curso ID 20)
4-Tab Interactive Streamlit Console connected to OpenAI (gpt-4o-mini + text-embedding-3-small)
with built-in local deterministic fallback when running without an API key.
"""

from __future__ import annotations

import glob
import html
import json
import os
import re
from collections import Counter, defaultdict

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
import streamlit as st
from openai import OpenAI
from sklearn.feature_extraction.text import TfidfVectorizer

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
DOCS_DIR = os.path.join(DATA_DIR, "maintenance_docs")
EMB_CACHE_PATH = os.path.join(DATA_DIR, "rag_embeddings_cache.npz")

NAVY = "#0D202B"
BLUE = "#007297"
LIME = "#8EC14B"
AMBER = "#E8820C"
RED = "#C0392B"

st.set_page_config(
    page_title="Copiloto Industrial NLP & RAG · Pungo Tech",
    page_icon="⚙️",
    layout="wide",
)

st.markdown(
    """
    <style>
      .stApp { background-color: #F4F8FA; }
      .pungo-banner {
        background: linear-gradient(90deg, #0D202B 0%, #004E6B 100%);
        padding: 18px 24px; border-radius: 14px; color: #FFFFFF;
        border-bottom: 4px solid #8EC14B; margin-bottom: 18px;
      }
      .pungo-banner h1 { margin: 0; font-size: 26px; font-weight: 800; color: #FFFFFF; }
      .pungo-banner p { margin: 4px 0 0; font-size: 14px; color: #CFE8F3; }
      .ner-box {
        background: #FFFFFF; border: 1.5px solid #CBD5E1; border-radius: 12px;
        padding: 16px 20px; line-height: 2.0; font-size: 16px; color: #0D202B;
      }
      .ner-tag {
        display: inline-block; padding: 2px 8px; border-radius: 6px;
        font-weight: 700; margin: 0 2px; font-size: 14.5px;
      }
      .ner-lbl {
        font-size: 10px; text-transform: uppercase; letter-spacing: 0.5px;
        margin-left: 5px; opacity: 0.85;
      }
      .kpi-card {
        background: #FFFFFF; border: 1.5px solid #CBD5E1; border-radius: 12px;
        padding: 14px 18px; border-left: 6px solid #007297;
      }
      .kpi-val { font-size: 26px; font-weight: 800; color: #0D202B; }
      .kpi-lbl { font-size: 12.5px; color: #475569; font-weight: 600; }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data
def load_datasets():
    wo = pd.read_csv(os.path.join(DATA_DIR, "curso_nlp_work_orders.csv"), parse_dates=["fecha_creacion", "fecha_cierre"])
    logs = pd.read_csv(os.path.join(DATA_DIR, "curso_nlp_operator_logs.csv"), parse_dates=["fecha_hora"])
    inc = pd.read_csv(os.path.join(DATA_DIR, "curso_nlp_incident_reports.csv"), parse_dates=["fecha_evento"])
    return wo, logs, inc


@st.cache_data
def load_sop_chunks():
    docs = []
    for p in sorted(glob.glob(os.path.join(DOCS_DIR, "*.md"))):
        txt = open(p, encoding="utf-8").read()
        sections = txt.split("\n## ")
        current = ""
        for sec in sections:
            if len(current) + len(sec) < 800:
                current += ("\n## " + sec) if current else sec
            else:
                if current:
                    docs.append({"source": os.path.basename(p), "text": current.strip()})
                current = "## " + sec
        if current:
            docs.append({"source": os.path.basename(p), "text": current.strip()})
    return docs


@st.cache_resource
def get_rag_index(chunks: list[dict], api_key: str):
    texts = [c["text"] for c in chunks]
    if api_key:
        if os.path.exists(EMB_CACHE_PATH):
            data = np.load(EMB_CACHE_PATH, allow_pickle=False)
            if len(data["embeddings"]) == len(texts):
                return {"mode": "openai", "matrix": data["embeddings"], "vec": None}
        client = OpenAI(api_key=api_key)
        all_embs = []
        for i in range(0, len(texts), 50):
            resp = client.embeddings.create(input=texts[i : i + 50], model="text-embedding-3-small")
            all_embs.extend([d.embedding for d in resp.data])
        mat = np.array(all_embs, dtype=np.float64)
        np.savez_compressed(EMB_CACHE_PATH, embeddings=mat)
        return {"mode": "openai", "matrix": mat, "vec": None}
    vec = TfidfVectorizer(ngram_range=(1, 2), max_features=2000).fit(texts)
    return {"mode": "local", "matrix": vec.transform(texts).toarray(), "vec": vec}


def get_openai_client(key: str):
    return OpenAI(api_key=key) if key else None


def classify_work_order(prob: str, trab: str, client) -> dict:
    sistemas = [
        "almacenamiento", "bombeo", "compresion", "electrica", "instrumentacion",
        "inyeccion_agua", "quimicos", "seguridad", "separacion", "transporte",
        "tratamiento", "tratamiento_agua",
    ]
    if client:
        prompt = (
            "Eres planificador senior de mantenimiento petrolero. Analiza problema y trabajo y devuelve SOLO JSON válido: "
            '{"tipo_orden":"correctivo|preventivo|predictivo","prioridad":"emergencia|urgente|normal|programada",'
            f'"sistema":"{"|".join(sistemas)}","especialidad":"mecánica|eléctrica|instrumentación|soldadura|predictivo|operaciones",'
            '"modo_falla":"UN SOLO valor principal entre: corrosion, fuga, desgaste_mecanico, falla_electrica, falla_instrumentacion, obstruccion, vibracion_excesiva, sobrecalentamiento",'
            '"justificacion":"explicación concisa en español"}'
        )
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": f"Problema: {prob}\nTrabajo: {trab}"},
            ],
            temperature=0,
            response_format={"type": "json_object"},
        )
        return json.loads(resp.choices[0].message.content)

    tl = (prob + " " + trab).lower()
    prio = "emergencia" if any(k in tl for k in ["emergencia", "derrame", "paro", "crític"]) else ("urgente" if any(k in tl for k in ["urgente", "fuga", "alta vibr"]) else "normal")
    tipo = "preventivo" if "preventivo" in tl or "programad" in tl else ("predictivo" if "vibración" in tl or "termograf" in tl else "correctivo")
    sist = "bombeo" if "p-10" in tl or "bomba" in tl else ("compresion" if "compresor" in tl or "c-10" in tl else ("instrumentacion" if "transmisor" in tl or "ft-" in tl or "v-" in tl else "separacion"))
    modo = "fuga" if "fuga" in tl or "sello" in tl else ("vibracion_excesiva" if "vibr" in tl else ("corrosion" if "corros" in tl else "falla_instrumentacion"))
    return {
        "tipo_orden": tipo,
        "prioridad": prio,
        "sistema": sist,
        "especialidad": "mecánica" if modo in ("fuga", "vibracion_excesiva") else "instrumentación",
        "modo_falla": modo,
        "justificacion": "Clasificación determinística en Modo Local por patrones léxicos.",
    }


def extract_entities(prob: str, trab: str, client) -> dict:
    full = f"Problema: {prob}\nTrabajo: {trab}".strip()
    tags = sorted(set(re.findall(r"\b([A-Z]{1,3}-\d{2,4}[A-B]?)\b", full)))
    meds = sorted(set(re.findall(r"(\d+\.?\d*\s*(?:°\s*[Cc]|psi|bar|kPa|mm/s|mm|%))", full)))
    if client:
        prompt = (
            "Extrae entidades de mantenimiento en JSON válido: "
            '{"equipos":[], "partes":[], "fallas":[], "mediciones":[], "acciones":[], "materiales":[]}. '
            "Usa cadenas exactas presentes en el texto."
        )
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": prompt}, {"role": "user", "content": full}],
            temperature=0,
            response_format={"type": "json_object"},
        )
        data = json.loads(resp.choices[0].message.content)
        data.setdefault("equipos", tags)
        return data

    tl = full.lower()
    partes = [p for p in ["sello mecánico", "rodamiento", "impeller", "transmisor", "posicionador", "brida", "junta", "tubing", "acople"] if p in tl]
    fallas = [f for f in ["fuga", "vibración", "corrosión", "desgaste", "descalibrado", "erosión", "sobrecalentamiento"] if f in tl]
    acciones = [a for a in ["reemplazó", "calibración", "verificó", "alineación", "reparación", "ajuste"] if a in tl]
    mats = [m for m in ["rosemount", "yokogawa", "ptfe", "skf", "cartucho", "junta"] if m in tl]
    return {"equipos": tags, "partes": partes, "fallas": fallas, "mediciones": meds, "acciones": acciones, "materiales": mats}


def highlight_ner_html(text: str, ent: dict) -> str:
    spans = []
    palette = [
        ("EQUIPO", ent.get("equipos", []), "#DBEAFE", "#1E40AF"),
        ("MEDICION", [str(m) for m in ent.get("mediciones", []) if isinstance(m, str)], "#FEF3C7", "#92400E"),
        ("PARTE", ent.get("partes", []), "#DCFCE7", "#166534"),
        ("FALLA", ent.get("fallas", []), "#FEE2E2", "#991B1B"),
        ("MATERIAL", ent.get("materiales", []), "#E0E7FF", "#3730A3"),
    ]
    out = html.escape(text)
    for label, terms, bg, fg in palette:
        for term in sorted({str(t) for t in terms if len(str(t)) >= 2}, key=len, reverse=True):
            esc = re.escape(html.escape(term))
            badge = f'<span class="ner-tag" style="background:{bg};color:{fg};">\\g<0><span class="ner-lbl">{label}</span></span>'
            out = re.sub(esc, badge, out, flags=re.IGNORECASE, count=2)
    return f'<div class="ner-box">{out}</div>'


# Load base resources
wo_df, logs_df, inc_df = load_datasets()
sop_chunks = load_sop_chunks()

# Sidebar
logo_path = os.path.join(ASSETS_DIR, "logo_pungo_tech.png")
if os.path.exists(logo_path):
    st.sidebar.image(logo_path, width=180)
st.sidebar.markdown("### Configuración del Motor IA")
env_key = os.environ.get("OPENAI_API_KEY", "").strip()
api_key_input = st.sidebar.text_input(
    "OpenAI API Key (opcional)",
    value=env_key,
    type="password",
    help="Si está vacía, el Copiloto opera en Modo Local Sin Costo.",
)
active_key = api_key_input.strip()
client = get_openai_client(active_key)
if client:
    st.sidebar.success("Motor Activo: OpenAI gpt-4o-mini + text-embedding-3-small")
else:
    st.sidebar.info("Motor Activo: Modo Local Determinístico (TF-IDF + Reglas)")

st.sidebar.markdown("---")
st.sidebar.markdown(
    f"""
**Corpus Industrial Cargado**
- Órdenes de Trabajo: **{len(wo_df):,}**
- Bitácoras de Turno: **{len(logs_df):,}**
- Incidentes HSE: **{len(inc_df):,}**
- Documentos SOP/OEM: **12 ({len(sop_chunks)} chunks)**
"""
)

# Top Header
st.markdown(
    """
    <div class="pungo-banner">
      <h1>Copiloto Industrial NLP & RAG — Pungo Tech</h1>
      <p>Triaje Automático JSON · Extracción NER & Grafos · Radar de Turnos · Asistente SOP Auditable</p>
    </div>
    """,
    unsafe_allow_html=True,
)

tab1, tab2, tab3, tab4 = st.tabs([
    "1. Triaje OTs (JSON Mode)",
    "2. Extractor NER & Grafo",
    "3. Radar de Turnos & Escalación",
    "4. Copiloto RAG (SOPs)",
])

with tab1:
    st.subheader("Clasificación Multi-Dimensional de Órdenes de Trabajo")
    PRESETS_OT = {
        "Falla Sello Bomba P-101A (Crítico)": (
            "Bomba P-101A presenta vibración de 7.2 mm/s y fuga activa de crudo por sello mecánico en prensa-estopa.",
            "Se ejecutó aislamiento LOTO, desmontaje de acople y reemplazo por sello mecánico tipo cartucho PTFE.",
        ),
        "Instrumento Descalibrado V-102": (
            "Válvula de control V-102 no responde a señal del controlador. Posicionador descalibrado.",
            "Se reemplazó transmisor por Rosemount modelo EJA530 y se calibró carrera 0-100%.",
        ),
        "Punto Caliente FCV-1002": (
            "Termografía detecta punto caliente en empaque del FCV-1002: 93°C. Riesgo de falla.",
            "Se redujo carga del FCV-1002 y se programó mantenimiento mayor. Temperatura estabilizada.",
        ),
        "Compresor M-201 Baja Eficiencia": (
            "Compresor M-201 con caída de eficiencia. Flujo actual 49% del nominal. Posible erosión en etapas.",
            "Se reemplazó impeller del M-201 con recubrimiento antierosión y se verificó balance dinámico.",
        ),
    }
    preset_sel = st.selectbox("Escenario de Orden de Trabajo:", list(PRESETS_OT.keys()))
    p_def, t_def = PRESETS_OT[preset_sel]
    col_in1, col_in2 = st.columns(2)
    prob_txt = col_in1.text_area("Descripción del Problema:", value=p_def, height=110)
    trab_txt = col_in2.text_area("Trabajo Realizado / Diagnóstico:", value=t_def, height=110)

    if st.button("Clasificar Orden de Trabajo", type="primary", key="btn_triage"):
        res_ot = classify_work_order(prob_txt, trab_txt, client)
        st.session_state["last_triage"] = res_ot
    if "last_triage" not in st.session_state:
        st.session_state["last_triage"] = classify_work_order(p_def, t_def, None)

    res_ot = st.session_state["last_triage"]
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Tipo de Orden", res_ot.get("tipo_orden", "-").upper())
    c2.metric("Prioridad", res_ot.get("prioridad", "-").upper())
    c3.metric("Sistema", res_ot.get("sistema", "-"))
    c4.metric("Modo de Falla", res_ot.get("modo_falla", "-"))
    st.success(f"**Justificación IA:** {res_ot.get('justificacion', '')}")
    with st.expander("Payload JSON listo para SAP PM / Maximo", expanded=True):
        st.json(res_ot)

with tab2:
    st.subheader("Extracción de Entidades (NER) y Grafo Equipo → Falla")
    ner_prob = st.text_area("Texto de Orden de Trabajo para NER:", value=f"{p_def} {t_def}", height=90, key="ner_txt")
    if st.button("Extraer Entidades Técnicas", type="primary", key="btn_ner"):
        st.session_state["last_ner"] = extract_entities(ner_prob, "", client)
    if "last_ner" not in st.session_state:
        st.session_state["last_ner"] = extract_entities(p_def, t_def, None)

    ner_res = st.session_state["last_ner"]
    st.markdown(highlight_ner_html(ner_prob, ner_res), unsafe_allow_html=True)
    col_g1, col_g2 = st.columns([1.0, 1.3])
    with col_g1:
        st.markdown("**Entidades Estructuradas**")
        st.json(ner_res)
    with col_g2:
        sist_filter = st.selectbox("Filtrar Grafo por Sistema (3,030 OTs):", sorted(wo_df["sistema"].unique()), index=1)
        sub_wo = wo_df[wo_df["sistema"] == sist_filter]
        G = nx.Graph()
        top_eq = sub_wo["equipo_tag"].value_counts().head(6).index
        for eq in top_eq:
            G.add_node(eq, kind="equipo")
            for fm, cnt in sub_wo[sub_wo["equipo_tag"] == eq]["modo_falla"].value_counts().head(2).items():
                G.add_node(fm, kind="falla")
                G.add_edge(eq, fm, weight=cnt)
        fig_g, ax_g = plt.subplots(figsize=(7.5, 4.6))
        pos = nx.spring_layout(G, seed=42, k=1.35)
        nx.draw_networkx_edges(G, pos, ax=ax_g, edge_color="#94A3B8", width=1.8)
        nx.draw_networkx_nodes(G, pos, nodelist=[n for n, d in G.nodes(data=True) if d["kind"] == "equipo"], node_color=BLUE, node_size=1450, ax=ax_g)
        nx.draw_networkx_nodes(G, pos, nodelist=[n for n, d in G.nodes(data=True) if d["kind"] == "falla"], node_color=AMBER, node_size=1650, node_shape="s", ax=ax_g)
        labels_wrapped = {n: n.replace("_", "\n") for n in G.nodes()}
        nx.draw_networkx_labels(G, pos, labels=labels_wrapped, font_size=7.5, font_weight="bold", font_color="white", ax=ax_g)
        ax_g.margins(0.18)
        ax_g.set_title(f"Subgrafo Equipo → Falla ({sist_filter})")
        ax_g.axis("off")
        st.pyplot(fig_g, use_container_width=True)
        plt.close(fig_g)

with tab3:
    st.subheader("Radar de Cambios de Turno y Escalación de Vibración")
    col_f1, col_f2 = st.columns(2)
    turno_sel = col_f1.multiselect("Turnos:", sorted(logs_df["turno"].unique()), default=sorted(logs_df["turno"].unique()))
    area_sel = col_f2.selectbox("Área de Planta:", ["Todas"] + sorted(logs_df["area"].unique()))
    f_logs = logs_df[logs_df["turno"].isin(turno_sel)].copy()
    if area_sel != "Todas":
        f_logs = f_logs[f_logs["area"] == area_sel]

    f_logs["vib_score"] = f_logs["entrada"].str.lower().apply(
        lambda t: 6 if "crítica" in str(t) else (5 if "severa" in str(t) else (4 if "preocupante" in str(t) else (3 if "notable" in str(t) else (2 if "vibr" in str(t) else 1))))
    )
    k1, k2, k3 = st.columns(3)
    k1.markdown(f'<div class="kpi-card"><div class="kpi-val">{len(f_logs):,}</div><div class="kpi-lbl">Bitácoras Filtradas</div></div>', unsafe_allow_html=True)
    k2.markdown(f'<div class="kpi-card" style="border-left-color:{AMBER};"><div class="kpi-val">{(f_logs["tipo_entrada"]=="anomalia").sum()}</div><div class="kpi-lbl">Anomalías Reportadas</div></div>', unsafe_allow_html=True)
    k3.markdown(f'<div class="kpi-card" style="border-left-color:{RED};"><div class="kpi-val">{(f_logs["vib_score"]>=4).sum()}</div><div class="kpi-lbl">Alertas Precursoras (Nivel ≥ 4)</div></div>', unsafe_allow_html=True)

    vib_only = f_logs[f_logs["vib_score"] >= 2].copy()
    if not vib_only.empty:
        vib_only["sem"] = vib_only["fecha_hora"].dt.to_period("W").dt.to_timestamp()
        sem_avg = vib_only.groupby("sem")["vib_score"].mean()
        fig_v, ax_v = plt.subplots(figsize=(11, 3.6))
        ax_v.plot(sem_avg.index, sem_avg.values, "o-", color=RED, linewidth=2)
        ax_v.axhline(3.0, color=AMBER, linestyle="--", label="Umbral Escalación (3.0)")
        ax_v.set_ylabel("Intensidad Léxica (1–6)")
        ax_v.set_title("Tendencia de Severidad en Menciones de Vibración")
        ax_v.legend()
        st.pyplot(fig_v, use_container_width=True)
        plt.close(fig_v)

    st.markdown("**Top 6 Entradas Prioritarias para Entrega de Turno**")
    st.dataframe(
        f_logs.sort_values(["vib_score", "fecha_hora"], ascending=[False, False])[
            ["log_id", "fecha_hora", "turno", "area", "tipo_entrada", "vib_score", "entrada"]
        ].head(6),
        use_container_width=True,
    )

with tab4:
    st.subheader("Copiloto RAG de Procedimientos Técnicos (12 SOPs Auditados)")
    rag_index = get_rag_index(sop_chunks, active_key)
    PRESETS_RAG = [
        "¿Cuál es el procedimiento para cambiar el sello mecánico de la bomba P-101A?",
        "¿Cuál fue la causa raíz de la falla de la bomba P-101A en julio 2023?",
        "¿Qué límite de LEL y H2S exige el permiso de trabajo en caliente?",
        "¿Cuáles son los criterios de vibración para compresores centrífugos?",
        "¿Cuál es la receta del reactor nuclear de fusión ITER en Francia?",
    ]
    q_preset = st.selectbox("Preguntas técnicas sugeridas:", PRESETS_RAG)
    q_user = st.text_input("Consulta técnica:", value=q_preset, key="rag_q")

    if st.button("Consultar Copiloto RAG", type="primary", key="btn_rag") or "last_rag" not in st.session_state:
        if rag_index["mode"] == "openai" and client:
            q_vec = np.array(client.embeddings.create(input=q_user, model="text-embedding-3-small").data[0].embedding, dtype=np.float64)
        else:
            q_vec = rag_index["vec"].transform([q_user]).toarray()[0]
        mat = rag_index["matrix"]
        norms = np.linalg.norm(mat, axis=1) * (np.linalg.norm(q_vec) + 1e-12)
        sims = np.dot(mat, q_vec) / np.maximum(norms, 1e-12)
        top_idx = sims.argsort()[-3:][::-1]
        retrieved = [{"source": sop_chunks[i]["source"], "text": sop_chunks[i]["text"], "sim": float(sims[i])} for i in top_idx]
        max_sim = retrieved[0]["sim"] if retrieved else 0.0
        min_thresh = 0.28 if rag_index["mode"] == "openai" else 0.08
        if max_sim < min_thresh:
            ans = f"GUARDRAIL ACTIVO: Similitud máxima ({max_sim:.3f}) debajo del umbral ({min_thresh}). Consulta fuera de los 12 SOPs auditados."
        elif client:
            ctx = "\n\n---\n\n".join(f"[Fuente: {r['source']}]\n{r['text']}" for r in retrieved)
            resp = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Asistente técnico de planta. Responde SOLO con el contexto y cita [Fuente: archivo]."},
                    {"role": "user", "content": f"Contexto:\n{ctx}\n\nPregunta: {q_user}"},
                ],
                temperature=0.15,
                max_tokens=450,
            )
            ans = resp.choices[0].message.content
        else:
            ans = f"[Extracto de {retrieved[0]['source']}]\n{retrieved[0]['text']}"
        st.session_state["last_rag"] = {"q": q_user, "ans": ans, "retrieved": retrieved, "guardrail": max_sim < min_thresh}

    rag_out = st.session_state["last_rag"]
    if rag_out["guardrail"]:
        st.warning(rag_out["ans"])
    else:
        st.info(rag_out["ans"])

    st.markdown("**Evidencia Recuperada (Top 3 Chunks por Similitud Coseno)**")
    for r in rag_out["retrieved"]:
        with st.expander(f"{r['source']} — Similitud Coseno: {r['sim']:.3f}"):
            st.markdown(r["text"])
