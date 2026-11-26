# Gestión de Corrosión e Integridad Mecánica

## 1. Objetivo
Establecer los lineamientos para el programa de integridad mecánica y gestión de corrosión de la facilidad de producción, en cumplimiento con API 510, API 570 y API 653.

## 2. Mecanismos de Daño Identificados

### 2.1 Corrosión Interna por CO2
- **Equipos afectados:** Líneas de producción multifásica, separadores, tuberías de agua producida
- **Mecanismo:** Formación de ácido carbónico (H2CO3) en presencia de agua y CO2
- **Velocidad típica:** 0.1 - 0.5 mm/año (sin tratamiento), < 0.1 mm/año (con inhibidor)
- **Monitoreo:** Cupones de corrosión, medición UT, probetas electroquímicas
- **Mitigación:** Inyección de inhibidor de corrosión (dosis: 20-50 ppm continuo)

### 2.2 Corrosión por H2S (Sulfhídrico)
- **Equipos afectados:** Tuberías de gas, compresores, scrubbers
- **Mecanismo:** Ataque por ácido sulfhídrico, riesgo de SSC (Sulfide Stress Cracking)
- **Concentración de H2S:** 50-200 ppm en gas
- **Requisitos de material:** NACE MR0175/ISO 15156 (dureza máx 22 HRC)
- **Monitoreo:** Analizador en línea AT-1505, inspección visual, UT

### 2.3 Corrosión Externa
- **Equipos afectados:** Todos los equipos y tuberías expuestos a ambiente marino
- **Mecanismo:** Corrosión atmosférica acelerada por salinidad y humedad
- **Mitigación:** Sistema de pintura: primer epóxico + acabado poliuretano
- **Inspección:** Visual anual, UT en zonas sin recubrimiento

### 2.4 Corrosión Bajo Aislamiento (CUI)
- **Equipos afectados:** Líneas y equipos con aislamiento térmico operando entre 50-175°C
- **Mecanismo:** Ingreso de humedad bajo el aislamiento → corrosión acelerada
- **Inspección:** Remoción de aislamiento en zonas susceptibles, termografía
- **Frecuencia:** Inspección del 10% del aislamiento cada año (rotativo)

### 2.5 Erosión
- **Equipos afectados:** Codos de tuberías multifásicas, internos de separadores, impellers de bombas
- **Mecanismo:** Impacto de partículas sólidas (arena de formación)
- **Monitoreo:** Detector de arena, medición UT en codos, monitoreo de vibración
- **Mitigación:** Desareadoras en cabeza de pozo, límite de velocidad en tuberías

## 3. Programa de Inspección

### 3.1 Tuberías (API 570)
| Clasificación | Intervalo Inspección | Criterio |
|--------------|---------------------|----------|
| Clase 1 (alta criticidad) | Máx 5 años | Servicio H2S, alta T, alta P |
| Clase 2 (media) | Máx 10 años | Servicio intermedio |
| Clase 3 (baja) | Máx 10 años | Servicios auxiliares, agua |

### 3.2 Recipientes a Presión (API 510)
| Tipo | Inspección Externa | Inspección Interna |
|------|-------------------|-------------------|
| Separadores V-101/102/103 | Anual | Cada 5 años o durante parada |
| Scrubber V-201 | Anual | Cada 5 años |
| Tanque de lavado V-301 | Anual | Cada 3 años (servicio corrosivo) |

### 3.3 Tanques (API 653)
| Inspección | Frecuencia | Alcance |
|-----------|-----------|---------|
| Visual externa | Mensual | Condición general, asentamiento, fugas |
| Medición UT de pared | Cada 5 años | Circuitos definidos |
| Inspección interna de fondo | Cada 10 años | Requiere vaciado del tanque |

## 4. Técnicas de Inspección Utilizadas
- **UT convencional:** Medición de espesor puntual
- **UT de barrido (scan):** Mapeo de corrosión en áreas extensas
- **Radiografía (RT):** Soldaduras y detección de corrosión interna
- **Partículas magnéticas (MT):** Detección de grietas superficiales
- **Líquidos penetrantes (PT):** Detección de discontinuidades abiertas a superficie
- **Inspección visual (VT):** Primer filtro de inspección, siempre
- **Termografía infrarroja:** CUI, problemas eléctricos, refractario
- **Emisión acústica (AE):** Monitoreo de recipientes en servicio

## 5. Criterios de Aptitud para Servicio (FFS)
Cuando un equipo presenta condición por debajo de espesor mínimo de retiro, se puede realizar una evaluación de aptitud para servicio según API 579-1/ASME FFS-1 para determinar si puede continuar operando de forma segura con restricciones:

### Niveles de evaluación:
- **Nivel 1:** Evaluación simplificada (ingeniero de planta puede realizar)
- **Nivel 2:** Evaluación detallada (requiere ingeniero de integridad)
- **Nivel 3:** Análisis por elemento finito (requiere consultor especializado)

## 6. Inyección de Químicos de Tratamiento

### 6.1 Inhibidor de Corrosión
- **Producto:** NALCO EC1018A (o equivalente aprobado)
- **Punto de inyección:** Cabezal de producción, antes del separador V-101
- **Dosis:** 25 ppm sobre base agua total (ajustar según resultados de cupones)
- **Equipo:** Bomba dosificadora P-401
- **Frecuencia de monitoreo:** Verificar dosis diariamente, cupones trimestrales

### 6.2 Anti-incrustante
- **Producto:** NALCO 7348 (prevención de carbonato de calcio y sulfato de bario)
- **Punto de inyección:** Downhole (fondo de pozo) vía capilar
- **Dosis:** 10-15 ppm

### 6.3 Demulsificante
- **Producto:** Clariant PHASETREAT 466
- **Punto de inyección:** Línea de multifásico antes del separador
- **Dosis:** 30-50 ppm, ajustar según emulsión
