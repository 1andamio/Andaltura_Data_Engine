from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import requests

url = (
    "https://www.ideandalucia.es/wfs-nga/services?"
    "service=WFS&request=GetCapabilities"
)

print("Conectando...")

response = requests.get(url, timeout=60)

print("Status:", response.status_code)
print("Content-Type:", response.headers.get("Content-Type"))
print()
print(response.text[:3000])