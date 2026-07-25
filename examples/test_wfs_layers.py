from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import requests
import xml.etree.ElementTree as ET

URL = (
    "https://www.ideandalucia.es/wfs-nga/services?"
    "SERVICE=WFS"
    "&VERSION=1.1.0"
    "&REQUEST=GetCapabilities"
)

print("=" * 80)
print("Conectando al servicio WFS del Nomenclátor...")
print("=" * 80)

response = requests.get(URL, timeout=60)
response.raise_for_status()

print(f"Estado HTTP : {response.status_code}")
print()

root = ET.fromstring(response.content)

# Mostrar namespaces detectados
print("=" * 80)
print("RAÍZ DEL DOCUMENTO")
print("=" * 80)
print(root.tag)
print()

print("=" * 80)
print("BUSCANDO FEATURETYPE")
print("=" * 80)

feature_types = []

# Busca cualquier elemento cuyo nombre termine en FeatureType
for element in root.iter():
    if element.tag.endswith("FeatureType"):
        feature_types.append(element)

print(f"FeatureType encontrados: {len(feature_types)}")
print()

for i, feature in enumerate(feature_types, start=1):

    print("=" * 80)
    print(f"FEATURE TYPE {i}")
    print("=" * 80)

    print(ET.tostring(feature, encoding="unicode"))

    print()