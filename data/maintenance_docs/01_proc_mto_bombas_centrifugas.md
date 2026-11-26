# Procedimiento de Mantenimiento Preventivo — Bombas Centrífugas

## 1. Objetivo
Establecer los pasos para la ejecución del mantenimiento preventivo de bombas centrífugas de transferencia de crudo en las estaciones de bombeo de la facilidad de producción.

## 2. Alcance
Aplica a todas las bombas centrífugas tipo API 610 instaladas en las estaciones de bombeo Norte y Sur (P-101A, P-101B, P-102, P-301).

## 3. Frecuencia
- Inspección visual: diaria (operador de campo)
- Mantenimiento menor: cada 3 meses
- Mantenimiento mayor (overhaul): cada 18 meses o 12,000 horas de operación

## 4. Herramientas y Materiales
- Juego de llaves combinadas (métricas)
- Llave de torque calibrada
- Alineador láser (Fixturlaser o equivalente)
- Lubricante: Mobilith SHC 460 o Shell Gadus S3
- Kit de sello mecánico (según tipo de bomba)
- Rodamientos de repuesto (6312, 6316 según modelo)
- Empaquetaduras y juntas

## 5. Procedimiento — Mantenimiento Menor (Trimestral)

### 5.1 Preparación
1. Obtener permiso de trabajo y análisis de riesgos (JSA)
2. Aislar eléctricamente el motor (Lock-Out/Tag-Out)
3. Cerrar válvulas de succión y descarga
4. Drenar la bomba si es necesario
5. Verificar que la presión residual sea cero

### 5.2 Inspección y Lubricación
1. Verificar nivel de aceite en cojinetes (si aplica nivel constante)
2. Re-engrasar rodamientos con lubricante especificado: 3 inyecciones de pistola de engrase
3. Verificar temperatura de rodamientos con pirómetro: máximo 80°C en operación
4. Verificar vibración en puntos 1H, 1V, 1A, 2H, 2V, 2A
   - Alarma H: 4.5 mm/s velocidad
   - Alarma HH: 7.1 mm/s velocidad
5. Inspeccionar sello mecánico: verificar que no haya fuga visible
6. Verificar alineación visual del acople
7. Inspeccionar base y pernos de anclaje

### 5.3 Verificaciones Operativas
1. Registrar presión de succión y descarga
2. Registrar corriente del motor
3. Verificar que no haya ruidos anormales
4. Verificar sistema de enfriamiento del sello (si aplica)

## 6. Procedimiento — Mantenimiento Mayor (Overhaul)

### 6.1 Desmontaje
1. Seguir pasos 5.1 para preparación
2. Desconectar acople del motor
3. Retirar guarda del acople
4. Desmontar cabezal de la bomba
5. Extraer rotor completo (impeller + eje)
6. Retirar sello mecánico
7. Extraer rodamientos

### 6.2 Inspección de Componentes
1. Inspeccionar impeller: buscar erosión, corrosión, grietas
   - Criterio de rechazo: pérdida de espesor > 15% del original
2. Inspeccionar eje: verificar runout con reloj comparador
   - Máximo runout: 0.025 mm TIR
3. Inspeccionar carcasa: buscar erosión en zona de contacto con impeller
4. Medir holguras internas con galgas
   - Holgura de desgaste máxima: consultar manual OEM

### 6.3 Reemplazo y Reensamble
1. Instalar rodamientos nuevos (precalentar a 80°C para montaje)
2. Instalar sello mecánico nuevo según manual del fabricante
3. Ensamblar rotor en carcasa
4. Montar cabezal
5. Aplicar torque de pernos según tabla del fabricante (patrón en estrella)
6. Conectar acople

### 6.4 Alineación
1. Realizar alineación láser del conjunto bomba-motor
2. Tolerancias de alineación:
   - Angular: máx 0.05 mm/100mm
   - Paralela: máx 0.05 mm
3. Registrar valores finales en reporte de mantenimiento

### 6.5 Pruebas Post-Mantenimiento
1. Realizar prueba de giro manual: verificar que gire libre
2. Arrancar bomba en vacío brevemente (< 30 segundos)
3. Abrir válvula de succión, luego descarga gradualmente
4. Registrar: presión, temperatura, vibración, corriente
5. Verificar ausencia de fuga en sello mecánico

## 7. Criterios de Aceptación
| Parámetro | Valor Normal | Alarma | Paro |
|-----------|-------------|--------|------|
| Vibración (mm/s vel) | < 3.0 | 4.5 | 7.1 |
| Temp. rodamiento (°C) | < 80 | 95 | 110 |
| Corriente motor (% FLA) | 60-90 | 95 | 105 |
| Fuga sello | Ninguna | Goteo leve | Flujo continuo |

## 8. Registros
- Completar formato FM-MTO-001 "Reporte de Mantenimiento Preventivo"
- Registrar datos de vibración en sistema SAP
- Actualizar horómetro del equipo
