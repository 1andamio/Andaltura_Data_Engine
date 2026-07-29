"""
Expresiones lógicas.
"""

from __future__ import annotations

from typing import Any

from primer.query.expression import Expression


class LogicalExpression(Expression[Any]):
    """
    Clase base para todas las expresiones lógicas.
    """

    pass


class And(LogicalExpression):
    """
    Operador lógico AND.
    """

    def __init__(self, left: Expression[Any], right: Expression[Any]) -> None:
        self.left = left
        self.right = right

    def evaluate(self, item: Any) -> bool:
        return self.left(item) and self.right(item)


class Or(LogicalExpression):
    """
    Operador lógico OR.
    """

    def __init__(self, left: Expression[Any], right: Expression[Any]) -> None:
        self.left = left
        self.right = right

    def evaluate(self, item: Any) -> bool:
        return self.left(item) or self.right(item)


class Not(LogicalExpression):
    """
    Operador lógico NOT.
    """

    def __init__(self, expression: Expression[Any]) -> None:
        self.expression = expression

    def evaluate(self, item: Any) -> bool:
        return not self.expression(item)