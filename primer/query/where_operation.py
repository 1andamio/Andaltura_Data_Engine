"""
Operación WHERE.
"""

from __future__ import annotations

from primer.query.operation import Operation


class WhereOperation(Operation):

    def __init__(self, expression):
        self.expression = expression

    def apply(self, dataset):

        return dataset.__class__(
            item
            for item in dataset
            if self.expression(item)
        )

    def __repr__(self):

        return f"WhereOperation({self.expression})"