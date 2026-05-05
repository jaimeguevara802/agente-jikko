---
name: sync-jcommander
description: Sincroniza notas crudas de J-Commander, usa IA para extraer tareas implícitas y las devuelve al sistema de pendientes.
---

# Sync J-Commander Workflow

Este workflow define el protocolo para que el Agente asuma el rol de analista al procesar las "Notas Rápidas" creadas por el usuario en su aplicación móvil (J-Commander).

## Objetivo
Quitarle al usuario la carga cognitiva de tener que escribir con sintaxis perfecta de Markdown en su teléfono. El usuario puede simplemente "escupir" sus ideas o grabar notas de voz/texto en J-Commander, y el agente se encargará de darle estructura y convertir la intención en accionables reales.

## Pasos del Workflow

1. **Descarga Inicial:**
   - Ejecuta el comando `python3 sync_obsidian.py` dentro de la carpeta `j-commander`.
   - Esto bajará las nuevas notas desde la nube de Supabase hacia la carpeta `knowledge/obsidian-vault/00_Inbox`.

2. **Curaduría y Extracción (IA):**
   - Busca en `00_Inbox` los archivos que comiencen con `JC_` y que no contengan la etiqueta `#status/procesado`.
   - Lee el contenido de cada archivo.
   - **Aplica tu criterio como PM/Agente:**
     - Identifica qué partes son contexto, ideas o pensamientos (déjalos como párrafos o viñetas normales).
     - Identifica qué partes implican una acción que el equipo o Jaime deben realizar.
     - Transforma las acciones encontradas usando la sintaxis estricta de Markdown para tareas: `- [ ] Acción a realizar`.
   - Una vez modificado el archivo, añade la etiqueta `#status/procesado` al YAML frontmatter o al inicio del documento.

3. **Subida de Accionables:**
   - Vuelve a ejecutar el comando `python3 sync_obsidian.py` dentro de la carpeta `j-commander`.
   - Esto escaneará el Inbox en busca de los nuevos checkboxes `- [ ]` que acabas de generar y los enviará automáticamente a la base de datos de tareas de J-Commander.

4. **Reporte:**
   - Termina tu turno informando al usuario cuántas notas procesaste y un resumen breve de los accionables que le organizaste en su sistema.
