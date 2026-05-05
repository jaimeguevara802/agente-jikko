import json
import urllib.request
import urllib.error
import ssl

SUPABASE_URL = "https://fwwkesboxlbmimzyoztq.supabase.co"
# Usando la misma Service Role Key que tenemos en sync_obsidian.py para pruebas internas
SUPABASE_SERVICE_ROLE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZ3d2tlc2JveGxibWltenlvenRxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3Nzk4MDMzMiwiZXhwIjoyMDkzNTU2MzMyfQ.rj3EkRLTS89tM3NbyftV023mWUbHIB4DvXU6cJZzVVU"

def insert_project():
    url = f"{SUPABASE_URL}/rest/v1/projects"
    headers = {
        "apikey": SUPABASE_SERVICE_ROLE_KEY,
        "Authorization": f"Bearer {SUPABASE_SERVICE_ROLE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=representation" # Para que devuelva la data insertada
    }
    
    project_data = {
        "name": "Supplier Data & Dashboard",
        "project_code": "SUP-001",
        "status": "Discovery",
        "business_area": "Growth / Supply",
        "owner": "Jaime Guevara",
        "team": "Célula Dropi",
        "summary": "Levantamiento de data estructurada de suppliers (cuantitativa y cualitativa) para construir un dashboard centralizado que facilite la toma de decisiones basada en puntos de dolor."
    }
    
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    req = urllib.request.Request(url, data=json.dumps(project_data).encode(), headers=headers, method='POST')
    
    try:
        with urllib.request.urlopen(req, context=ctx) as response:
            result = json.loads(response.read().decode())
            print("✅ Proyecto Canónico creado exitosamente en Supabase:")
            print(json.dumps(result, indent=2, ensure_ascii=False))
            return True
    except urllib.error.HTTPError as e:
        print(f"❌ Error HTTP: {e.code}")
        print(e.read().decode())
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False

if __name__ == "__main__":
    print("Intentando crear el primer proyecto en la nueva tabla 'projects'...")
    insert_project()
