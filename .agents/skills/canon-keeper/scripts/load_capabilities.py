from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict, List
from urllib.parse import quote

import requests
from dotenv import load_dotenv

ROOT = Path.cwd()
load_dotenv(ROOT / ".env")

API_URL = os.getenv("AIRTABLE_API_URL", "https://api.airtable.com/v0").rstrip("/")
TOKEN = os.getenv("AIRTABLE_TOKEN")
BASE_ID = os.getenv("AIRTABLE_BASE_ID")
TABLE_NAME = "Capabilities"
PROJECT = "[Company Project]"

CAPABILITIES: List[Dict[str, Any]] = [
    # Add your project capabilities here
]

REQUIRED_FIELDS = {
    "Capability ID": "singleLineText",
    "Project": "singleLineText",
    "Name": "singleLineText",
    "Purpose": "multilineText",
    "Scope": "multilineText",
    "Expected Outcome": "multilineText",
    "Exclusions": "multilineText",
    "Status": "singleLineText",
    "Version": "singleLineText",
    "Order": "singleLineText",
    "Source References": "multilineText",
}


def require_env() -> None:
    missing = [k for k, v in {"AIRTABLE_TOKEN": TOKEN, "AIRTABLE_BASE_ID": BASE_ID}.items() if not v]
    if missing:
        raise SystemExit(f"Faltan variables de entorno: {', '.join(missing)}")


def headers() -> Dict[str, str]:
    return {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}


def request_json(method: str, path: str, payload: Dict[str, Any] | None = None, params: Dict[str, Any] | None = None) -> Dict[str, Any]:
    url = f"{API_URL}{path}"
    response = requests.request(method, url, headers=headers(), json=payload, params=params, timeout=60)
    if response.status_code >= 400:
        raise SystemExit(f"Error {response.status_code} en {method} {url}: {response.text}")
    return response.json() if response.text.strip() else {}


def get_schema() -> Dict[str, Any]:
    return request_json("GET", f"/meta/bases/{BASE_ID}/tables")


def get_table(schema: Dict[str, Any], table_name: str) -> Dict[str, Any]:
    for table in schema.get("tables", []):
        if table.get("name") == table_name:
            return table
    raise SystemExit(f"No encontré la tabla {table_name}")


def create_field(table_id: str, name: str, field_type: str) -> None:
    request_json(
        "POST",
        f"/meta/bases/{BASE_ID}/tables/{table_id}/fields",
        payload={"name": name, "type": field_type},
    )


def ensure_fields() -> None:
    schema = get_schema()
    table = get_table(schema, TABLE_NAME)
    existing = {field["name"] for field in table.get("fields", [])}

    created = []
    for field_name, field_type in REQUIRED_FIELDS.items():
        if field_name not in existing:
            create_field(table["id"], field_name, field_type)
            created.append(field_name)

    if created:
        print(json.dumps({"created_fields": created}, ensure_ascii=False, indent=2))


def find_record(capability_id: str) -> str | None:
    params = {
        "filterByFormula": f"{{Capability ID}}='{capability_id}'",
        "maxRecords": 1,
    }
    data = request_json("GET", f"/{BASE_ID}/{quote(TABLE_NAME)}", params=params)
    records = data.get("records", [])
    return records[0]["id"] if records else None


def create_record(fields: Dict[str, Any]) -> str:
    payload = {"records": [{"fields": fields}], "typecast": True}
    result = request_json("POST", f"/{BASE_ID}/{quote(TABLE_NAME)}", payload=payload)
    return result["records"][0]["id"]


def update_record(record_id: str, fields: Dict[str, Any]) -> None:
    payload = {"fields": fields, "typecast": True}
    request_json("PATCH", f"/{BASE_ID}/{quote(TABLE_NAME)}/{record_id}", payload=payload)


def main() -> None:
    require_env()
    ensure_fields()

    created = []
    updated = []

    for capability in CAPABILITIES:
        record_id = find_record(capability["Capability ID"])
        if record_id:
            update_record(record_id, capability)
            updated.append(capability["Capability ID"])
        else:
            new_id = create_record(capability)
            created.append({"capability_id": capability["Capability ID"], "record_id": new_id})

    print(json.dumps({
        "table": TABLE_NAME,
        "project": PROJECT,
        "created": created,
        "updated": updated,
        "total": len(CAPABILITIES),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
