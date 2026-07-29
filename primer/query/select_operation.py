"""
Operación SELECT.
"""

from __future__ import annotations

from primer.datasets.projection_dataset import ProjectionDataset
from primer.models.row import Row
from primer.query.fieldset import FieldSet
from primer.query.operation import Operation


class SelectOperation(Operation):
    """
    Proyecta un conjunto de entidades sobre un conjunto de campos.
    """

    def __init__(self, fields: FieldSet):

        self.fields = fields

    def apply(self, dataset):

        rows = []

        for entity in dataset:

            values = {}

            for field in self.fields:

                values[field.path] = field.get_value(entity)

            rows.append(Row(**values))

        return ProjectionDataset(rows)

    def __repr__(self):

        return f"SelectOperation({self.fields})"