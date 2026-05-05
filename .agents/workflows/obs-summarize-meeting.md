# obs-summarize-meeting

**Descripción**: Genera una minuta procesada a partir de una transcripción.

## Prerrequisitos
- Plantilla `tpl_meeting_note.md` disponible.

## Pasos del Agente
1. Pídele al usuario que te indique dónde está la transcripción (puede estar en el Inbox o en Scratch).
2. Lee `obsidian-meeting-synthesizer/SKILL.md`.
3. Lee el texto crudo y genera la minuta estructurada.
4. Guárdala en `/knowledge/obsidian-vault/04_Meetings/` con nombre en formato `YYYY-MM-DD-Tema.md`.
