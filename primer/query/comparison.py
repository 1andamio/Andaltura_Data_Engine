"""
Expresiones de comparación.
"""

from __future__ import annotations

from typing import Any

from primer.query.expression import Expression


class ComparisonExpression(Expression[Any]):
    """
    Compara el valor de un campo con otro valor.
    """

    def __init__(self, field, operator: str, value: Any):
        self.field = field
        self.operator = operator
        self.value = value

    def evaluate(self, item: Any) -> bool:
        left = self.field.value(item)

        match self.operator:
            case "==":
                return left == self.value
            case "!=":
                return left != self.value
            case "<":
                return left < self.value
            case "<=":
                return left <= self.value
            case ">":
                return left > self.value
            case ">=":
                return left >= self.value

        raise ValueError(f"Operador no soportado: {self.operator}")