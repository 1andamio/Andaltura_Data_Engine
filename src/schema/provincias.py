"""
MDTA - Esquema de Provincias
"""

from models import Table
from profiles.province import ProvinceProfile


class ProvinciasSchema:

    @staticmethod
    def table() -> Table:
        """
        Devuelve la definición de la tabla de provincias.
        """

        return Table(
            name="provincias",
            description="Catálogo de provincias.",
            fields=ProvinceProfile.fields(),
        )