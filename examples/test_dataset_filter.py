from datetime import datetime

from primer.datasets.named_places import NamedPlaceDataset
from primer.models.common.geometry import Point
from primer.models.common.geographical_name import GeographicalName
from primer.models.common.identifier import Identifier
from primer.models.geonames.named_place import NamedPlace


def create_place(local_id: str, name: str, feature_type: str) -> NamedPlace:
    return NamedPlace(
        identifier=Identifier(
            namespace="ES.ES61.NGA",
            local_id=local_id,
        ),
        name=GeographicalName(
            text=name,
            language="spa",
            nativeness="endonym",
            name_status="official",
            source="Test",
            script="Latn",
        ),
        geometry=Point(0.0, 0.0),
        local_type="Lugar",
        feature_type=feature_type,
        begin_lifespan_version=datetime.now(),
    )


dataset = NamedPlaceDataset()

dataset.add(create_place("1", "Río A", "hydrography"))
dataset.add(create_place("2", "Monte B", "relief"))
dataset.add(create_place("3", "Rambla C", "hydrography"))

hydro = dataset.where(lambda p: p.feature_type == "hydrography")

print(dataset)
print(hydro)
print(len(dataset))
print(len(hydro))

for place in hydro:
    print(place.text)