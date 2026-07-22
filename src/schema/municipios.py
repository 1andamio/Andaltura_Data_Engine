"""
MDTA - Esquema de Municipios
"""

from models import Table

from profiles.municipality import MunicipalityProfile

from dictionary.administrative import Administrative
from dictionary.geography import Geography
from dictionary.demography import Demography


class MunicipiosSchema:

    @staticmethod
    def table() -> Table:

        table = Table(
            name="municipios",
            description="Catálogo oficial de municipios.",
            fields=MunicipalityProfile.fields(),
        )

        # ------------------------------------------------------
        # Campos específicos de municipios
        # ------------------------------------------------------

        table.add_fields([

            Administrative.CODIGO_INE.clone(),

            Administrative.CODIGO_POSTAL.clone(),

            Geography.ALTITUD_MEDIA.clone(),

            Demography.POBLACION_2025.clone(),

        ])

        return table