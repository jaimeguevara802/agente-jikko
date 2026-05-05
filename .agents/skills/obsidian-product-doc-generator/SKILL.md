---
name: obsidian-product-doc-generator
description: Convierte notas de descubrimiento en PRDs y baja PRDs a Historias de Usuario.
---

# Product Doc Generator

## Objetivo
Traducir el conocimiento de negocio (Discovery) en documentos estructurados de producto dentro de la carpeta `02_Product`.

## Instrucciones
1. Toma como input uno o varios archivos de `03_Discovery`.
2. Si se solicita un PRD, usa `tpl_prd.md` y estructura el problema, casos de uso y requerimientos.
3. Si el PRD ya existe y se solicitan Historias, usa `tpl_user_story.md` y genera un archivo por historia en la carpeta de producto, enlazándolos al PRD original.
4. Etiqueta todo con `#draft` hasta que un humano lo valide.
