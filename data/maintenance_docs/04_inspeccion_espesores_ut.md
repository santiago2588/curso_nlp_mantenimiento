# Procedimiento de Inspección de Espesores por Ultrasonido (UT)

## 1. Objetivo
Establecer el procedimiento para la medición de espesores por ultrasonido en tuberías, recipientes y equipos de proceso de la facilidad de producción de crudo.

## 2. Alcance
Aplica a todos los equipos y tuberías sujetos al programa de integridad mecánica, incluyendo:
- Líneas de proceso (LN-CR-001, LN-GAS-001, LN-AG-001)
- Recipientes a presión (V-101, V-102, V-103, V-201, V-301)
- Tanques de almacenamiento (TK-101, TK-102, TK-201)
- Intercambiadores de calor (E-101, E-102)

## 3. Equipos de Medición
- Medidor de espesor ultrasónico: Olympus 38DL Plus o equivalente
- Transductores: D790 (alta temperatura), D791 (uso general)
- Acoplante: gel ultrasónico grado industrial
- Calibrador de referencia según ASTM E797

## 4. Circuitos de Inspección

### 4.1 Circuito CIR-001: Línea de crudo desde separador V-101 a tanque TK-101
- Total de puntos: 24 (TML - Thickness Measurement Locations)
- Frecuencia: semestral
- Material: A106 Gr.B, espesor nominal 8.18mm (6" Sch 40)
- Espesor mínimo requerido (t_min): 3.2mm (por cálculo ASME B31.3)
- Velocidad de corrosión histórica: 0.15 mm/año

### 4.2 Circuito CIR-002: Línea de agua producida a disposición
- Total de puntos: 18 TMLs
- Frecuencia: trimestral (alta velocidad de corrosión)
- Material: A106 Gr.B, espesor nominal 6.02mm (4" Sch 40)
- Espesor mínimo requerido: 2.8mm
- Velocidad de corrosión histórica: 0.45 mm/año
- Nota: inyección de inhibidor de corrosión en servicio

### 4.3 Circuito CIR-003: Cuerpo del separador V-101
- Total de puntos: 32 TMLs (distribución circunferencial y longitudinal)
- Frecuencia: anual
- Material: SA-516 Gr.70, espesor nominal 19mm
- Espesor mínimo requerido: 12.5mm (ASME Sec VIII Div 1)
- Velocidad de corrosión histórica: 0.08 mm/año

## 5. Procedimiento de Medición

### 5.1 Preparación de la Superficie
1. Remover pintura, óxido y depósitos en el punto de medición (área mínima 25mm × 25mm)
2. Utilizar cepillo de alambre o amoladora con disco de lija
3. La superficie debe quedar lisa y libre de irregularidades
4. Para equipos en servicio a alta temperatura (>60°C), utilizar transductor de alta temperatura

### 5.2 Calibración del Equipo
1. Calibrar con bloque de referencia del mismo material
2. Verificar calibración al inicio, cada 2 horas, y al final
3. Registrar calibración en formato FM-INSP-003

### 5.3 Toma de Lecturas
1. Aplicar acoplante en el punto de medición
2. Colocar el transductor perpendicular a la superficie
3. Tomar mínimo 3 lecturas por punto
4. Registrar el valor mínimo
5. Marcar el punto con pintura para futura referencia

## 6. Criterios de Evaluación

| Condición | Acción |
|-----------|--------|
| Espesor > t_min + 3mm | Monitoreo rutinario |
| t_min + 1mm < Espesor < t_min + 3mm | Incrementar frecuencia de inspección |
| t_min < Espesor < t_min + 1mm | Planificación de reemplazo/reparación |
| Espesor < t_min | Acción inmediata: evaluación de aptitud para servicio (FFS) |

## 7. Cálculo de Velocidad de Corrosión y Vida Remanente
- Velocidad de corrosión (CR) = (t_anterior - t_actual) / intervalo en años [mm/año]
- Vida remanente = (t_actual - t_min) / CR [años]
- Si vida remanente < 2 años → programar reemplazo en próxima parada
- Si vida remanente < 6 meses → acción inmediata

## 8. Registros
- Formato FM-INSP-001: Registro de espesores
- Base de datos: actualizar en sistema PCMS (Plant Condition Monitoring System)
- Informes: reporte de inspección con recomendaciones según API 570/API 510
