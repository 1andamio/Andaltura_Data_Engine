from datetime import datetime

from primer.datasets.named_places import NamedPlaceDataset
from primer.models.common.geometry import Point
from primer.models.common.geographical_name import GeographicalName
from primer.models.common.identifier import Identifier
from primer.models.geonames.named_place import NamedPlace


dataset = NamedPlaceDataset()

place = NamedPlace(
    identifier=Identifier(
        namespace="ES.ES61.NGA",
        local_id="1",
    ),
    name=GeographicalName(
        text="Prueba",
        language="spa",
        nativeness="endonym",
        name_status="official",
        source="Test",
        script="Latn",
    ),
    geometry=Point(
        1.0,
        2.0,
    ),
    local_type="Lugar",
    feature_type="test",
    begin_lifespan_version=datetime.now(),
)

dataset.add(place)

print(dataset)

print(len(dataset))

print(dataset.first())

print(dataset.last())

print(bool(dataset))

for item in dataset:
    print(item.text)