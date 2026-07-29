"""
Operación ORDER BY.
"""

from __future__ import annotations

from primer.query.operation import Operation


class OrderByOperation(Operation):
    """
    Ordena un dataset utilizando un objeto OrderBy.
    """

    def __init__(self, order):
        self.order = order

    def apply(self, dataset):

        return dataset.__class__(
            sorted(
                dataset,
                key=self.order.key,
                reverse=not self.order.ascending,
            )
        )

    def __repr__(self):

        direction = "ASC" if self.order.ascending else "DESC"
        return f"OrderByOperation({direction})"