"""
Representa un campo consultable.
"""

from __future__ import annotations

from primer.query.comparison import ComparisonExpression
from primer.query.order import OrderBy


class Field:

    def __init__(self, path: str):

        self.path = path

    # ---------------------------------------------------------
    # Obtención de valores
    # ---------------------------------------------------------

    def get_value(self, obj):
        """
        Obtiene el valor del campo.

        Soporta rutas:

            name
            province.name
            geometry.x
        """

        value = obj

        for part in self.path.split("."):
            value = getattr(value, part)

        return value

    # Compatibilidad hacia atrás
    value = get_value

    # ---------------------------------------------------------
    # Comparaciones
    # ---------------------------------------------------------

    def __eq__(self, other):
        return ComparisonExpression(self, "==", other)

    def __ne__(self, other):
        return ComparisonExpression(self, "!=", other)

    def __lt__(self, other):
        return ComparisonExpression(self, "<", other)

    def __le__(self, other):
        return ComparisonExpression(self, "<=", other)

    def __gt__(self, other):
        return ComparisonExpression(self, ">", other)

    def __ge__(self, other):
        return ComparisonExpression(self, ">=", other)

    # ---------------------------------------------------------
    # Ordenación
    # ---------------------------------------------------------

    def asc(self):
        return OrderBy(self, True)

    def desc(self):
        return OrderBy(self, False)

    # ---------------------------------------------------------

    def __repr__(self):

        return f"Field({self.path!r})"