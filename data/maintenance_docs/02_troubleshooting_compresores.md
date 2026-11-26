# Guía de Troubleshooting — Compresores Centrífugos de Gas

## 1. Objetivo
Proporcionar una guía de diagnóstico y resolución de problemas para los compresores centrífugos de gas de exportación y gas lift (C-101, C-102, C-103).

## 2. Síntomas Comunes y Diagnóstico

### 2.1 Alta Vibración

**Posibles causas:**
1. **Desbalanceo del rotor**
   - Diagnóstico: componente dominante a 1x RPM
   - Acción: balanceo dinámico en sitio o enviar rotor a taller
   - Frecuencia típica: después de incrustación o erosión

2. **Desalineación**
   - Diagnóstico: componente 2x RPM elevada (angular) o axial alta (paralela)
   - Acción: verificar y corregir alineación láser
   - Verificar: expansión térmica de la base

3. **Cojinete dañado**
   - Diagnóstico: frecuencias de defecto de rodamiento (BPFO, BPFI, BSF)
   - Acción: reemplazo del cojinete
   - Nota: verificar análisis de aceite para partículas metálicas

4. **Surge / operación inestable**
   - Diagnóstico: vibración intermitente con fluctuación de presión
   - Acción: verificar punto de operación vs curva del compresor
   - Precaución: el surge repetido causa daño acumulativo

### 2.2 Alta Temperatura de Descarga

**Posibles causas:**
1. **Relación de compresión excesiva**
   - Verificar: presión de succión baja o presión de descarga alta
   - Acción: ajustar condiciones de operación

2. **Válvulas de recirculación cerradas/dañadas**
   - Verificar: posición de válvula anti-surge
   - Acción: calibrar actuador de válvula

3. **Enfriador inter-etapa obstruido**
   - Verificar: delta T del enfriador vs diseño
   - Acción: limpiar (lado aire o lado gas según tipo)

4. **Eficiencia reducida por fouling interno**
   - Verificar: curva de eficiencia vs nueva
   - Acción: programar lavado en línea o apertura para limpieza

### 2.3 Caída de Presión de Descarga

**Posibles causas:**
1. **Desgaste de laberintos internos**
   - Holguras internas aumentadas → recirculación interna
   - Acción: overhaul programado para reemplazo de laberintos

2. **Fuga en válvula de recirculación**
   - Gas recircula al suministro en lugar de ir al proceso
   - Acción: inspeccionar y reparar válvula anti-surge

3. **Cambio en condiciones de gas**
   - Peso molecular o temperatura del gas diferentes al diseño
   - Acción: verificar análisis de gas y recalcular punto de operación

### 2.4 Alta Temperatura de Cojinetes

**Posibles causas:**
1. **Nivel bajo de aceite lubricante**
   - Acción: verificar nivel y rellenar con aceite especificado
   - Tipo de aceite: ISO VG 46 (turbina)

2. **Enfriador de aceite obstruido**
   - Verificar: temperatura de aceite antes y después del enfriador
   - Acción: limpiar enfriador E-201

3. **Cojinete dañado o con excesivo juego**
   - Verificar: análisis de aceite y vibración
   - Acción: reemplazo en próxima parada programada

4. **Desalineación**
   - Carga radial excesiva sobre cojinetes
   - Acción: verificar alineación

### 2.5 Disparo del Compresor

**Acciones inmediatas:**
1. No re-arrancar sin investigar la causa del disparo
2. Verificar panel de control: leer alarma/causa de disparo
3. Registrar parámetros del momento del disparo (DCS trends)
4. Notificar a mantenimiento y supervisor de operaciones

**Causas frecuentes de disparo:**
- Alta vibración (> 7.0 mm/s)
- Alta temperatura de cojinetes (> 120°C)
- Surge detectado (3 eventos en 1 minuto)
- Baja presión de aceite (< 1.5 bar)
- Alta temperatura de descarga (> 180°C)

## 3. Parámetros de Operación Normal

| Parámetro | C-101 | C-102 | C-103 |
|-----------|-------|-------|-------|
| Presión succión (bar) | 5-8 | 10-15 | 2-4 |
| Presión descarga (bar) | 45-55 | 80-100 | 10-15 |
| Temp descarga (°C) | 120-150 | 130-160 | 90-110 |
| Velocidad (RPM) | 9,500 | 11,200 | 8,000 |
| Vibración máx (mm/s) | 4.5 | 4.5 | 4.5 |
| Temp cojinete máx (°C) | 100 | 100 | 100 |
| Flujo aceite (l/min) | 45 | 55 | 30 |

## 4. Contactos de Emergencia
- Control de sala: Ext. 2001
- Supervisor de mantenimiento: Ext. 2050
- Ingeniero de confiabilidad: Ext. 2055
- Soporte OEM (Siemens): +1-800-XXX-XXXX
