# Análisis de Falla — Bomba Centrífuga P-101A (Caso Histórico)

## Información del Evento
- **Equipo:** P-101A — Bomba centrífuga de transferencia de crudo
- **Fecha del evento:** 15 de Julio de 2023
- **Tipo de falla:** Falla catastrófica de sello mecánico
- **Impacto:** Derrame de 200 litros de crudo, paro no programado de 36 horas
- **Costo total:** USD 85,000 (reparación + producción diferida)

## Cronología del Evento

### Semanas previas (señales precursoras)
- **25-Jun-2023:** Operador reporta goteo leve por sello mecánico de P-101A. Se genera OT-2024-01543 (prioridad normal).
- **02-Jul-2023:** Mantenimiento inspecciona, confirma goteo menor (~5 gotas/min). Se programa cambio de sello para próxima mini-parada (agosto).
- **08-Jul-2023:** Análisis de vibración muestra incremento de 15% en componente 1x en punto 1H. Valor: 3.8 mm/s (dentro de alarma pero tendencia ascendente).
- **12-Jul-2023:** Operador de turno noche reporta que goteo ha aumentado a ~20 gotas/min. No se escala a supervisión.

### Día del evento
- **15-Jul-2023, 03:15 hrs:** Alarma de alta vibración (7.2 mm/s) en P-101A. Operador reconoce alarma.
- **15-Jul-2023, 03:22 hrs:** Falla del sello mecánico. Fuga masiva de crudo por prensa-estopa.
- **15-Jul-2023, 03:25 hrs:** Paro automático por alta vibración HH.
- **15-Jul-2023, 03:30 hrs:** Activación de protocolo de derrame. P-101B arrancada como respaldo.
- **15-Jul-2023, 04:00 hrs:** Contención del derrame completada. Área asegurada.

## Análisis de Causa Raíz (ACR)

### Metodología: 5 ¿Por qué?

1. **¿Por qué falló el sello?** → Las caras del sello presentaban desgaste severo y carbonización.
2. **¿Por qué se desgastaron las caras?** → Operación con vibración progresiva causó movimiento axial del eje.
3. **¿Por qué había vibración progresiva?** → Desalineación menor que se agravó con el desgaste del acople.
4. **¿Por qué no se corrigió la desalineación?** → La última alineación fue hace 14 meses, y no se verificó después del último desmontaje parcial.
5. **¿Por qué no se verificó?** → No existe procedimiento que requiera verificación de alineación post-intervención parcial.

### Causa Raíz Identificada
**Causa raíz física:** Desgaste prematuro de sello mecánico por vibración inducida por desalineación progresiva.
**Causa raíz latente:** Ausencia de procedimiento de verificación de alineación después de intervenciones parciales.
**Causa raíz organizacional:** El reporte de goteo del operador (25-Jun) no fue escalado con la urgencia adecuada.

## Lecciones Aprendidas
1. Cualquier fuga de sello mecánico, por mínima que sea, debe ser evaluada por ingeniería de confiabilidad.
2. Tendencias de vibración ascendentes deben generar alertas automáticas en el sistema predictivo.
3. Toda intervención mecánica, incluso parcial, debe incluir verificación de alineación como paso obligatorio.

## Acciones Correctivas
| # | Acción | Responsable | Fecha Compromiso | Estado |
|---|--------|------------|-----------------|--------|
| 1 | Actualizar procedimiento FM-MTO-001 para incluir alineación post-intervención | Ing. Confiabilidad | 30-Ago-2023 | Completada |
| 2 | Implementar alertas automáticas de tendencia en sistema de vibración | Predictivo | 15-Sep-2023 | Completada |
| 3 | Capacitar operadores en criterios de escalamiento de fugas de sellos | Supervisión | 30-Jul-2023 | Completada |
| 4 | Instalar sensor de fuga continuo en P-101A y P-101B | Instrumentación | 30-Oct-2023 | En progreso |
| 5 | Cambiar sellos mecánicos de P-101A/B a tipo cartucho para facilitar instalación | Ing. Mecánico | Próxima parada | Pendiente |
