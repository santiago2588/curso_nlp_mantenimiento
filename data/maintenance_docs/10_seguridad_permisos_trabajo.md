# Procedimiento de Seguridad — Gestión de Cambios (MOC) y Permisos de Trabajo

## 1. Gestión de Cambios (Management of Change - MOC)

### 1.1 Definición
Cualquier modificación temporal o permanente a equipos, procesos, procedimientos, materiales o sustancias químicas que difiera del diseño original requiere un proceso formal de Gestión de Cambios.

### 1.2 Cambios que Requieren MOC
- Modificación de equipos de proceso o instalaciones
- Cambio de materiales de construcción
- Cambio de parámetros de operación fuera de ventana operativa aprobada
- Reemplazo de equipos por modelos o marcas diferentes
- Cambio de químicos de proceso o sus concentraciones
- Modificaciones a la lógica de control o sistemas de seguridad

### 1.3 Cambios que NO Requieren MOC (reemplazo en especie)
- Reemplazo de equipos o componentes por la misma marca, modelo y especificación
- Mantenimiento rutinario según procedimiento aprobado
- Calibración de instrumentos sin cambio de rango

### 1.4 Proceso de MOC
1. Solicitante completa formato FM-MOC-001
2. Revisión por ingeniería de proceso
3. Evaluación de riesgos (HAZOP simplificado si aplica)
4. Aprobación por comité multidisciplinario
5. Ejecución del cambio con supervisión
6. Actualización de documentación (P&IDs, procedimientos, data sheets)
7. Comunicación y entrenamiento al personal afectado
8. Cierre del MOC con verificación de campo

## 2. Permisos de Trabajo

### 2.1 Tipos de Permisos
| Tipo | Color | Aplica cuando |
|------|-------|---------------|
| Trabajo en Frío | Verde | Sin fuente de ignición, riesgo menor |
| Trabajo en Caliente | Rojo | Soldadura, esmerilado, corte |
| Entrada a Espacio Confinado | Amarillo | Recipientes, tanques, excavaciones |
| Trabajo en Altura | Azul | Trabajos > 1.8m de altura |
| Trabajo Eléctrico | Naranja | Circuitos > 50V o en áreas clasificadas |

### 2.2 Procedimiento de Permiso de Trabajo
1. Solicitante (supervisor de mantenimiento) identifica los riesgos
2. Emisor (supervisor de operaciones) verifica condiciones del área
3. Se completan mediciones de gas (LEL, O2, H2S) si aplica
4. Se implementan aislamientos y LOTO necesarios
5. Se firma el permiso por ambas partes
6. Trabajo se ejecuta bajo las condiciones aprobadas
7. Al finalizar, cierre del permiso verificando que el área queda segura

### 2.3 Mediciones de Gas Requeridas
- **LEL (Límite Explosivo Inferior):** Máximo 10% LEL para trabajo en caliente
- **Oxígeno:** 19.5% - 23.5% para entrada a espacio confinado
- **H2S:** Máximo 10 ppm (STEL)
- **Frecuencia:** Inicial + cada 4 horas (o continuo con detector personal)

## 3. Lock-Out / Tag-Out (LOTO)

### 3.1 Aislamientos Mecánicos
- Cerrar y bloquear válvulas de proceso con candado personal
- Instalar bridas ciegas o spades donde sea necesario
- Drenar y despresurizar líneas y equipos
- Verificar cero energía (abrir drenaje o venteo)

### 3.2 Aislamientos Eléctricos
- Abrir breaker principal en MCC o switchgear
- Instalar candado personal y tarjeta de bloqueo
- Probar arranque para verificar aislamiento efectivo
- Para equipos con VDF: aislar en ambos lados (entrada y salida)

### 3.3 Reglas de LOTO
- Cada persona que trabaje en el equipo coloca su propio candado
- Solo la persona que colocó el candado puede retirarlo
- La tarjeta debe indicar: nombre, fecha, motivo del bloqueo
- Prohibido romper candados sin autorización del Gerente de Planta

## 4. Procedimiento de Trabajo en Caliente (Soldadura en Área de Proceso)

### 4.1 Requisitos Previos
1. Permiso de trabajo en caliente aprobado
2. Medición de gas en área: LEL < 10%, monitoreo continuo
3. Equipos contra incendio disponibles (extintor + manguera)
4. Vigía de fuego asignado (permanece durante trabajo + 30 min después)
5. Drenar, purgar e inertizar equipos a intervenir
6. Retirar materiales combustibles en radio de 15 metros
7. Cubrir con manta ignífuga drenajes y aberturas cercanas

### 4.2 Durante el Trabajo
- Monitor de gas en operación continua
- Comunicación con sala de control permanente
- Vigía de fuego con extintor listo
- Si LEL supera 10%: parar trabajo inmediatamente

### 4.3 Post-Trabajo
- Vigía permanece 30 minutos monitoreando
- Verificar que no haya puntos calientes con termómetro IR
- Cierre del permiso

## 5. Procedimiento de Respuesta ante Fuga de Gas H2S

### 5.1 Niveles de Alarma
| Nivel | Concentración | Acción |
|-------|--------------|--------|
| Alarma Baja | 10 ppm | Colocar equipo de respiración, investigar fuente |
| Alarma Alta | 20 ppm | Evacuar área inmediata, notificar sala de control |
| Alarma Muy Alta | 50 ppm | Evacuación general del área, activar sirena |

### 5.2 Acciones Inmediatas
1. Si detecta olor a H2S: colocarse equipo de respiración inmediatamente
2. Moverse en dirección contraria al viento
3. Notificar a sala de control: ubicación y nivel de alarma
4. No intentar reparar la fuente sin equipo SCBA (aire autónomo)
5. Asistir a personal inconsciente solo si tiene equipo de protección
