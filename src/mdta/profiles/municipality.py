"""
MDTA - Municipality Profile

Perfil base reutilizable para municipios.
"""

from dictionary.groups import FieldGroups


class MunicipalityProfile:

    @staticmethod
    def fields():

        return [

            # -----------------------------
            # Identidad
            # -----------------------------
            *FieldGroups.identity(),

            # -----------------------------
            # Organización territorial
            # -----------------------------
            *FieldGroups.administrative(),

            # -----------------------------
            # Información geográfica
            # -----------------------------
            *FieldGroups.polygon(),

            # -----------------------------
            # Información demográfica
            # -----------------------------
            *FieldGroups.demography(),

            # -----------------------------
            # Auditoría
            # -----------------------------
            *FieldGroups.audit(),

            # -----------------------------
            # Ciclo de vida
            # -----------------------------
            *FieldGroups.lifecycle(),

        ]