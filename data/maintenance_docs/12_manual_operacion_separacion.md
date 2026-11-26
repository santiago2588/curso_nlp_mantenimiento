# Sistema de Separación de Producción — Manual de Operación

## 1. Descripción General
El sistema de separación de producción consta de tres recipientes principales que se encargan de separar el fluido multifásico proveniente de los pozos productores en sus fases: gas, crudo y agua producida.

### Esquema de Proceso
```
Pozos → Cabezal de Producción → V-101 (Separador Trifásico)
                                    ├── Gas → V-201 (Scrubber) → C-101 (Compresor)
                                    ├── Crudo → E-101 (Intercambiador) → TK-101/102
                                    └── Agua → V-301 (Tratamiento) → TK-201 → Reinyección
```

## 2. Separador Trifásico V-101

### 2.1 Parámetros de Operación Normal
| Parámetro | Valor Normal | Alarma L | Alarma H | Paro |
|-----------|-------------|----------|----------|------|
| Presión (psi) | 75-85 | 60 | 95 | 110 |
| Temperatura (°C) | 55-65 | -- | 80 | 90 |
| Nivel crudo (%) | 40-60 | 20 | 80 | 85/15 |
| Nivel interface (%) | 25-45 | 15 | 55 | 60/10 |
| Nivel de arena (cm) | 0-15 | -- | 20 | 30 |

### 2.2 Válvulas de Control Asociadas
- **FCV-1002:** Control de flujo de crudo a tanques. Controlada por LC-1504 (nivel de crudo).
- **FCV-1003:** Control de flujo de agua a tratamiento. Controlada por LC-1505 (nivel interface).
- **PCV-1001:** Control de presión del separador. Envía gas a scrubber V-201.

### 2.3 Procedimiento de Arranque
1. Verificar que todas las válvulas de drenaje estén cerradas
2. Verificar instrumentación operativa (niveles, presión, temperatura)
3. Abrir válvula de salida de gas (PCV-1001 en automático)
4. Abrir válvula de entrada de fluido del cabezal gradualmente
5. Esperar establecimiento de niveles (15-20 minutos)
6. Poner lazos de control de nivel en automático (FCV-1002, FCV-1003)
7. Monitorear BS&W del crudo de salida (máximo 1% BS&W)

### 2.4 Procedimiento de Paro Normal
1. Cerrar válvula de entrada del cabezal de producción
2. Esperar que niveles bajen a 20%
3. Cerrar válvulas de salida de crudo y agua
4. Despresurizar por válvula de venteo a tea (flare)
5. Drenar remanente por válvula de fondo

### 2.5 Problemas Comunes y Soluciones

**Problema: BS&W alto en crudo de salida (> 1%)**
- Verificar nivel de interface: puede estar alto → abrir más FCV-1003
- Verificar químico demulsificante: dosis adecuada, punto de inyección
- Verificar temperatura: si baja, la separación empeora
- Verificar si hay emulsión estable → contactar ing. de proceso

**Problema: Carry-over de líquido al gas**
- Verificar nivel de crudo: puede estar alto → abrir más FCV-1002
- Verificar presión del separador: presión baja → gas más rápido
- Verificar internos: malla coalescedora puede estar dañada o saturada

**Problema: Acumulación de arena**
- Monitorear detector de arena (AT-1510)
- Realizar drenaje de arena por válvulas de fondo (periódico o automático)
- Si acumulación excesiva: programar limpieza interna

## 3. Scrubber de Succión V-201

### Función
Proteger el compresor C-101 de líquidos arrastrados en el gas. Última barrera antes del compresor.

### Parámetros Operativos
- Presión: 5-8 bar (misma que succión del compresor)
- Nivel máximo: 40% (alarma alta), 60% (paro del compresor)
- Drenaje automático a separador V-101

### Criticidad
**Si el nivel del scrubber sube rápidamente, puede indicar un problema mayor aguas arriba (carry-over del separador V-101). Verificar inmediatamente condiciones del V-101.**

## 4. Tanque de Lavado V-301

### Función
Tratamiento final del agua producida antes de reinyección. Permite asentamiento gravitacional para remover trazas de crudo.

### Requisitos de Calidad del Agua
- Contenido de aceite: < 40 ppm (hacia reinyección)
- Sólidos suspendidos: < 5 ppm
- Contenido de O2: < 50 ppb (prevención de corrosión downhole)

## 5. Rondas del Operador

### Cada Turno (8 horas)
1. Verificar presiones y temperaturas de separadores
2. Verificar niveles de crudo e interface en V-101
3. Drenar agua acumulada en puntos bajos de líneas
4. Verificar que no haya fugas visibles
5. Registrar lecturas en bitácora de turno
6. Verificar drenaje de arena (si aplica)

### Diario
1. Tomar muestra de crudo de salida V-101 para BS&W
2. Tomar muestra de agua de V-301 para contenido de aceite
3. Verificar consumo de químicos (demulsificante, inhibidor)
4. Reportar anomalías al supervisor
