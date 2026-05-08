---
tags: [discovery, business-context, supplier-intelligence, SUP-001, asis]
status: draft
date: "2026-05-05"
updated: "2026-05-06"
project: SUP-001
---

# Contexto y Expectativa: Supplier Intelligence en Dropi

## 📌 1. Visión General
El proyecto **Supplier Intelligence** para la célula de Supplier Success nace de la necesidad de estructurar la información dispersa de los proveedores. 
El objetivo **no es construir reportería por reportería ni un dashboard estático**, sino construir una **capacidad de análisis y decisión** pensada desde casos de uso reales. 

> **Principio Clave:** Si una métrica, vista o análisis no ayuda a tomar una decisión concreta o a ejecutar una acción, no debe estar en la primera versión.

### Stakeholders Clave Identificados:
- **Miguel Gutiérrez**: Ownership y manejo de data actual.
- **Laura Torres**: Contexto en avances de dashboards previos.

---

## 🏗 2. Casos de Uso Core (Estructura PM)

A continuación, se desglosan los casos de uso priorizados bajo el framework de decisión requerido:

---

## 📋 AS-IS — Estado actual del conocimiento del dominio supplier

> Fuente: conversación María (Directora de Producto) / Jaime (PM) — 2026-05-06
> Transcript Supabase: `2f2124b6-85a4-4a8a-bfce-c7c156ab9429`
> Draft Supabase: `90a4354c-7bf0-4e79-a570-6cb4b7d49dfd`

### Marco conceptual: las dos dimensiones del proveedor

María establece dos ejes como punto de partida del trabajo de la célula:

**Dimensión 1 — Proveedor como usuario:** SLAs, activación, fricción en el flujo.
**Dimensión 2 — Proveedor como aliado estratégico:** catálogo, variedad, stock disponible.

Vínculo con OKRs: *"si queremos llegar a 7.8M de órdenes mensuales, al menos en la plataforma debería tener 9M de unidades de productos."* El catálogo es el piso del crecimiento.

### Problema central: nadie sabe qué es un "proveedor activado"

No existe definición acordada. Dos versiones en tensión:

| Visión | Definición | Lógica |
|---|---|---|
| **Negocio (Dropi gana)** | Primera orden movilizada (transportadora la recoge) | Dropi gana independientemente de si se entrega |
| **Producto (usuario ve valor)** | Primera orden entregada exitosamente | El proveedor recibe su ganancia y entiende el valor |

Dato de cohortes de **dropshippers** (no existe equivalente para proveedores):
- Sin primera orden exitosa → **35% probabilidad de retención**
- Con primera orden exitosa → **80% mayor probabilidad de retención**

> *"Proveedores es el menos explorado de todos."*

### Riesgo de doble pérdida del proveedor en devoluciones

El proveedor (a diferencia del dropshipper) puede perder el producto dañado en devoluciones:
- Estimado: 20% de devoluciones → ~40% llegan dañados = **~10% de pérdida neta sobre productos enviados**
- Consecuencia en cadena: absorbe pérdida → sube costo al dropshipper → sube precio al consumidor → pierde competitividad vs Temu

### Vacíos críticos de datos

- Cuántos proveedores se activan → **no se sabe**
- Qué define activación del proveedor → **sin definir**
- Si proveedores con primera venta fallida abandonan → **no se sabe**
- % real de productos dañados en devoluciones → **no calculado**
- Análisis de cohortes de proveedores → **no existe**

### Contexto organizacional
- Células recién conformadas. Proyecto de supply: **heredado de Juan Diego**, a formalizar.
- Un solo proyecto asignado a la célula desde junta directiva (aprobado con todos los directores).
- La célula debe: entregar el proyecto **y** proponer cómo impactar los OKRs.

### Primer entregable recomendado por María
Tablero base de la célula para alinear definiciones internamente antes de escalar.

---

## 🏗 2. Casos de Uso Core (Estructura PM)

A continuación, se desglosan los casos de uso priorizados bajo el framework de decisión requerido:

### Caso de Uso 1: Identificar suppliers registrados que no se han activado
- **Usuario:** Líder de Supplier Success, Product Manager, analista o equipo operativo.
- **Situación:** Existen suppliers que completan el registro pero no llegan a su primera venta. Se desconoce dónde están bloqueados.
- **Decisión que necesita tomar:** ¿A qué suppliers debemos intervenir manualmente hoy y a cuáles a través de campañas masivas?
- **Preguntas de negocio:** ¿Cuántos no han vendido? ¿Hace cuánto se registraron? ¿Completaron su perfil? ¿Tienen productos visibles/aprobados? ¿Han tenido interés de dropshippers?
- **Datos necesarios:** Fecha de registro, status del perfil, count de productos (cargados/aprobados/visibles), métricas de interacción previas a la venta.
- **Fuente de datos:** Data transaccional de registro y catálogo.
- **Vista o herramienta esperada:** Lista/Tabla accionable y filtrable de suppliers bloqueados en fase de activación, ordenada por potencial.
- **Acción resultante:** Contactar suppliers bloqueados, lanzar campañas de activación, escalar problemas recurrentes a Producto.
- **Métrica de éxito:** Aumento en el % de conversión (Registro -> Primera Venta), Reducción del Lead Time a primera venta.

