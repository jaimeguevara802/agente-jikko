from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[4]
load_dotenv(ROOT / ".env")

SUPA_URL = os.getenv("SUPABASE_URL", "").rstrip("/")
SUPA_KEY = os.getenv("SUPABASE_SERVICE_KEY", "")
TIMEOUT = 60


class WriterError(Exception):
    pass


def require_env() -> None:
    missing = [k for k, v in {"SUPABASE_URL": SUPA_URL, "SUPABASE_SERVICE_KEY": SUPA_KEY}.items() if not v]
    if missing:
        raise WriterError(f"Faltan variables de entorno: {', '.join(missing)}")


def headers() -> dict:
    return {
        "apikey": SUPA_KEY,
        "Authorization": f"Bearer {SUPA_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=representation",
    }


def rest(method: str, table: str, payload: dict | list | None = None, params: dict | None = None) -> list:
    url = f"{SUPA_URL}/rest/v1/{table}"
    resp = requests.request(method, url, headers=headers(), json=payload, params=params, timeout=TIMEOUT)
    if resp.status_code >= 400:
        raise WriterError(f"Error {resp.status_code} en {method} {table}: {resp.text}")
    return resp.json() if resp.text.strip() else []


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def get_project_id(project_code: str) -> str:
    records = rest("GET", "projects", params={"project_code": f"eq.{project_code}", "select": "id,name"})
    if not records:
        raise WriterError(f"Proyecto '{project_code}' no encontrado en Supabase.")
    return records[0]["id"]


def read_content(args: argparse.Namespace) -> str:
    if getattr(args, "content_file", None):
        return Path(args.content_file).read_text(encoding="utf-8")
    if getattr(args, "content", None):
        return args.content
    data = sys.stdin.read()
    if data.strip():
        return data
    raise WriterError("Debes enviar contenido con --content-file, --content o stdin.")


# ── Commands ──────────────────────────────────────────────────────────────────

def cmd_ingest(args: argparse.Namespace) -> None:
    """Ingresa una transcripción cruda en la tabla transcripts."""
    require_env()
    content = read_content(args)
    project_id = get_project_id(args.project_code)

    record = {
        "project_id": project_id,
        "raw_transcript": content,
        "source_url": args.source_url or "",
        "imported_at": now_iso(),
        "immutable": False,
    }
    if args.meeting_id:
        record["meeting_id"] = args.meeting_id

    created = rest("POST", "transcripts", payload=record)
    print(json.dumps({"action": "ingest", "project_code": args.project_code, "record": created[0] if created else {}}, ensure_ascii=False, indent=2))


def cmd_draft(args: argparse.Namespace) -> None:
    """Guarda un borrador de insight en draft_insights."""
    require_env()
    content = read_content(args)
    project_id = get_project_id(args.project_code)

    record = {
        "project_id": project_id,
        "draft_type": args.draft_type,
        "title": args.title or f"{args.draft_type} - {now_iso()[:10]}",
        "content": content,
        "status": args.status or "Draft",
    }
    if args.meeting_id:
        record["meeting_id"] = args.meeting_id
    if args.version_hint is not None:
        record["version_hint"] = args.version_hint

    created = rest("POST", "draft_insights", payload=record)
    print(json.dumps({"action": "draft", "project_code": args.project_code, "record": created[0] if created else {}}, ensure_ascii=False, indent=2))


def cmd_publish(args: argparse.Namespace) -> None:
    """Publica un canon aprobado en approved_context."""
    require_env()
    content = read_content(args)
    project_id = get_project_id(args.project_code)

    # versión siguiente
    existing = rest("GET", "approved_context", params={
        "project_id": f"eq.{project_id}",
        "context_type": f"eq.{args.context_type}",
        "select": "id,version,status",
        "order": "version.desc",
        "limit": "100",
    })
    max_version = max((r.get("version", 0) for r in existing), default=0)
    next_version = int(max_version) + 1

    # marcar anteriores como Superseded
    superseded_ids = []
    for r in existing:
        if r.get("status") == "Active":
            rest("PATCH", f"approved_context?id=eq.{r['id']}", payload={"status": "Superseded"})
            superseded_ids.append(r["id"])

    record = {
        "project_id": project_id,
        "context_type": args.context_type,
        "title": args.title or f"{args.context_type} v{next_version}",
        "approved_content": content,
        "version": next_version,
        "status": "Active",
        "source_references": args.source_refs or "",
        "approved_by": args.approved_by or "Jaime",
        "approved_at": now_iso(),
    }
    created = rest("POST", "approved_context", payload=record)

    if args.sync_file:
        sync_path = Path(args.sync_file)
        sync_path.parent.mkdir(parents=True, exist_ok=True)
        sync_path.write_text(content, encoding="utf-8")

    print(json.dumps({
        "action": "publish",
        "project_code": args.project_code,
        "context_type": args.context_type,
        "version": next_version,
        "superseded_ids": superseded_ids,
        "record": created[0] if created else {},
        "synced_file": args.sync_file or None,
    }, ensure_ascii=False, indent=2))


def cmd_show_active(args: argparse.Namespace) -> None:
    """Muestra el canon activo de un tipo de contexto para un proyecto."""
    require_env()
    project_id = get_project_id(args.project_code)
    records = rest("GET", "approved_context", params={
        "project_id": f"eq.{project_id}",
        "context_type": f"eq.{args.context_type}",
        "status": "eq.Active",
        "order": "version.desc",
        "limit": "1",
    })
    print(json.dumps({"action": "show_active", "project_code": args.project_code, "context_type": args.context_type, "records": records}, ensure_ascii=False, indent=2))


# ── CLI ───────────────────────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Escritor de contexto en Supabase para el PM Operating System")
    sub = parser.add_subparsers(dest="command", required=True)

    # ingest
    ig = sub.add_parser("ingest", help="Ingresa transcripción cruda en transcripts")
    ig.add_argument("--project-code", required=True)
    ig.add_argument("--meeting-id")
    ig.add_argument("--source-url")
    ig.add_argument("--content-file")
    ig.add_argument("--content")
    ig.set_defaults(func=cmd_ingest)

    # draft
    dr = sub.add_parser("draft", help="Guarda borrador en draft_insights")
    dr.add_argument("--project-code", required=True)
    dr.add_argument("--draft-type", required=True, help="ASIS | TOBE | Capability | Feature | Risk | Decision | Summary | Open Question")
    dr.add_argument("--title")
    dr.add_argument("--meeting-id")
    dr.add_argument("--content-file")
    dr.add_argument("--content")
    dr.add_argument("--status", default="Draft")
    dr.add_argument("--version-hint", type=int)
    dr.set_defaults(func=cmd_draft)

    # publish
    pub = sub.add_parser("publish", help="Publica canon aprobado en approved_context")
    pub.add_argument("--project-code", required=True)
    pub.add_argument("--context-type", required=True, help="ASIS | TOBE | Capability | Feature | Risk | Decision")
    pub.add_argument("--title")
    pub.add_argument("--content-file")
    pub.add_argument("--content")
    pub.add_argument("--approved-by")
    pub.add_argument("--source-refs")
    pub.add_argument("--sync-file", help="Ruta local a sincronizar con la versión vigente")
    pub.set_defaults(func=cmd_publish)

    # show-active
    show = sub.add_parser("show-active", help="Muestra el canon activo de un tipo de contexto")
    show.add_argument("--project-code", required=True)
    show.add_argument("--context-type", required=True)
    show.set_defaults(func=cmd_show_active)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    try:
        main()
    except WriterError as exc:
        raise SystemExit(str(exc))
