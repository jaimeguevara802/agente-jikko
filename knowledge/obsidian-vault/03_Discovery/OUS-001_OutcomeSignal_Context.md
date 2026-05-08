---
tags: [discovery, asis, project]
project_code: OUS-001
project: Outcome Signal
status: draft
date: "2026-05-06"
version: v0.2
---

# OUS-001: Outcome Signal — Discovery AS-IS

## 1. Propósito de este documento

Documentar el estado actual del proceso de medición de efectividad de features en Dropi, como insumo para diseñar un módulo (Outcome Signal) que automatice, estandarice y escale dicho proceso.

La fuente principal de esta versión es la reunión entre Michelle Lopez Obregon y Jaime Guevara del 2026-05-06 (33 min, Fathom).
Transcript Supabase ID: `d9c917a0-4909-4bdf-aa02-f8e598e7f06b`

---

## 2. Contexto de negocio

### 2.1 Qué es Dropi y quiénes son los usuarios
Dropi es una plataforma de dropshipping que conecta **dropshippers** (vendedores) con **proveedores** de producto. El cliente final es el comprador del dropshipper.

Los proyectos que se miden son funcionalidades nuevas lanzadas en la plataforma. Los usuarios afectados son principalmente dropshippers, aunque algunos proyectos también impactan a proveedores.

### 2.2 Por qué se mide
El equipo de producto necesita saber si lo que implementó generó el resultado esperado: mayor adopción, menor fricción, reducción de devoluciones, u otros KPIs de negocio. Sin esta medición, no hay forma objetiva de decidir si hay que ajustar, escalar o descartar una funcionalidad.

### 2.3 Proyectos actualmente en medición activa
| Proyecto | Descripción breve | Métrica de negocio objetivo |
|---|---|---|
| **Huella Digital** | Permite al dropshipper ver el historial del cliente final (compras, devoluciones, probabilidad de entrega) a través del número de teléfono | Reducción de devoluciones |
| **Garantías** | Segundo proyecto activo — detalles a complementar en próximas sesiones | Por definir |

### 2.4 Alcance del sistema de medición
El proceso aplica a **todos los proyectos que involucren dropshippers y/o proveedores**. Actualmente no existe un criterio explícito de exclusión. Michelle lo expresó así:

> *"Cualquier proyecto podría entrar aquí en este sistema de análisis. En realidad, todos deberían entrar."*

---

## 3. Actores y roles

| Actor | Rol en el proceso | Cuándo interviene |
|---|---|---|
| **Michelle Lopez Obregon** | PM responsable — define métricas, redacta documentos, hace el análisis recurrente, presenta resultados | Todo el proceso |
| **Laura Torres** | Admin de UserPilot — configura los eventos de tracking y construye los dashboards en la herramienta | Fase de setup técnico, antes del lanzamiento |
| **Cata (Catalina)** | PM — también realiza mediciones de otros proyectos. Tiene experiencia usando Claude para visualización | Proceso paralelo, potencial colaboración |
| **Diana Aldana** | Vigila las métricas a nivel portafolio y da feedback al equipo de PM | Revisión y validación |
| **Marketing** | Recibe insumos del lanzamiento (descripción, video, materiales de comunicación) | Fase de lanzamiento |
| **Equipo de desarrollo** | Implementa la funcionalidad y los eventos técnicos que UserPilot necesita para trackear | Prerequisito del proceso |

---

## 4. Herramientas actuales

### 4.1 UserPilot — Herramienta principal de tracking
UserPilot es la fuente de verdad de comportamiento de usuario en producto.

**Qué puede hacer:**
- Mostrar usuarios activos (DAU, WAU, MAU) con filtros por segmento de usuario (ej. Dropshippers Colombia)
- Trackear eventos de clic en botones específicos configurados por Laura Torres
- Construir funnels para medir conversión paso a paso dentro de una funcionalidad
- Lanzar encuestas in-app a los usuarios (escala 1-5 con campo de texto abierto)
- Mostrar dashboards de proyectos individuales (ej. Dashboard Huella Digital, Dashboard Garantías)

**Limitaciones conocidas:**
- Los filtros de fecha hay que configurarlos manualmente cada vez que se consulta (no hay vistas guardadas con rango dinámico)
- No se sabe si tiene API accesible para extracción de datos programática
- El scope actual está limitado a Colombia — no está claro si hay datos de otros países
- La configuración de nuevos eventos requiere intervención de Laura Torres (cuello de botella)

