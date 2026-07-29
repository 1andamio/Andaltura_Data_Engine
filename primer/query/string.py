"""
Expresiones para operaciones sobre cadenas de texto.
"""

from __future__ import annotations

from typing import Any

from primer.query.expression import Expression


class StringExpression(Expression[Any]):
    """
    Clase base para expresiones sobre cadenas.
    """

    def __init__(self, field, value: str):
        self.field = field
        self.value = value


class Contains(StringExpression):
    """
    Comprueba si una cadena contiene otra.
    """

    def evaluate(self, item: Any) -> bool:
        field_value = self.field.value(item)

        if field_value is None:
            return False

        return self.value in str(field_value)


class StartsWith(StringExpression):
    """
    Comprueba si una cadena comienza por otra.
    """

    def evaluate(self, item: Any) -> bool:
        field_value = self.field.value(item)

        if field_value is None:
            return False

        return str(field_value).startswith(self.value)


class EndsWith(StringExpression):
    """
    Comprueba si una cadena termina por otra.
    """

    def evaluate(self, item: Any) -> bool:
        field_value = self.field.value(item)

        if field_value is None:
            return False

        return str(field_value).endswith(self.value)