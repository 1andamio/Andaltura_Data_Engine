from collections import Counter
from xml.etree import ElementTree as ET

from primer.services.wfs.client import WFSClient
from primer.services.wfs.iterator import FeatureIterator
from primer.services.wfs.parser import WFSParser


counter = Counter()


def walk(element: ET.Element, prefix: str = ""):

    tag = element.tag.split("}")[-1]

    path = f"{prefix}/{tag}" if prefix else tag

    counter[path] += 1

    for child in element:
        walk(child, path)


client = WFSClient(
    "https://www.ideandalucia.es/wfs-nga-inspire/services"
)

iterator = FeatureIterator(
    client,
    type_name="gn:NamedPlace",
    batch_size=100,
)

response = next(iterator)

parser = WFSParser()

for feature in parser.iter_features(response.text):
    walk(feature)

client.close()

print()
print("========== CAMPOS ==========")
print()

for path, count in sorted(counter.items()):
    print(f"{count:3}  {path}")