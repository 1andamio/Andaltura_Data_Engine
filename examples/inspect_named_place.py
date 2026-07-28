from xml.etree import ElementTree as ET

from primer.services.wfs.client import WFSClient
from primer.services.wfs.iterator import FeatureIterator
from primer.services.wfs.parser import WFSParser


def dump(element: ET.Element, level: int = 0) -> None:
    indent = "    " * level

    tag = element.tag.split("}")[-1]

    text = (element.text or "").strip()

    if text:
        print(f"{indent}{tag}: {text}")
    else:
        print(f"{indent}{tag}")

    for child in element:
        dump(child, level + 1)


client = WFSClient(
    "https://www.ideandalucia.es/wfs-nga-inspire/services"
)

iterator = FeatureIterator(
    client,
    type_name="gn:NamedPlace",
    batch_size=1,
)

response = next(iterator)

parser = WFSParser()

feature = next(parser.iter_features(response.text))

dump(feature)