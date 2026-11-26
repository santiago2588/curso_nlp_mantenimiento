# Plan de Mantenimiento Preventivo — Programa Anual

## 1. Filosofía de Mantenimiento
La facilidad de producción opera bajo una estrategia de mantenimiento que combina:
- **Mantenimiento Preventivo (PM):** Intervalos fijos basados en horas de operación o calendario
- **Mantenimiento Predictivo (PdM):** Monitoreo de condición (vibración, termografía, análisis de aceite)
- **Mantenimiento Correctivo (CM):** Reparación de fallas no anticipadas

La distribución objetivo es: 60% PM + PdM, 40% CM.

## 2. Programa de Mantenimiento por Sistema

### 2.1 Sistema de Bombeo (P-101A/B, P-102, P-201, P-202, P-301)

| Actividad | Frecuencia | Especialidad | Duración Est. |
|-----------|-----------|-------------|---------------|
| Inspección visual y operativa | Diaria | Operaciones | 15 min |
| Lubricación de rodamientos | Mensual | Mecánica | 30 min |
| Medición de vibración | Mensual | Predictivo | 45 min |
| Verificación de alineación | Trimestral | Mecánica | 2 hrs |
| Termografía de motor y bomba | Trimestral | Predictivo | 30 min |
| Análisis de aceite lubricante | Trimestral | Predictivo | Muestra |
| Cambio de aceite lubricante | Semestral | Mecánica | 1 hr |
| Mantenimiento mayor (overhaul) | 18 meses | Mecánica | 3-5 días |
| Prueba de bomba contra incendio P-501 | Semanal | Operaciones | 30 min |

### 2.2 Sistema de Compresión (C-101, C-102, C-103)

| Actividad | Frecuencia | Especialidad | Duración Est. |
|-----------|-----------|-------------|---------------|
| Monitoreo en línea de vibración | Continuo | Predictivo | Auto |
| Ronda operativa | Cada 4 hrs | Operaciones | 20 min |
| Análisis de aceite lubricante | Mensual | Predictivo | Muestra |
| Cambio de filtros de aceite | Según ΔP | Mecánica | 1 hr |
| Inspección de válvulas anti-surge | Trimestral | Instrumentación | 2 hrs |
| Boroscopia de etapas | Anual | Predictivo | 4 hrs |
| Overhaul mayor | 4-5 años | Mecánica | 2-3 semanas |

### 2.3 Sistema de Separación (V-101, V-102, V-103)

| Actividad | Frecuencia | Especialidad | Duración Est. |
|-----------|-----------|-------------|---------------|
| Verificación de niveles | Cada turno | Operaciones | 10 min |
| Drenaje de agua y sedimentos | Diario | Operaciones | 20 min |
| Inspección de instrumentos de nivel | Mensual | Instrumentación | 1 hr |
| Calibración de transmisores | Semestral | Instrumentación | 2 hrs |
| Inspección interna | Anual (durante parada) | Mecánica | 2-3 días |
| Inspección de espesores (UT) | Anual | Inspección | 4 hrs |
| Prueba de válvulas de seguridad | Anual | Mecánica | 2 hrs |

### 2.4 Sistema Eléctrico (M-101A, M-201, G-101)

| Actividad | Frecuencia | Especialidad | Duración Est. |
|-----------|-----------|-------------|---------------|
| Termografía de tableros y conexiones | Trimestral | Predictivo | 2 hrs |
| Megado de motores | Semestral | Eléctrica | 1 hr/motor |
| Inspección de cables y conexiones | Semestral | Eléctrica | 2 hrs |
| Prueba de generador de emergencia | Mensual | Eléctrica | 1 hr |
| Mantenimiento de generador diesel | Trimestral | Mecánica | 4 hrs |
| Cambio de aceite de transformador | Según análisis | Eléctrica | 4 hrs |

### 2.5 Instrumentación y Control

| Actividad | Frecuencia | Especialidad | Duración Est. |
|-----------|-----------|-------------|---------------|
| Verificación de lazos de control | Mensual | Instrumentación | 1 hr/lazo |
| Calibración de transmisores de presión | Semestral | Instrumentación | 1 hr |
| Calibración de transmisores de flujo | Semestral | Instrumentación | 1.5 hrs |
| Calibración de analizador de H2S | Mensual | Instrumentación | 2 hrs |
| Prueba de sistemas de paro (ESD) | Anual | Instrumentación | 1 día |
| Respaldo de programa de PLC | Trimestral | Instrumentación | 1 hr |
| Prueba de detectores de gas y fuego | Semestral | Instrumentación | 4 hrs |

## 3. Paradas Programadas

### 3.1 Parada General (cada 3-4 años)
- Duración: 3-4 semanas
- Alcance: inspección interna de recipientes, overhaul de compresores, cambio de internos de separadores
- Planificación: inicia 12 meses antes
- Requiere: scaffolding, equipo de izaje, contratistas especializados

### 3.2 Mini-paradas (anuales)
- Duración: 3-5 días
- Alcance: trabajos que requieren paro parcial de producción
- Ejemplo: cambio de válvulas de seguridad, inspección de intercambiadores

## 4. Indicadores de Desempeño (KPIs)

| KPI | Meta | Fórmula |
|-----|------|---------|
| Cumplimiento de PM | > 95% | OTs PM completadas / OTs PM programadas |
| MTBF (bombas) | > 8,000 hrs | Horas operación / Número de fallas |
| MTTR (bombas) | < 8 hrs | Suma horas reparación / Número de fallas |
| Disponibilidad mecánica | > 97% | (Hrs calendario - Hrs fuera) / Hrs calendario |
| Ratio PM/CM | > 1.5 | Horas PM / Horas CM |
| Backlog de mantenimiento | < 4 semanas | OTs pendientes × horas promedio / Capacidad semanal |
