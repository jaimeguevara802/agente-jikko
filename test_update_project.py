import json
import urllib.request
import urllib.error
import ssl

SUPABASE_URL = "https://fwwkesboxlbmimzyoztq.supabase.co"
SUPABASE_SERVICE_ROLE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZ3d2tlc2JveGxibWltenlvenRxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3Nzk4MDMzMiwiZXhwIjoyMDkzNTU2MzMyfQ.rj3EkRLTS89tM3NbyftV023mWUbHIB4DvXU6cJZzVVU"

def update_prototype_url():
    url = f"{SUPABASE_URL}/rest/v1/projects?project_code=eq.SUP-001"
    headers = {
        "apikey": SUPABASE_SERVICE_ROLE_KEY,
        "Authorization": f"Bearer {SUPABASE_SERVICE_ROLE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=representation"
    }
    
    update_data = {
        "prototype_url": "prototypes/sup-001-v2.html"
    }
    
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    req = urllib.request.Request(url, data=json.dumps(update_data).encode(), headers=headers, method='PATCH')
    
    try:
        with urllib.request.urlopen(req, context=ctx) as response:
            result = json.loads(response.read().decode())
            print("✅ URL del prototipo asignada exitosamente al proyecto SUP-001.")
            return True
    except Exception as e:
        print(f"❌ Error al hacer PATCH: {e}")
        return False

if __name__ == "__main__":
    update_prototype_url()
