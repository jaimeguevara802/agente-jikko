---
description: Analiza seguimientos del proyecto, genera borradores y guarda solo con aprobación explícita
---

# Workflow: Project Followup

## Objetivo
Permitir que el usuario trabaje conversacionalmente sobre seguimientos, transcripciones e insights del proyecto, comparando siempre contra el contexto canónico aprobado.

## Proyecto principal
[Nombre del Proyecto]

## Fuentes canónicas obligatorias
Antes de analizar cualquier seguimiento, leer:

1. `canon/business_context.md`
2. `canon/project_context.md` (si existe)
3. `canon/asis.md` (si existe)
4. `canon/tobe.md` (si existe)
5. `canon/capabilities.md` (si existe)
6. `canon/user_stories.md` (si existe)

## Reglas

### Modo análisis
Si el usuario dice:
- analiza
- revisa
- dame borrador
- no guardes todavía
- qué ves
- qué riesgos hay

Entonces:
- NO escribir en Airtable.
- NO modificar archivos canónicos.
- Entregar solo un borrador estructurado.

### Modo aprobación oficial
Si el usuario dice explícitamente:
- aprueba este seguimiento
- guarda como seguimiento oficial
- registra los riesgos y decisiones
- esto queda aprobado

Entonces:
- pedir confirmación final antes de ejecutar scripts.
- guardar seguimiento en `Followups`.
- guardar riesgos en `Risks`.
- guardar decisiones en `Decisions`.
- guardar compromisos o hitos en `Milestones` si aplica.
- nunca actualizar AS-IS, TO-BE, Capabilities o User Stories sin aprobación explícita adicional.

## Formato obligatorio del borrador

# Borrador de seguimiento

## 1. Resumen ejecutivo
## 2. Evolución / avances detectados
## 3. Capabilities impactadas
## 4. HUs impactadas
## 5. Riesgos detectados
## 6. Deuda acumulada
## 7. Decisiones o definiciones pendientes
## 8. Compromisos / próximos pasos
## 9. Desviación contra TO-BE
## 10. Recomendación de guardado

## Reglas duras
- No inventar responsables.
- No inventar fechas.
- Si una HU no se puede identificar, decir “HU no identificada”.
- Si una capability no se puede identificar, decir “Capability no identificada”.
- No modificar canon sin aprobación explícita.