### 4.2 FigJam — Herramienta de reporte
Se usa para construir las tablas de seguimiento y pegar evidencia de screenshots. No es una herramienta de análisis — es el "cuaderno" donde se documenta el resultado.

**Limitaciones:**
- Pegar tablas desde Claude o Excel en FigJam es complicado; las tablas copiadas van a una sola celda
- No tiene capacidad de graficar ni visualizar tendencias
- El formato no es fácil de leer para personas externas al proceso

### 4.3 IA asistente — Gemini (en proceso de migración a Claude)
Michelle usa una "Gema" (Gem de Google Gemini) configurada con el prompt completo del proceso de medición. Sirve como asistente de análisis: Michelle le pasa los datos (a veces screenshots) y la IA genera las tablas y el texto del análisis.

Está migrando a Claude porque Gemini está generando malos resultados y la experiencia es frustrante. Cata ya exploró Claude para visualización con resultados prometedores.

---

## 5. Proceso AS-IS — Paso a paso detallado

### Fase 0 — Prerequisito: Feature implementada y en producción
El proceso de medición **no puede empezar antes** de que la funcionalidad esté en desarrollo. Los eventos de tracking en UserPilot dependen de que el código esté implementado, porque los botones o interacciones que se quieren medir deben existir en el producto.

> *"Para que Laura Torres pueda hacer los eventos para poder medir la cantidad de clics en cada uno de los botones que necesitamos, pues eso ya debe estar implementado, ya debe estar en desarrollo."*

### Fase 1 — Historia de Lanzamiento
**Quién:** Michelle (redacta), Laura Torres y Marketing (destinatarios)

**Qué es:** Un documento/historia de usuario que actúa como brief de lanzamiento. Contiene:

| Campo | Descripción |
|---|---|
| Descripción del proyecto | Qué se hizo y qué problema resuelve |
| Objetivo | Qué buscamos lograr con esta funcionalidad |
| Propuesta de valor | Qué esperamos que el usuario logre |
| Usuarios impactados | Segmento(s) de usuario afectados |
| Países | En qué mercados aplica |
| Fecha beta | Cuándo sale la versión limitada |
| Fecha de lanzamiento | Cuándo sale al público general |
| Link Figma | Diseño de referencia |
| Link Tango | Explicación paso a paso del flujo |
| Video demo | Cómo funciona la funcionalidad |

**Para Laura Torres:** le sirve para entender qué eventos debe configurar en UserPilot.
**Para Marketing:** le sirve para preparar la comunicación del lanzamiento.

### Fase 2 — Documento de Métricas
**Quién:** Michelle (redacta)

**Qué es:** Un documento formal que define exactamente qué se medirá y cómo se evaluará el éxito. Se adjunta a la Historia de Lanzamiento. Contiene:

#### Sección A — Contexto
- Contexto del problema
- Objetivo del proyecto
- Propuesta de valor
- Alcance de la medición

#### Sección B — Métricas de Negocio
Por cada métrica de negocio se define:
- **Qué medir** (ej. tasa de devoluciones)
- **Por qué medirlo** (vínculo con el objetivo del proyecto)
- **Fórmula de cálculo** (ej. devoluciones / total órdenes enviadas)
- **Criterio de éxito** (ej. reducción del X% en 3 meses)
- **Segmentación técnica** (qué subconjunto de usuarios aplica)

#### Sección C — Métricas de Comportamiento / UX (Framework HEART)
Se usa el framework HEART de Google. Por cada dimensión se define la misma estructura (qué, por qué, fórmula, criterio de éxito, segmentación):

| Dimensión | Definición | Cómo se mide en UserPilot |
|---|---|---|
| **H — Happiness** | Satisfacción percibida del usuario con la funcionalidad | Encuesta in-app: "¿Qué tan útil te parece esta información?" (1-5). Si califica 1-2, se abre campo de texto libre para comentarios. Segunda encuesta: "¿Qué tan claro fue?" (1-5), igual con campo abierto si nota baja. |
| **E — Engagement** | Frecuencia y cantidad de uso de la funcionalidad | Conteo de clics en botones, número de sesiones con interacción con la feature |
| **A — Adoption** | Qué porcentaje de los usuarios objetivo descubrió y usó la funcionalidad al menos una vez | % de dropshippers activos que abrieron Huella Digital al menos 1 vez en el período |
| **R — Retention** | Si los usuarios que adoptaron volvieron a usar la funcionalidad | % de usuarios que la usaron en semana 1 y también en semana 2, 3, etc. |
| **T — Task Success** | Si el usuario pudo completar el flujo completo sin abandonar | % de usuarios que completaron el funnel de principio a fin vs. los que se salieron en algún paso intermedio |

