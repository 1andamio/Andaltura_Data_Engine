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
        .where(Field("population") > 150000)
        .order_by(Field("name").asc())
)

result = query.all()

print(type(result).__name__)

for city in result:
    print(city.name)