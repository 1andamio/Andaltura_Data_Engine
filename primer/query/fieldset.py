"""
Conjunto de campos utilizados en una consulta.
"""

from __future__ import annotations

from primer.query.field import Field


class FieldSet:
    """
    Representa una colección ordenada de campos.
    """

    def __init__(self, *fields):

        self._fields = []

        for field in fields:

            if isinstance(field, str):
                field = Field(field)

            if not isinstance(field, Field):
                raise TypeError(
                    "FieldSet only accepts Field or str instances."
                )

            self._fields.append(field)

    def __iter__(self):
        return iter(self._fields)

    def __len__(self):
        return len(self._fields)

    def __getitem__(self, index):
        return self._fields[index]

    def names(self):
        """
        Devuelve los nombres de todos los campos.
        """
        return [field.path for field in self._fields]

    def add(self, field):

        if isinstance(field, str):
            field = Field(field)

        self._fields.append(field)

    def __contains__(self, field):

        if isinstance(field, str):
            return field in self.names()

        return field in self._fields

    def __repr__(self):

        names = ", ".join(self.names())

        return f"FieldSet({names})"