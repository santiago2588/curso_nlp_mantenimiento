# Procedimiento de Calibración de Instrumentos de Campo

## 1. Objetivo
Establecer el procedimiento para la calibración de transmisores de presión, temperatura, flujo y nivel instalados en la facilidad de producción.

## 2. Instrumentos Cubiertos
| Tag | Tipo | Rango | Ubicación |
|-----|------|-------|-----------|
| PT-1501 | Presión | 0-150 psi | Separador V-101 |
| PT-1502 | Presión | 0-500 psi | Descarga C-101 |
| TT-1502 | Temperatura | 0-200°C | Línea de crudo |
| TT-1503 | Temperatura | 0-300°C | Descarga C-101 |
| FT-1503 | Flujo | 0-50 MMSCFD | Gas exportación |
| LT-1504 | Nivel | 0-100% | Separador V-101 |
| AT-1505 | H2S | 0-100 ppm | Gas a compresor |

## 3. Equipos de Calibración
- Calibrador de presión: Fluke 721 (0-1500 psi)
- Calibrador de temperatura: Fluke 714B con RTD/TC de referencia
- HART Communicator: Emerson 475 o AMS Trex
- Multímetro de proceso: Fluke 789

## 4. Procedimiento General

### 4.1 Transmisores de Presión
1. Aislar el transmisor del proceso (cerrar válvula de bloqueo del manifold)
2. Abrir válvula de venteo para despresurizar la cámara
3. Conectar calibrador de presión en manifold de 3 o 5 válvulas
4. Verificar en 5 puntos (0%, 25%, 50%, 75%, 100% del rango)
5. En cada punto: registrar presión aplicada vs lectura del transmisor
6. Criterio: error ≤ ±0.1% del span
7. Si fuera de tolerancia: ajustar trim con HART
8. Repetir verificación post-ajuste (As-Left)

### 4.2 Transmisores de Temperatura
1. Retirar termopozo del proceso (si es posible)
2. Insertar sensor de referencia y sensor del transmisor en baño seco
3. Verificar en 5 puntos a lo largo del rango
4. Criterio: error ≤ ±0.5°C (para RTD), ±1.0°C (para termocupla)
5. Si fuera de tolerancia: ajustar trim
6. Re-instalar termopozo y verificar lectura en DCS

### 4.3 Transmisores de Nivel
1. Para transmisores de presión diferencial: simular nivel con columna de líquido
2. Para radar/ultrasonido: verificar con medición manual (cinta/regla)
3. Criterio: error ≤ ±1% del span
4. Verificar alarmas de nivel alto y bajo

### 4.4 Analizadores de Gas (H2S)
1. Preparar de gas de calibración certificado (gas span: concentración conocida)
2. Purgar con gas cero (nitrógeno) - verificar lectura cero
3. Aplicar gas span - verificar lectura
4. Criterio: error ≤ ±2% de la lectura del span
5. Frecuencia: mensual (por razones de seguridad)

## 5. Registros
- Formato FM-INST-001: Registro de calibración
- Incluir: As-Found, ajustes realizados, As-Left
- Certificado de calibración de patrones de referencia
- Registro en sistema CMMS (SAP PM)
