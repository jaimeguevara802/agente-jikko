# obs-extract-decisions

**Descripción**: Escanea reuniones y extrae decisiones a la carpeta 05_Decisions.

## Prerrequisitos
- Debe haber minutas procesadas en `04_Meetings`.

## Pasos del Agente
1. Lee `obsidian-decision-extractor/SKILL.md`.
2. Revisa las reuniones de la última semana.
3. Extrae decisiones formalizadas en `tpl_decision_log.md`.
4. Guárdalas en `05_Decisions/` conectándolas con links `[[ ]]` a la reunión original.
