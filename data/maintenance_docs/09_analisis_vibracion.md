# Procedimiento de Análisis de Vibración — Monitoreo de Condición

## 1. Objetivo
Definir el procedimiento para la recolección y análisis de datos de vibración en equipos rotativos de la facilidad de producción.

## 2. Equipos en Programa de Vibración

### Ruta 1: Bombas de Proceso (mensual)
P-101A, P-101B, P-102, P-201, P-202, P-301, P-401, P-501

### Ruta 2: Compresores (quincenal)
C-101, C-102, C-103

### Ruta 3: Motores eléctricos y generador (mensual)
M-101A, M-201, G-101

## 3. Puntos de Medición
Para cada equipo rotativo se miden 6 puntos:
- **1H:** Cojinete lado acople, dirección horizontal
- **1V:** Cojinete lado acople, dirección vertical
- **1A:** Cojinete lado acople, dirección axial
- **2H:** Cojinete lado libre, dirección horizontal
- **2V:** Cojinete lado libre, dirección vertical
- **2A:** Cojinete lado libre, dirección axial

## 4. Criterios de Alarma (ISO 10816-3, Grupo 2)

| Zona | Velocidad (mm/s RMS) | Condición |
|------|---------------------|-----------|
| A | 0 - 2.8 | Buena — recién comisionado |
| B | 2.8 - 4.5 | Aceptable — operación a largo plazo |
| C | 4.5 - 7.1 | Alarma — planificar intervención |
| D | > 7.1 | Peligro — parar equipo |

## 5. Diagnóstico por Patrón de Vibración

### 5.1 Desbalanceo
- **Síntoma:** Componente dominante a 1x RPM en dirección radial
- **Causa:** Acumulación de depósitos, pérdida de material, impeller desgastado
- **Acción:** Balanceo en sitio o en taller

### 5.2 Desalineación Angular
- **Síntoma:** Componente 2x RPM elevada, vibración axial alta
- **Causa:** Alineación incorrecta, expansión térmica, hundimiento de base
- **Acción:** Re-alineación láser

### 5.3 Desalineación Paralela
- **Síntoma:** 1x RPM elevada, desfase de 180° entre cojinetes en dirección radial
- **Acción:** Re-alineación láser

### 5.4 Holgura Mecánica
- **Síntoma:** Múltiples harmónicos (1x, 2x, 3x, 4x...), forma de onda ruidosa
- **Causa:** Pernos flojos, holgura en cojinetes, juego en acople
- **Acción:** Inspección y apriete, reemplazo de cojinetes si necesario

### 5.5 Defectos de Rodamiento
- **Frecuencias características (dependen de geometría del rodamiento):**
  - BPFO: defecto en pista externa
  - BPFI: defecto en pista interna
  - BSF: defecto en elemento rodante
  - FTF: defecto en jaula
- **Evolución típica:**
  1. Etapa 1: frecuencias ultrasónicas (detección anticipada con enveloping)
  2. Etapa 2: frecuencias de defecto visibles en espectro
  3. Etapa 3: armónicos de frecuencias de defecto + bandas laterales
  4. Etapa 4: piso de ruido elevado, ruido audible, falla inminente
- **Acción:** Programar cambio antes de llegar a Etapa 3-4

### 5.6 Problemas Eléctricos en Motores
- **Síntoma:** Componente a 2x frecuencia de línea (120 Hz en 60 Hz)
- **Causa:** Excentricidad del rotor, barras rotas, problemas de estator
- **Prueba confirmatoria:** Desconectar motor y verificar si la vibración desaparece

## 6. Equipos de Medición
- Colector de datos: CSI 2140 (Emerson) o equivalente
- Acelerómetros: 100 mV/g, montaje magnético
- Software de análisis: AMS Machinery Health Manager

## 7. Reporte Mensual
El reporte mensual de vibración debe incluir:
1. Resumen ejecutivo: equipos en alerta, tendencias preocupantes
2. Tabla de valores globales por equipo y punto
3. Gráficos de tendencia de los últimos 12 meses
4. Espectros de equipos en condición Alarma o Peligro
5. Recomendaciones con prioridad y fecha sugerida
6. Seguimiento de recomendaciones anteriores

## 8. Indicadores
- **Cobertura del programa:** % de puntos medidos vs programados (meta: > 95%)
- **Detección anticipada:** % de fallas detectadas antes del evento (meta: > 80%)
- **P-F interval promedio:** Tiempo entre primera detección y falla funcional
