from primer.services.wfs.client import WFSClient
from primer.services.wfs.iterator import FeatureIterator
from primer.services.wfs.parser import WFSParser

client = WFSClient(
    "https://www.ideandalucia.es/wfs-nga-inspire/services"
)

iterator = FeatureIterator(
    client,
    type_name="gn:NamedPlace",
    batch_size=10,
)

response = next(iterator)

parser = WFSParser()

print("Número de entidades:", parser.count_features(response.text))

print()

for feature in parser.iter_features(response.text):
    print(feature.tag)