#### Sección D — Metodología de Validación
Cómo se recolecta la data cualitativa: encuestas in-app configuradas en UserPilot con las preguntas de satisfacción y claridad.

#### Sección E — Esquema de Seguimiento
Define la cadencia de análisis (ver Sección 7).

### Fase 3 — Historia de Dashboard para Laura Torres
**Quién:** Michelle (redacta el pedido), Laura Torres (lo ejecuta en UserPilot)

**Qué es:** Una segunda historia específica para que Laura Torres construya el dashboard de seguimiento en UserPilot. Michelle le especifica exactamente qué elementos deben aparecer y en qué orden:
- Qué funnels incluir
- Qué eventos de clic mostrar (por botón)
- Qué métricas de usuarios activos mostrar
- Cómo segmentar

Laura Torres va a UserPilot, configura los eventos (asocia un nombre de evento al botón o interacción en el producto) y construye el dashboard con los gráficos y tablas especificadas.

**Cuello de botella:** Michelle no sabe exactamente cómo Laura configura los eventos — hay dependencia total de Laura Torres para que los datos estén disponibles en UserPilot.

### Fase 4 — Ciclo recurrente de Análisis (proceso más crítico y costoso)

Esta fase se repite según la cadencia definida (ver Sección 7).

**Paso 4.1 — Entrar a UserPilot y capturar datos**
- Michelle entra al dashboard del proyecto en UserPilot
- Configura manualmente el filtro de fechas (ej. "últimos 7 días" para medir la semana)
- Revisa cada sección del dashboard: funnels, clics por botón, usuarios activos, encuestas
- **Captura screenshots de cada sección** como evidencia

**Paso 4.2 — Trasladar datos a FigJam**
- Abre FigJam (herramienta de tablero colaborativo)
- Pega los screenshots como evidencia visual
- Extrae manualmente los números de los screenshots

**Paso 4.3 — Análisis con IA asistente**
- Pasa los datos (números, screenshots) a Gemini (Gem configurado) o Claude
- La IA genera:
  - Análisis descriptivo de cada métrica
  - Comparación con el período anterior
  - Identificación de variaciones importantes
  - Hipótesis explicativas

**Paso 4.4 — Construcción de entregables en FigJam**
Se generan dos entregables distintos:

**Entregable A — Análisis semanal detallado:**
Tabla completa con cada métrica definida en el Doc de Métricas, con:
- Valor actual del período
- Comparación vs. período anterior
- Análisis textual de qué pasó y por qué
- Hallazgos, dolores y fricciones detectados
- Bugs o problemas técnicos identificados (requiere validación manual)
- Próximos pasos recomendados

**Entregable B — Bitácora de seguimiento (comparativa):**
Tabla resumida donde:
- Cada columna es una métrica
- Cada fila es un período de medición (S1, S2, S3, S4, Q1, Q2, M3...)
- Permite comparar la evolución de cada métrica en el tiempo de un vistazo

> *"Esto es como, o sea, no es tan fácil de leer, sería más fácil si tuviésemos como una gráfica o algo así, más fácil de entender a simple vista."*

---

## 6. Caso en profundidad: Huella Digital

### ¿Qué es Huella Digital?
Funcionalidad que permite al dropshipper consultar el historial completo del cliente final a través de su número de teléfono. Dropi tiene registros de comportamiento de compradores en múltiples tiendas y transportadoras, y clasifica al cliente en tres categorías:

- **Entrega probable**: historial positivo, bajo riesgo
- **Entrega incierta**: historial mixto, requiere atención
- *(tercera categoría no confirmada en la transcripción)*

El dropshipper puede ver cuántas compras ha hecho, en qué tiendas, qué transportadoras se usaron, si ha tenido devoluciones. Con esa información decide si enviar o no el pedido.

### Puntos de entrada a Huella Digital
La funcionalidad se puede abrir desde tres lugares distintos en la plataforma:
1. **Botón flotante** (disponible siempre en pantalla)
2. **Creación de la orden**
3. **Edición de la orden**

### Hallazgos actuales de uso
| Punto de entrada | Nivel de uso |
|---|---|
| Botón flotante | ALTO — el más utilizado |
| Botón en creación de orden | BAJO — casi no se usa |
| Botón en edición de orden | BAJO — casi no se usa |

