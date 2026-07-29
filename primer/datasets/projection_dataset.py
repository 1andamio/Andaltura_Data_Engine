"""
Dataset que contiene filas proyectadas (Row).
"""

from __future__ import annotations

from primer.datasets.base import BaseDataset


class ProjectionDataset(BaseDataset):
    """
    Representa el resultado de una proyección (SELECT).
    """

    def columns(self):
        """
        Devuelve los nombres de las columnas de la proyección.
        """

        if not self:
            return []

        return list(self.first().keys())

    def to_dicts(self):
        """
        Convierte todas las filas en diccionarios.
        """

        return [
            row.to_dict()
            for row in self
        ]

    def __repr__(self):

        return (
            f"ProjectionDataset(rows={len(self)})"
        )