from dataclasses import dataclass

from primer.datasets.base import BaseDataset
from primer.query.limit_operation import LimitOperation


@dataclass
class City:
    name: str
    population: int


dataset = BaseDataset([
    City("Granada", 230000),
    City("Jaén", 112000),
    City("Almería", 198000),
])

operation = LimitOperation(2)

result = operation.apply(dataset)

print(type(result).__name__)
print(len(result))

for city in result:
    print(city.name)