### Hipótesis del equipo
La fricción de los botones en creación/edición se explica por el modelo de negocio de los dropshippers:

> *"La mayoría de los pedidos que tienen los dropshippers son por integraciones. Entonces, es muy tedioso para ellos estar yendo a cada uno de los pedidos, abrir el botón de huella para verificar la información del cliente."*

Es decir: los dropshippers que operan por integración reciben pedidos de forma automática en masa — revisar la huella de cada cliente pedido por pedido genera una fricción inaceptable.

### Próximo paso hipotético
Si la hipótesis se confirma, la solución podría ser:
> *"Una funcionalidad para que te alerte todos los pedidos que vienen con una probabilidad riesgosa, para que no tengas que abrir la huella pedido por pedido."*

### Métrica de negocio esperada
El objetivo de negocio es **reducir las tasa de devoluciones**. Si el dropshipper consulta la huella y cancela pedidos riesgosos, las devoluciones deberían bajar. Sin embargo, aún no hay evidencia confirmada de que esto esté ocurriendo — la adopción baja limita la capacidad de medir el impacto.

---

## 7. Cadencia de medición

| Período | Frecuencia de análisis | Contexto |
|---|---|---|
| Mes 1 (semanas 1-4) | Semanal (3-4 análisis) | Fase de lanzamiento temprana, alta variabilidad |
| Mes 2 | Quincenal (2 análisis) | Estabilización |
| Mes 3 en adelante | Mensual | Seguimiento de largo plazo |

**Nota importante:** Las métricas en UserPilot quedan disponibles siempre. Lo que ocurre en cada período de medición **no es la recolección de datos** (eso es automático), sino el **análisis** de esos datos y la construcción de los entregables.

---

## 8. Dolores y fricciones actuales

### 8.1 Costo de tiempo inaceptable
- **Tiempo esperado:** 1 hora por proyecto → 2 horas para 2 proyectos
- **Tiempo real medido:** 5 horas de trabajo + 3 horas adicionales de pulido = **8 horas totales**
- **Resultado final:** Michelle no quedó satisfecha con el resultado después de 8 horas

> *"Yo en realidad esto lo hice el sábado y literal puse el cronómetro para darme cuenta cuánto me demoré y me demoré cinco horas."*

### 8.2 Proceso completamente manual y fragmentado
Cada ciclo de análisis requiere:
1. Entrar a UserPilot manualmente
2. Configurar filtros de fecha a mano
3. Capturar screenshots uno a uno
4. Abrir FigJam y pegar screenshots
5. Extraer números manualmente de las imágenes
6. Pasar datos a la IA por pantalla
7. Copiar el output de la IA a FigJam
8. Formatear las tablas en FigJam (el copy-paste de tablas falla)

No hay ningún paso automatizado ni integración entre las herramientas.

### 8.3 Sin baseline capturado al lanzamiento
No existe un mecanismo para tomar un snapshot del estado de las métricas **en el momento exacto del lanzamiento**. Cuando se quiere comparar el antes y el después, se reconstruye retroactivamente — lo que introduce error y pérdida de contexto.

### 8.4 Visualización pobre y difícil de compartir
Los entregables actuales son tablas de texto en FigJam. No hay gráficas de tendencia, no hay colores semafóricos, no hay comparaciones visuales fáciles de leer. Para que un stakeholder entienda el estado de un proyecto tiene que leer toda la tabla.

> *"Sería más fácil si tuviésemos como una gráfica o algo así, más fácil de entender a simple vista, porque si ves que se lo compartamos a los demás implicados, que todos estamos enterados de lo que está pasando."*

Cata (otra PM) ya experimentó con Claude para generar visualizaciones comparativas por semana y los resultados fueron notablemente mejores.

### 8.5 Conocimiento concentrado en una persona
Michelle es la única que entiende y ejecuta todo el proceso end-to-end. No existe documentación del proceso que permita a otra persona replicarlo o continuar un análisis si Michelle no está disponible.

### 8.6 Dependencia técnica de Laura Torres
Cualquier nuevo proyecto que quiera entrar al sistema de medición necesita que Laura Torres configure los eventos en UserPilot. No hay proceso de self-service ni documentación técnica estándar para este paso.

### 8.7 Asistente de IA inestable (Gemini)
La Gema de Gemini da resultados inconsistentes y Michelle expresa abiertamente su frustración con la herramienta. La migración a Claude es una decisión ya tomada pero no completada.

