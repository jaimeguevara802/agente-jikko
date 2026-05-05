---
name: obsidian-decision-extractor
description: Escanea minutas e hilos para extraer decisiones clave y formalizarlas en la carpeta 05_Decisions.
---

# Decision Extractor

## Objetivo
Identificar acuerdos informales o menciones de decisiones en las notas de reuniones y convertirlas en ADRs o Logs de Decisiones (Decision Logs).

## Instrucciones
1. Escanea archivos recientes en `04_Meetings`.
2. Busca la sección "Decisiones Tomadas".
3. Por cada decisión significativa detectada, usa la plantilla `tpl_decision_log.md`.
4. Crea un nuevo archivo en `05_Decisions/`.
5. Asegúrate de que el archivo cite (usando `[[ ]]`) la reunión de origen para trazabilidad.
