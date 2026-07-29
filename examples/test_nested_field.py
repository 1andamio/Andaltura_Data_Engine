from dataclasses import dataclass

from primer.query.field import Field


@dataclass
class Name:
    text: str


@dataclass
class Identifier:
    local_id: str


@dataclass
class City:

    identifier: Identifier
    name: Name


city = City(
    identifier=Identifier("ES001"),
    name=Name("Granada"),
)

print((Field("name.text") == "Granada")(city))
print((Field("identifier.local_id") == "ES001")(city))
print((Field("identifier.local_id") == "ES999")(city))