---

## 9. Supuestos y vacíos de información

| Supuesto / Vacío | Impacto | Estado |
|---|---|---|
| UserPilot no tiene API accesible para extracción programática | Si hay API, podemos automatizar la ingesta de datos. Si no, el proceso manual es obligatorio. | Sin confirmar |
| Laura Torres es cuello de botella permanente para nuevos eventos | Bloquea la escalabilidad — cada nuevo proyecto necesita su intervención | Sin alternativa explorada |
| Los criterios de éxito se definen después del lanzamiento | Si no hay criterio previo, no hay forma objetiva de evaluar el outcome | Confirmado como dolor |
| Las encuestas de UserPilot son la única fuente cualitativa | No se exploró si hay otras fuentes (Intercom, entrevistas sistematizadas, soporte) | Sin confirmar |
| El proceso de Cata es equivalente al de Michelle | Puede haber variaciones relevantes que enriquezcan el AS-IS | Pendiente de explorar |
| Diana Aldana define métricas o solo valida | Define el alcance de su influencia en el proceso | Sin confirmar |

---

## 10. Expectativas preliminares (TO-BE)

> Estas expectativas son preliminares, basadas en una sola sesión. No son definitivas hasta validarse con más stakeholders.

- **Registro de proyecto antes del lanzamiento:** poder crear un "proyecto de medición" con sus criterios de éxito definidos explícitamente antes de salir a producción
- **Baseline automático:** capturar el estado de las métricas en el momento del lanzamiento sin intervención manual
- **Extracción automática de datos:** conectar con UserPilot (vía API u otro mecanismo) para traer los datos de cada período sin screenshots
- **Análisis asistido por IA:** generar el análisis descriptivo y comparativo de forma automatizada
- **Visualización clara y compartible:** gráficas de tendencia, semáforos, comparativas semanales — consumibles por cualquier stakeholder sin necesidad de entrenamiento
- **Bitácora centralizada:** un solo lugar donde todos los implicados de un proyecto puedan ver el estado actualizado de las métricas
- **Outcome claro por proyecto:** un juicio evaluado automáticamente → **efectivo / parcial / nulo**
- **Escalable a cualquier proyecto:** no solo Huella Digital o Garantías — cualquier feature con dropshippers/proveedores

---

## 11. Preguntas abiertas para próximas sesiones

### Técnicas
- [ ] ¿UserPilot tiene API? ¿Qué endpoints expone? ¿Quién tiene acceso?
- [ ] ¿Los eventos de UserPilot los puede configurar alguien más además de Laura Torres?
- [ ] ¿Hay datos de encuestas exportables en raw (no solo como screenshot)?

### De proceso
- [ ] ¿Cuál es el proceso exacto de Cata? ¿Difiere del de Michelle?
- [ ] ¿Qué define Diana Aldana? ¿Ella establece los criterios de éxito o solo valida los que definió el PM?
- [ ] ¿Existe algún documento donde estén definidas las métricas de todos los proyectos activos?

### De criterios
- [ ] ¿Cuándo se define el criterio de éxito? ¿Antes o después del lanzamiento?
- [ ] ¿Hay un umbral mínimo de adopción aceptable definido por la empresa (ej. 30% en 30 días)?
- [ ] ¿Qué pasa cuando un proyecto no alcanza el criterio de éxito? ¿Hay un proceso de decisión?

### De alcance del sistema futuro
- [ ] ¿El sistema debe generar alertas automáticas cuando una métrica cae por debajo del umbral?
- [ ] ¿Debe incluir soporte para métricas de negocio que no vienen de UserPilot (ej. devoluciones de ERP)?
- [ ] ¿El output final debe ser exportable a un formato específico (PDF, Notion, Slack)?

---

## 12. Registro de transcripciones

| Fecha | Participantes | Duración | ID Supabase | Temas cubiertos |
|---|---|---|---|---|
| 2026-05-06 | Michelle Lopez Obregon, Jaime Guevara | 33 min | `d9c917a0-4909-4bdf-aa02-f8e598e7f06b` | AS-IS completo del proceso de medición, caso Huella Digital, stakeholders, herramientas, dolores, expectativas |

---

## 13. Historial de versiones

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| v0.1 | 2026-05-06 | Documento inicial creado | Sistema |
| v0.2 | 2026-05-06 | AS-IS expandido con detalle completo desde transcripción Michelle/Jaime | Sistema |
