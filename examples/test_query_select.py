from dataclasses import dataclass

from primer.datasets.base import BaseDataset


@dataclass
class City:
    name: str
    population: int


dataset = BaseDataset([
    City("Granada", 230000),
    City("Jaén", 112000),
    City("Almería", 198000),
])

result = (
    dataset
    .query()
    .select(
        "name",
        "population",
    )
    .all()
)

print(type(result).__name__)

print(result.columns())

for row in result:
    print(row.name, row.population)