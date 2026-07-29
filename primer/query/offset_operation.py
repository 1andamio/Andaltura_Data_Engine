"""
Operación OFFSET.
"""

from __future__ import annotations

from primer.query.operation import Operation


class OffsetOperation(Operation):
    """
    Descarta los primeros elementos de un dataset.
    """

    def __init__(self, offset: int):

        if offset < 0:
            raise ValueError("offset must be greater than or equal to zero")

        self.offset = offset

    def apply(self, dataset):

        return dataset.__class__(
            list(dataset)[self.offset:]
        )

    def __repr__(self):

        return f"OffsetOperation({self.offset})"