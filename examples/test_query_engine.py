from dataclasses import dataclass

from primer.datasets.base import BaseDataset
from primer.query.field import Field


@dataclass
class City:
    name: str
    province: str
    population: int


dataset = BaseDataset([
    City("Granada", "Granada", 230000),
    City("Motril", "Granada", 58000),
    City("Jaén", "Jaén", 112000),
])

expr = (
    (Field("province") == "Granada")
    & (Field("population") > 100000)
)

result = dataset.where(expr)

print(result)

for city in result:
    print(city.name)