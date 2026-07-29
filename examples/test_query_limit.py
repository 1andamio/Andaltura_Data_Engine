from dataclasses import dataclass

from primer.datasets.base import BaseDataset
from primer.query.field import Field


@dataclass
class City:
    name: str
    population: int


dataset = BaseDataset([
    City("Granada", 230000),
    City("Jaén", 112000),
    City("Almería", 198000),
])

query = (
    dataset
        .query()
        .where(Field("population") > 100000)
        .order_by(Field("name").asc())
        .limit(1)
)

print(query.count())

for city in query:
    print(city.name)