### Caso de Uso 2: Detectar puntos de fuga en el funnel de activación
- **Usuario:** Product Manager, Supplier Success Manager o equipo de estrategia.
- **Situación:** Se pierde esfuerzo al no saber en qué etapa exacta del funnel de activación (Registro -> Venta recurrente) se caen los suppliers.
- **Decisión que necesita tomar:** ¿Qué etapa del proceso o feature del producto debemos intervenir o mejorar este sprint?
- **Preguntas de negocio:** ¿Dónde ocurre la mayor pérdida? ¿Cuál es el tiempo promedio entre etapas? ¿Qué categorías se activan más rápido?
- **Datos necesarios:** Timestamps precisos por cada etapa del funnel (Registro, Perfil, Carga, Aprobación, Visibilidad, 1ra Venta).
- **Fuente de datos:** Logs de eventos de usuario, base de datos de productos.
- **Vista o herramienta esperada:** Gráfico de Funnel con tasas de conversión entre pasos y tiempos promedio (Drop-off analysis).
- **Acción resultante:** Priorizar mejoras de producto UX, automatizar recordatorios, crear playbooks por etapa.
- **Métrica de éxito:** Incremento de conversión *Step-by-Step* en el funnel, disminución del *Time-in-Stage*.

### Caso de Uso 3: Priorizar suppliers para gestión o acompañamiento
- **Usuario:** Equipo de Supplier Success.
- **Situación:** Capacidad operativa limitada. No todos los suppliers justifican el mismo nivel de esfuerzo manual.
- **Decisión que necesita tomar:** ¿En qué suppliers invierto mi tiempo humano hoy y cuáles dejo en flujos automatizados?
- **Preguntas de negocio:** ¿Cuáles tienen mayor potencial? ¿Cuáles están cerca de activarse? ¿Cuáles tienen productos atractivos pero 0 ventas?
- **Datos necesarios:** GMV histórico/potencial, atractividad del producto (visitas de dropshippers), nivel de completitud.
- **Fuente de datos:** Scoring de proveedores (por definir), data transaccional.
- **Vista o herramienta esperada:** Matriz de Priorización (Potencial vs. Esfuerzo) o ranking dinámico de suppliers.
- **Acción resultante:** Crear listas enfocadas de gestión humana vs. automatizada.
- **Métrica de éxito:** ROI del equipo de Success (GMV generado por hora de gestión manual).

### Caso de Uso 4: Identificar oportunidades para aumentar valor sin afectar al dropshipper
- **Usuario:** Supplier Success, Comercial, Producto o Growth.
- **Situación:** Necesidad de crecer el GMV/Ticket promedio mediante estrategias sostenibles (combos, volumen) sin inflar precios artificialmente.
- **Decisión que necesita tomar:** ¿Qué productos agrupo en combos y a qué suppliers les propongo modelos de descuento por volumen?
- **Preguntas de negocio:** ¿Qué productos tienen alta rotación? ¿Qué suppliers tienen buena satisfacción pero bajo ticket?
- **Datos necesarios:** Ticket promedio por supplier, rotación de inventario, cruce de productos comprados juntos (Market Basket Analysis).
- **Fuente de datos:** Órdenes de compra, catálogo, analítica de carritos.
- **Vista o herramienta esperada:** Motor de recomendaciones o reporte de afinidad de productos/categorías.
- **Acción resultante:** Proponer combos, negociar volumen, optimizar el catálogo de los mejores suppliers.
- **Métrica de éxito:** Incremento del Ticket Promedio (AOV) y Unidades por Orden (UPT).

### Caso de Uso 5: Detectar suppliers que crecen pero afectan la salud del ecosistema
- **Usuario:** Supplier Success Manager, Operaciones, Calidad o Producto.
- **Situación:** Suppliers con alto volumen de ventas están generando fricción (cancelaciones, reclamos) dañando la confianza del Dropshipper.
- **Decisión que necesita tomar:** ¿Qué suppliers penalizo, pauso o meto a un plan de remediación urgente?
- **Preguntas de negocio:** ¿Qué suppliers venden mucho pero tienen alto % de reclamos? ¿Qué productos tienen problemas recurrentes?
- **Datos necesarios:** Tasa de cancelación, volumen de tickets de soporte, tiempos de despacho, GMV.
- **Fuente de datos:** Zendesk/Soporte, módulo de devoluciones/cancelaciones, logística.
- **Vista o herramienta esperada:** Dashboard de "Risk & Health" con alertas automáticas (semáforos).
- **Acción resultante:** Intervenir problemáticos, pausar productos, escalar a operaciones.
- **Métrica de éxito:** Disminución en la Tasa de Reclamos/Cancelaciones, aumento del NPS/CSAT del Dropshipper.

---

## 🎯 3. Resultados Esperados y Próximos Pasos (Roadmap AS-IS)

Antes de construir el dashboard definitivo, el entregable inicial debe ser un **Diagnóstico Estructurado** que responda:

1. ¿Qué casos de uso (de los 5) son prioritarios?
2. ¿Qué datos existen hoy y cuáles faltan? (Gap Analysis).
3. Reuniones de contexto con **Miguel Gutiérrez** y **Laura Torres** para validar tableros/datos existentes.
4. Definición de Quick Wins para generar impacto temprano.
5. Diseño del Roadmap de la capacidad de Supplier Intelligence.
