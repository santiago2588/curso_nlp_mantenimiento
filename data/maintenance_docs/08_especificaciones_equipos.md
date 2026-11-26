# Especificaciones Técnicas de Equipos Principales

## 1. Bombas Centrífugas

### P-101A/B — Bomba de Transferencia de Crudo
- **Fabricante:** Sulzer, Modelo MSD-D 8x10-13
- **Tipo:** Centrífuga horizontal, entre cojinetes, API 610 BB2
- **Fluido:** Crudo (API 28-32°, viscosidad 5-15 cP a T operación)
- **Caudal diseño:** 450 m³/h
- **Cabeza diferencial:** 180 m
- **NPSH requerido:** 3.5 m
- **Velocidad:** 3,560 RPM
- **Motor:** 500 HP, 4,160V, 3Φ, 60 Hz
- **Sello mecánico:** John Crane 5610, plan API 53B
- **Rodamientos:** DE: 6316 C3, NDE: NU316, empuje: 7316B
- **Lubricación:** Aceite ISO VG 68 (nivel constante)
- **Material carcasa:** A216 WCB
- **Material impeller:** A743 CA6NM (13Cr-4Ni)
- **Peso total:** 3,200 kg

### P-201 — Bomba de Inyección de Agua
- **Fabricante:** Flowserve, Modelo WIK 6x8-15
- **Tipo:** Centrífuga horizontal multi-etapa, API 610 BB5
- **Fluido:** Agua tratada para inyección (TDS < 50,000 ppm)
- **Caudal diseño:** 280 m³/h
- **Presión descarga:** 2,500 psi
- **Velocidad:** 3,560 RPM
- **Motor:** 1,500 HP, 4,160V
- **Sello mecánico:** Eagle Burgmann M7N, plan API 54
- **Material:** Duplex 2205 (alta resistencia a corrosión por cloruros)

## 2. Compresores Centrífugos

### C-101 — Compresor de Gas de Exportación
- **Fabricante:** Siemens, Modelo STC-SV
- **Tipo:** Centrífugo, 3 etapas con enfriamiento inter-etapa
- **Gas:** Gas natural (MW ~20, con 50-200 ppm H2S)
- **Flujo:** 15 MMSCFD
- **Presión succión:** 5-8 bar
- **Presión descarga:** 45-55 bar
- **Temperatura descarga máxima:** 180°C
- **Velocidad:** 9,500 RPM
- **Potencia absorbida:** 4,200 kW
- **Accionamiento:** Turbina de gas (Solar Centaur 50)
- **Cojinetes:** Tipo tilting pad (radiales), Kingsbury (empuje)
- **Sistema de aceite:** ISO VG 46, 2 bombas (principal + respaldo)
- **Sistema anti-surge:** Compressor Controls Corporation (CCC)

### C-102 — Compresor de Gas Lift
- **Fabricante:** Dresser-Rand, Modelo DATUM
- **Tipo:** Centrífugo, 2 etapas
- **Gas:** Gas natural seco
- **Flujo:** 8 MMSCFD
- **Presión succión:** 10-15 bar
- **Presión descarga:** 80-100 bar
- **Velocidad:** 11,200 RPM
- **Accionamiento:** Motor eléctrico 3,000 HP con VDF

## 3. Separadores

### V-101 — Separador Trifásico de Producción
- **Fabricante:** Exterran
- **Tipo:** Horizontal trifásico con platos coalescedores
- **Diámetro:** 3.0 m (10 ft)
- **Longitud T-T:** 9.0 m (30 ft)
- **Presión diseño:** 300 psi
- **Temperatura diseño:** 100°C
- **Material:** SA-516 Gr.70, espesor pared 19mm
- **Capacidad líquido:** 5,000 BPD crudo + 8,000 BPD agua
- **Capacidad gas:** 20 MMSCFD
- **Instrumentación:** 
  - Nivel de crudo: LT-1504 (radar guiado)
  - Nivel de interface: LT-1505 (flotador magnético)
  - Presión: PT-1501 (Rosemount 3051)
  - Temperatura: TT-1501

## 4. Intercambiadores de Calor

### E-101 — Intercambiador Crudo/Crudo
- **Tipo:** Carcasa y tubos, TEMA AES
- **Servicio:** 
  - Lado carcasa: crudo caliente (de separador)
  - Lado tubos: crudo frío (a tanques)
- **Área de transferencia:** 85 m²
- **Presión diseño:** 200 psi (ambos lados)
- **Material tubos:** Acero al carbono (A179)
- **Material carcasa:** A516 Gr.70
- **Duty:** 2.5 MMBtu/hr

### E-102 — Enfriador de Gas Comprimido
- **Tipo:** Aero-enfriador (air-cooled)
- **Servicio:** Gas de descarga del compresor C-101
- **Número de bahías:** 2
- **Ventiladores:** 4 (2 por bahía), motor 25 HP cada uno
- **Temperatura entrada gas:** 150°C
- **Temperatura salida gas:** 45°C (diseño)
- **Presión diseño:** 75 bar

## 5. Tanques de Almacenamiento

### TK-101, TK-102 — Tanques de Crudo
- **Tipo:** Cilíndrico vertical, techo flotante interno
- **Capacidad:** 20,000 barriles cada uno
- **Diámetro:** 15 m
- **Altura:** 12 m
- **Material fondo:** A36, 8mm espesor
- **Material pared:** A36, variable (10mm base, 6mm tope)
- **Norma:** API 650
- **Sistema contra-incendio:** Espuma por cámaras, anillo de enfriamiento
