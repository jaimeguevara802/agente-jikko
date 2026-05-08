---
tags: [discovery, business-context, automation, FOL-001]
status: draft
date: "2026-05-05"
project: FOL-001
---

# Contexto y Expectativa: Automatización de Following (User Pilot)

## 📌 1. Visión General
Este proyecto nace como una oportunidad de **"Victoria Temprana" (Quick Win)** identificada a partir de las notas de campo (J-Commander). 
El objetivo principal es eliminar la carga operativa de extraer métricas y comentarios manualmente desde **User Pilot**, liberando tiempo del equipo para que se enfoque en análisis y toma de decisiones.

> **Principio Clave:** Todo reporte periódico que no requiera criterio humano para su extracción, debe ser automatizado.

---

## 🏗 2. Estado Actual (AS-IS)

Actualmente, el proceso de recopilación de insights semanales de "Following" se realiza de forma 100% manual.

- **Actividades manuales:**
  - Entrar a la plataforma de User Pilot.
  - Filtrar por el periodo de tiempo necesario (semanal).
  - Extraer las métricas clave definidas previamente en un documento de seguimiento.
  - Extraer comentarios de las encuestas y hallazgos clave.
  - Redactar los "próximos pasos" basados en la data obtenida.
- **Dolor principal:** Consume tiempo valioso (horas-hombre) en tareas mecánicas (copiar y pegar), retrasando el verdadero análisis de valor.

---

## 🚀 3. Estado Futuro Esperado (TO-BE)

La expectativa es construir un flujo automatizado (script, integración vía API o herramienta No-Code) que ejecute la extracción de datos mecánicos de User Pilot y prepare el terreno para el análisis humano.

### Caso de Uso Core: Extracción y consolidación automática de métricas semanales
- **Usuario:** Product Manager o Analista de Datos.
- **Situación:** Llegó el fin de semana o inicio de semana y se requiere el reporte de "Following" actualizado.
- **Decisión que necesita tomar:** ¿Qué métricas bajaron, subieron, y qué hallazgos arrojaron los usuarios en las encuestas para definir nuestros próximos pasos?
- **Datos necesarios:** Métricas definidas del periodo, comentarios en bruto de encuestas, eventos de uso.
- **Fuente de datos:** User Pilot (vía API o exportación automatizada).
- **Vista o herramienta esperada:** El documento o dashboard oficial pre-poblado con los datos del periodo, listo para que el PM solo redacte las conclusiones y "próximos pasos".
- **Métrica de éxito:** 
  - Horas operativas ahorradas a la semana.
  - Precisión de la data extraída.
  - Tiempo (Lead time) desde que termina el periodo hasta que el reporte está listo.

---

## 🎯 4. Resultados Esperados y Próximos Pasos

Para consolidar esta victoria temprana, debemos avanzar con los siguientes pasos de descubrimiento técnico:

1. **[Técnico] Investigar factibilidad:** Validar si User Pilot cuenta con una API abierta para exportar encuestas y métricas, o si admite webhooks.
2. **[Negocio] Definición de Formato Destino:** Confirmar dónde "aterrizarán" los datos automáticamente (¿un Google Sheet, Airtable, Slack, Notion?).
3. **[Prototipo] Prueba de Concepto (PoC):** Construir un pequeño script o integración (Zapier/Make/Python) que extraiga los datos de los últimos 7 días con éxito.
4. **[Presentación] Mostrar el Quick Win:** Socializar la automatización con el equipo para validar la reducción de carga de trabajo.
