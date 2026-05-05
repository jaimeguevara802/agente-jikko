# obs-process-inbox

**Descripción**: Limpia el Inbox del Vault clasificando cualquier nota suelta.

## Prerrequisitos
- El sistema debe tener acceso a `/knowledge/obsidian-vault/00_Inbox/`.

## Pasos del Agente
1. Lee `canon/obsidian_vault_rules.md`.
2. Lee `obsidian-knowledge-curator/SKILL.md`.
3. Escanea todos los archivos Markdown en `00_Inbox/`.
4. Analiza su contenido, propón un nombre adecuado y una ruta final.
5. Pide confirmación al usuario o muévelos automáticamente si tienes alta confianza.
