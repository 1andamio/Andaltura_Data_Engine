from dataclasses import dataclass

from primer.datasets.base import BaseDataset
from primer.query.field import Field
from primer.query.order_by_operation import OrderByOperation


@dataclass
class City:
    name: str
    population: int


dataset = BaseDataset([
    City("Granada", 230000),
    City("Jaén", 112000),
    City("Almería", 198000),
])

operation = OrderByOperation(
    Field("name").asc()
)

result = operation.apply(dataset)

print(type(result).__name__)

for city in result:
    print(city.name)