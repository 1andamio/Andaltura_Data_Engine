"""
Campo de una entidad utilizado para construir expresiones.
"""

from __future__ import annotations

from typing import Any

from primer.query.comparison import ComparisonExpression
from primer.query.order import OrderBy
from primer.query.string import Contains, EndsWith, StartsWith


class Field:
    """
    Representa un atributo de un modelo.

    Soporta atributos anidados mediante notación con puntos.

    Ejemplos:
        Field("name.text")
        Field("identifier.local_id")
        Field("geometry.x")
    """

    def __init__(self, path: str):
        self.path = path

    def value(self, item: Any) -> Any:
        """
        Obtiene el valor siguiendo una ruta de atributos.
        """

        value = item

        for attribute in self.path.split("."):
            value = getattr(value, attribute)

        return value

    # ---------------------------------------------------------
    # Expresiones de texto
    # ---------------------------------------------------------

    def contains(self, text: str) -> Contains:
        return Contains(self, text)

    def startswith(self, text: str) -> StartsWith:
        return StartsWith(self, text)

    def endswith(self, text: str) -> EndsWith:
        return EndsWith(self, text)

    # ---------------------------------------------------------
    # Ordenación
    # ---------------------------------------------------------

    def asc(self) -> OrderBy:
        return OrderBy(self, ascending=True)

    def desc(self) -> OrderBy:
        return OrderBy(self, ascending=False)

    # ---------------------------------------------------------
    # Comparaciones
    # ---------------------------------------------------------

    def __eq__(self, other: Any) -> ComparisonExpression:  # type: ignore[override]
        return ComparisonExpression(self, "==", other)

    def __ne__(self, other: Any) -> ComparisonExpression:
        return ComparisonExpression(self, "!=", other)

    def __lt__(self, other: Any) -> ComparisonExpression:
        return ComparisonExpression(self, "<", other)

    def __le__(self, other: Any) -> ComparisonExpression:
        return ComparisonExpression(self, "<=", other)

    def __gt__(self, other: Any) -> ComparisonExpression:
        return ComparisonExpression(self, ">", other)

    def __ge__(self, other: Any) -> ComparisonExpression:
        return ComparisonExpression(self, ">=", other)

    def __repr__(self) -> str:
        return f"Field({self.path!r})"