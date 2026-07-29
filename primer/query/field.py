"""
Representa un campo consultable.
"""

from __future__ import annotations


class Field:

    def __init__(self, path: str):

        self.path = path

    def get_value(self, obj):
        """
        Obtiene el valor del campo sobre un objeto.

        Soporta rutas como:

            name
            province.name
            geometry.x
        """

        value = obj

        for part in self.path.split("."):
            value = getattr(value, part)

        return value

    def __repr__(self):

        return f"Field({self.path!r})"