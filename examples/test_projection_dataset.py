from primer.datasets.projection_dataset import ProjectionDataset
from primer.models.row import Row


dataset = ProjectionDataset([
    Row(
        name="Granada",
        population=230000,
    ),
    Row(
        name="Jaén",
        population=112000,
    ),
])

print(dataset)

print(dataset.columns())

print(dataset.to_dicts())

for row in dataset:
    print(row.name)