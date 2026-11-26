# NLP para Mantenimiento Industrial: De Órdenes de Trabajo a Inteligencia con IA

**Curso Oficial de Pungo Academy (Nivel Avanzado · ~3 Horas)**  
Instructor: **Santiago Zapata, PhD** · **Pungo Tech** (`PUNGO TECH S.A.S.`)  
`www.pungoapp.com` | `contacto@pungoapp.com` | Pungo Tech · Quito, Ecuador

---

## Descripción General

El **80% del conocimiento operativo de una planta de procesos** reside en texto libre no estructurado: órdenes de trabajo (MWOs) en CMMS, bitácoras de cambio de turno, manuales OEM, SOPs de seguridad e informes de incidentes HSE.

Este repositorio contiene los **7 Google Colab Notebooks ejecutables**, el **Copiloto interactivo en Streamlit** y los **datasets industriales reales** del curso para transformar texto sucio de campo en modelos clasificadores, payloads JSON listos para SAP PM / Maximo, grafos de conocimiento Equipo → Falla, alertas tempranas de deterioro y asistentes RAG auditables.

---

## Modalidad Dual-Mode (OpenAI API + Fallback Local Determinístico)

Todos los notebooks (`02`–`07`) y la aplicación Streamlit (`app/app_nlp_mantenimiento.py`) operan automáticamente en **Dual-Mode**:

1. **OpenAI API Live (`gpt-4o-mini` + `text-embedding-3-small`):** configura tu clave en `OPENAI_API_KEY` (Google Colab userdata / variable de entorno / barra lateral de Streamlit).
2. **Fallback Local Determinístico:** si ejecutas sin clave API en redes corporativas aisladas o pruebas rápidas offline, cada componente activa respaldo basado en `TfidfVectorizer`, expresiones regulares y extracción verificada sin errores.

---

## Contenido del Repositorio

### Notebooks (`notebooks/`)
| # | Notebook | Enfoque Técnico |
|---|---|---|
| 01 | `01_preprocesamiento_texto.ipynb` | Limpieza preservando tags (`P-101A`) y unidades (`93°C`, `7.2 mm/s`), expansión de jerga, tokenización y TF-IDF sobre `3,030` OTs. |
| 02 | `02_clasificacion_modos_falla.ipynb` | Benchmark riguroso: TF-IDF + Regresión Logística (`98.8%` en test completo `n=578`), GPT Zero-Shot (`94.0%`), Few-Shot sin fuga de datos (`88.0%`) y Embeddings `1,536D` (`96.0%` con solo `n=200` train). |
| 03 | `03_categorizacion_ordenes.ipynb` | Triaje multi-dimensional en OpenAI `json_object` para CMMS (`tipo_orden`, `prioridad`, `12` sistemas reales), auditoría de ruido histórico y economía (`$0.000096/OT`). |
| 04 | `04_extraccion_entidades.ipynb` | NER híbrido Regex (`89.1%` tags, `50.1%` mediciones) + `gpt-4o-mini` sobre problema+trabajo y grafo bipartito `Equipo → Falla` en NetworkX. |
| 05 | `05_deteccion_tendencias.ipynb` | Analítica temporal de `1,586` bitácoras de turno, estacionalidad de corrosión (Jun–Oct), radar multi-alerta (`872` señales), scoring GPT `1–10` y escala léxica precursora de vibración (`1–6`). |
| 06 | `06_asistente_rag.ipynb` | Motor RAG transparente en NumPy puro (`85` chunks estructurales sobre `12` SOPs = `47.2 KB`), similitud coseno y guardrail anti-alucinación en dos niveles (`sim < 0.28`). |
| 07 | `07_caso_estudio_incidentes_hse.ipynb` | **Capstone Final:** auditoría de `500` incidentes HSE, imputación JSON Mode de `20` filas sin severidad, ranking de activos críticos (`GAS-001`, `V-301`) y verificación RAG OSHA/LEL/H2S/LOTO. |

### Aplicación en Vivo (`app/`)
Ejecuta localmente el Copiloto Industrial de 4 pestañas (**Triaje JSON · Extractor NER + Grafo · Radar de Turnos · Copiloto RAG**):

```bash
pip install -r app/requirements.txt
export OPENAI_API_KEY="tu-clave-opcional"
streamlit run app/app_nlp_mantenimiento.py
```

### Datasets y Biblioteca Normativa (`data/`)
- `curso_nlp_work_orders.csv` — `3,030` órdenes de trabajo (`17` columnas, `$35.3M USD` históricos, `37` equipos en `12` sistemas).
- `curso_nlp_operator_logs.csv` — `1,586` entradas cronológicas de bitácoras de entrega de turno.
- `curso_nlp_incident_reports.csv` — `500` reportes reales de incidentes de seguridad HSE (`2023-01-02` → `2024-12-29`).
- `maintenance_docs/` — `12` procedimientos SOP y manuales OEM auditados (`01_proc_mto_bombas_centrifugas.md` .. `12_manual_operacion_separacion.md`).
- `rag_embeddings_cache.npz` — Caché vectorial pre-computado para consulta instantánea en Streamlit.

También disponibles vía CDN público de Pungo Academy:
`https://d29ikw7e1z6k4e.cloudfront.net/curso_nlp/curso_nlp_work_orders.csv`
`https://d29ikw7e1z6k4e.cloudfront.net/curso_nlp/curso_nlp_operator_logs.csv`
`https://d29ikw7e1z6k4e.cloudfront.net/curso_nlp/curso_nlp_incident_reports.csv`

---

Inscríbete al curso completo en vídeo (~3 horas, evaluaciones y certificado oficial) en **[academy.pungoapp.com](https://academy.pungoapp.com)**.
