from dataclasses import dataclass

from primer.datasets.base import BaseDataset
from primer.query.field import Field
from primer.query.where_operation import WhereOperation


@dataclass
class City:
    name: str
    population: int


dataset = BaseDataset([
    City("Granada", 230000),
    City("Jaén", 112000),
    City("Almería", 198000),
])

operation = WhereOperation(
    Field("population") > 150000
)

result = operation.apply(dataset)

print(type(result).__name__)

for city in result:
    print(city.name)