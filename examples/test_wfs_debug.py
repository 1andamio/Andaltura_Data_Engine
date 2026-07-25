from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import requests
import xml.etree.ElementTree as ET

URL = (
    "https://www.ideandalucia.es/wfs-nga/services?"
    "SERVICE=WFS"
    "&REQUEST=GetCapabilities"
    "&VERSION=1.1.0"
)

print("=" * 80)
print("DESCARGANDO CAPABILITIES")
print("=" * 80)

xml = requests.get(URL, timeout=60)
xml.raise_for_status()

root = ET.fromstring(xml.content)

print("\nRAÍZ:")
print(root.tag)

print("\nNAMESPACES ENCONTRADOS")
print("-" * 80)

for event, elem in ET.iterparse(
    __import__("io").BytesIO(xml.content),
    events=("start-ns",),
):
    print(elem)

print("\nFEATURE TYPES")
print("-" * 80)

for feature in root.iter():
    if feature.tag.endswith("FeatureType"):

        print("\n================ FEATURETYPE ================\n")

        for child in feature:

            tag = child.tag.split("}")[-1]
            text = (child.text or "").strip()

            print(f"{tag:20} {text}")

        print("\nXML ORIGINAL\n")
        print(ET.tostring(feature, encoding="unicode"))