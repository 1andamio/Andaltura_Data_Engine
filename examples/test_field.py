from dataclasses import dataclass

from primer.query.field import Field


@dataclass
class City:
    name: str
    population: int


city = City("Granada", 230000)

print((Field("name") == "Granada")(city))
print((Field("population") > 100000)(city))
print((Field("population") < 100000)(city))