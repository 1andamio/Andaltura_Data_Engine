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

print("ASC")

for city in dataset.order_by(Field("name").asc()):
    print(city.name)

print()

print("DESC")

for city in dataset.order_by(Field("population").desc()):
    print(city.name, city.population)