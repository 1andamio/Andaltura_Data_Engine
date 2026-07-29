from dataclasses import dataclass

from primer.datasets.base import BaseDataset
from primer.query.fieldset import FieldSet
from primer.query.select_operation import SelectOperation


@dataclass
class City:
    name: str
    population: int


dataset = BaseDataset([
    City("Granada", 230000),
    City("Jaén", 112000),
    City("Almería", 198000),
])

operation = SelectOperation(
    FieldSet(
        "name",
        "population",
    )
)

result = operation.apply(dataset)

print(type(result).__name__)

print(result.columns())

for row in result:
    print(row)