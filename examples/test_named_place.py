from datetime import datetime

from primer.models.common.geometry import Point
from primer.models.common.geographical_name import GeographicalName
from primer.models.common.identifier import Identifier
from primer.models.geonames.named_place import NamedPlace


place = NamedPlace(
    identifier=Identifier(
        namespace="ES.ES61.NGA",
        local_id="242130",
    ),
    name=GeographicalName(
        text="EF A-6050",
        language="spa",
        nativeness="endonym",
        name_status="other",
        source="Nomenclátor Geográfico de Andalucía.",
        script="Latn",
    ),
    geometry=Point(
        428114.054,
        4177614.090,
    ),
    local_type="Vía de Comunicación",
    feature_type="transportNetwork",
    begin_lifespan_version=datetime.fromisoformat(
        "2019-11-15T00:00:00+00:00"
    ),
)

print(place)

print(place.identifier)

print(place.text)

print(place.geometry)

print(place.local_type)

print(place.feature_type)

print(place.begin_lifespan_version)