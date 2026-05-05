---
tags: [moc, dashboard, pendientes]
---

# 🎯 Dashboard de Pendientes y Accionables

> [!INFO]
> Este tablero recopila automáticamente todos los accionables pendientes marcados en las reuniones y notas de descubrimiento. 
> *Nota: Requiere tener instalado y activado el plugin **Dataview** en Obsidian.*

## 🔥 Accionables Pendientes (Reuniones)

```dataview
TASK
FROM "04_Meetings"
WHERE !completed
```

## ✅ Tareas Completadas Recientemente

```dataview
TASK
FROM "04_Meetings" OR "03_Discovery"
WHERE completed
LIMIT 10
```

---
*Tip: Una vez que un pendiente de aquí se vuelve un compromiso oficial para ejecución, recuerda utilizar el proceso de sincronización (`obsidian-pm-sync-agent`) para enviarlo a la capa de Tracking de tu PM System.*
