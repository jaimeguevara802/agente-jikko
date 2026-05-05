# Reglas de Gobernanza: Obsidian Vault

Esta capa representa el **Conocimiento Vivo** del sistema. A diferencia del Canon Oficial (que requiere aprobación estricta para alterarse), el Vault es un sistema de archivos Markdown en constante evolución.

## 1. Reglas Generales de Interacción
- **No inventar información:** Si un dato no existe en las transcripciones, reuniones o notas previas, los agentes no deben alucinar ni crear información falsa.
- **Separar Hechos de Hipótesis:** Si se genera un documento basado en supuestos (ej. un PRD en fase Discovery), debe etiquetarse explícitamente con `#draft` o `#hipotesis`.
- **Inmutabilidad Relativa:** Las notas de reuniones (minutas y transcripciones) son registros inmutables. El descubrimiento y PRDs son documentos vivos.

## 2. Convenciones de Enlazado (Wikilinks)
- Los agentes deben conectar el conocimiento usando enlaces estilo Obsidian: `[[Nombre de la Nota]]`.
- Todo PRD debe enlazar a sus [[Decisiones]] e [[Historias de Usuario]].
- Toda decisión (`05_Decisions`) debe enlazar a la [[Reunión]] o [[Stakeholder]] que la originó.

## 3. Destrucción de Notas
- Los agentes **NUNCA** deben eliminar notas del Vault.
- Si una nota queda obsoleta o es un duplicado, debe moverse a una carpeta de Archivo o etiquetarse con `#deprecated`, o añadir un prefijo `[ARCHIVED]`.

## 4. Promoción a PM System
- La información contenida en el Vault *NO es oficial para ejecución* hasta que no se sincroniza con el PM System (Airtable/Canon).
- Solo las notas etiquetadas con `#status/approved` son candidatas para el workflow `obs-sync-to-pm.md`.
