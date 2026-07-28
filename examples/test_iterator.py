from primer.services.wfs.client import WFSClient
from primer.services.wfs.iterator import FeatureIterator

WFS_URL = "https://www.ideandalucia.es/wfs-nga-inspire/services"

client = WFSClient(WFS_URL)

iterator = FeatureIterator(
    client,
    type_name="gn:NamedPlace",
    batch_size=10,
)

response = next(iterator)

print(f"Status Code : {response.status_code}")
print()
print(response.text[:1000])

client.close()