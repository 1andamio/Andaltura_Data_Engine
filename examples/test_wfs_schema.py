from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import requests

URL = (
    "https://www.ideandalucia.es/wfs-nga/services?"
    "SERVICE=WFS"
    "&VERSION=1.1.0"
    "&REQUEST=DescribeFeatureType"
    "&TYPENAME=app:Entidad"
    "&NAMESPACE=xmlns(app=http://www.deegree.org/app)"
)

print("Obteniendo esquema...\n")

response = requests.get(URL, timeout=60)
response.raise_for_status()

print("Status:", response.status_code)
print()
print(response.text)