# J-Commander Project Memory

Memoria operativa para publicar prototipos en la pestaña **Prototipo** de J-Commander.

## Reglas rápidas

- Prototipos: `j-commander/prototypes/*.html`.
- URL relativa para Supabase: `prototypes/<archivo>.html`.
- Proyecto en Supabase: tabla `projects`, clave práctica `project_code`.
- Campo usado por la app: `prototype_url`, con múltiples URLs separadas por coma.
- Si el archivo sigue `prototypes/{project_code_lower}-vN.html`, la app puede detectarlo por HEAD request.
- Si el archivo tiene otro nombre, registrar explícitamente en `prototype_url`.
- No sobrescribir `prototype_url` sin consultar y preservar lo existente.
- No guardar secretos de Supabase aquí.

## Proyectos conocidos

| Código | Nombre | Área | Prototipos registrados | Notas |
| --- | --- | --- | --- | --- |
| `COM-001` | Combos | Growth / Demand | `prototypes/flujo1-combos-creacion-supplier.html`, `prototypes/test-combo-producto-simple-shopify.html`, `prototypes/test-combo-producto-variable-shopify.html` | Proyecto de combos; prototipos Shopify simple y variable agregados el 2026-05-15. |
| `CELL-001` | Cellboard | Supplier Success | `prototypes/presentacion-1.html` | Proyecto creado en Supabase el 2026-05-15 con presentación de visión de producto. |
| `SUP-001` | Supplier Data & Dashboard | Growth / Supply | `prototypes/sup-001-v2.html` | Tiene patrón de versión y actualización histórica vía `test_update_project.py`. |

## Últimas publicaciones

| Fecha | Proyecto | Archivo | Commit j-commander | Commit repo padre |
| --- | --- | --- | --- | --- |
| 2026-05-15 | `COM-001` | `prototypes/test-combo-producto-simple-shopify.html` | `d106ca5` | `f0c4317` |
| 2026-05-15 | `COM-001` | `prototypes/test-combo-producto-variable-shopify.html` | `9a9e3e7` | `18a6b14` |
| 2026-05-15 | `CELL-001` | `prototypes/presentacion-1.html` | `d8d079a` | `pending` |
