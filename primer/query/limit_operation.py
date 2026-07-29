"""
Operación LIMIT.
"""

from __future__ import annotations

from primer.query.operation import Operation


class LimitOperation(Operation):
    """
    Limita el número de elementos de un dataset.
    """

    def __init__(self, limit: int):

        if limit < 0:
            raise ValueError("limit must be greater than or equal to zero")

        self.limit = limit

    def apply(self, dataset):

        return dataset.__class__(
            list(dataset)[: self.limit]
        )

    def __repr__(self):

        return f"LimitOperation({self.limit})"