# obs-sync-to-pm

**Descripción**: Sincroniza conocimiento aprobado en el Vault hacia la capa oficial (Canon/Airtable).

## Prerrequisitos
- El documento en el Vault debe estar etiquetado con `#status/approved`.

## Pasos del Agente
1. Lee `obsidian-pm-sync-agent/SKILL.md` y `canon/operating_rules.md`.
2. Busca notas listas para sincronizar (ej. PRDs, HUs, Decisiones).
3. Transfórmalas al formato requerido por la capa PM.
4. Muestra un resumen de los cambios (diff o payload) y pide permiso.
5. Si el usuario aprueba, actualiza el Canon Oficial o Airtable y cambia la etiqueta de la nota a `#status/synced`.
