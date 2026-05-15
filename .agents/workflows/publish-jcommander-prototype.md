---
name: publish-jcommander-prototype
description: Publica un HTML de prototipo en j-commander y lo asocia a un proyecto existente en la pestaña Prototipo.
---

# Publish J-Commander Prototype Workflow

Usar este workflow cuando Jaime pida "sube este prototipo a jcommander", "asocialo al proyecto X", "publícalo como prototipo" o una variante similar.

## Contexto

- `j-commander` funciona como repositorio/submódulo dentro del workspace principal.
- Los prototipos viven en `j-commander/prototypes/*.html`.
- La app lee la tabla `projects` de Supabase.
- La pestaña **Prototipo** muestra:
  - Archivos con patrón automático `prototypes/{project_code_lower}-v1.html`, `v2`, etc.
  - O URLs explícitas en `projects.prototype_url`, separadas por coma.
- Si el nombre del HTML no sigue el patrón `{codigo}-vN.html`, actualizar `prototype_url`.

## Pasos

1. Confirmar el archivo origen.
   - Si ya está en `j-commander/prototypes/`, no moverlo.
   - Si está fuera, copiarlo a `j-commander/prototypes/` con nombre claro y estable.

2. Identificar el proyecto.
   - Revisar `.agents/memory/jcommander-projects.md`.
   - Si no está ahí, buscar en `knowledge/obsidian-vault/03_Discovery` por nombre o código.
   - El código canónico suele verse como `COM-001`, `SUP-001`, etc.

3. Consultar `projects.prototype_url` en Supabase antes de escribir.
   - Preservar URLs existentes.
   - Agregar la nueva URL con formato relativo: `prototypes/nombre-del-archivo.html`.
   - Evitar duplicados.

4. Actualizar Supabase.
   - Hacer PATCH a `projects?project_code=eq.<CODIGO>`.
   - Campo: `prototype_url`.
   - No guardar llaves o credenciales nuevas en archivos de memoria.

5. Publicar el archivo en `j-commander`.
   - `git -C j-commander status --short`
   - `git -C j-commander add prototypes/<archivo>.html`
   - `git -C j-commander diff --cached --check`
   - `git -C j-commander commit -m "Add <descripcion> prototype"`
   - `git -C j-commander push origin main`

6. Registrar el puntero del submódulo en el repo padre.
   - `git status --short`
   - `git add j-commander`
   - `git commit -m "Update j-commander prototype pointer"`
   - `git push origin main`
   - No tocar ni incluir archivos no relacionados del vault.

7. Actualizar memoria.
   - Editar `.agents/memory/jcommander-projects.md` con:
     - Proyecto/código.
     - Nueva URL de prototipo.
     - Commit de `j-commander`.
     - Fecha.

## Verificación mínima

- `git -C j-commander status --short` debe quedar limpio.
- El repo padre puede quedar con archivos no relacionados sin trackear; no incluirlos.
- Confirmar en la respuesta final:
  - Código de proyecto.
  - URL relativa del prototipo.
  - Commit de `j-commander`.
  - Commit del repo padre, si se actualizó.
