"""
Representa una fila resultado de una consulta.
"""

from __future__ import annotations


class Row:
    """
    Fila genérica devuelta por una proyección.
    """

    def __init__(self, **values):
        self._values = values

    def get(self, name, default=None):
        return self._values.get(name, default)

    def to_dict(self):
        return dict(self._values)

    def keys(self):
        return self._values.keys()

    def values(self):
        return self._values.values()

    def items(self):
        return self._values.items()

    def __getitem__(self, name):
        return self._values[name]

    def __getattr__(self, name):

        try:
            return self._values[name]
        except KeyError:
            raise AttributeError(name)

    def __contains__(self, name):
        return name in self._values

    def __len__(self):
        return len(self._values)

    def __iter__(self):
        return iter(self._values.items())

    def __repr__(self):

        values = ", ".join(
            f"{k}={v!r}"
            for k, v in self._values.items()
        )

        return f"Row({values})"