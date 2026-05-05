# obs-generate-user-stories

**Descripción**: Baja un PRD a historias de usuario en Obsidian.

## Prerrequisitos
- Debe existir un PRD en `02_Product/`.

## Pasos del Agente
1. Lee `obsidian-product-doc-generator/SKILL.md`.
2. Lee el PRD especificado por el usuario.
3. Extrae las funcionalidades y usa `tpl_user_story.md` para generar múltiples archivos.
4. Guarda las historias en `02_Product/` asociándolas al PRD mediante wikilinks.
