from xml.etree import ElementTree as ET

from primer.services.wfs import WFSClient

client = WFSClient(
    "https://www.ideandalucia.es/wfs-nga-inspire/services"
)

xml = client.get_capabilities()

root = ET.fromstring(xml)

ns = {
    "wfs": "http://www.opengis.net/wfs/2.0",
}

print()
print("=" * 80)
print("FEATURE TYPES")
print("=" * 80)
print()

for feature in root.findall(".//wfs:FeatureType", ns):

    name = feature.find("wfs:Name", ns)
    title = feature.find("wfs:Title", ns)

    print("NAME :", name.text if name is not None else "")
    print("TITLE:", title.text if title is not None else "")
    print("-" * 80)

client.close()