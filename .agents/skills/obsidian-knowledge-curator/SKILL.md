---
name: obsidian-knowledge-curator
description: Lee el Inbox de Obsidian, clasifica notas, aplica etiquetas y las mueve a sus carpetas correctas.
---

# Knowledge Curator

## Objetivo
Mantener el orden del Vault procesando cualquier archivo Markdown crudo que caiga en `/knowledge/obsidian-vault/00_Inbox/`.

## Instrucciones
1. Escanea la carpeta `00_Inbox`.
2. Lee el contenido de cada archivo Markdown.
3. Determina de qué trata (dominio, descubrimiento, actas sueltas, etc.).
4. Sugiere una clasificación y aplica el frontmatter adecuado.
5. Mueve el archivo a la carpeta final (`01_Domain`, `03_Discovery`, etc.).
6. Si la nota menciona personas o conceptos clave, asegúrate de crear enlaces (wikilinks `[[ ]]`).
