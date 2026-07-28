from primer.readers.named_place_reader import NamedPlaceReader
from primer.services.wfs.client import WFSClient


client = WFSClient(
    "https://www.ideandalucia.es/wfs-nga-inspire/services"
)

reader = NamedPlaceReader(
    client,
    batch_size=10,
)

for i, place in enumerate(reader.read(), start=1):

    print(
        f"{i:02d} | "
        f"{place.local_id} | "
        f"{place.text} | "
        f"{place.feature_type}"
    )

    if i == 10:
        break

client.close()