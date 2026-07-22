"""
MDTA - Province Profile

Perfil estándar para una provincia.
"""

from dictionary.groups import FieldGroups


class ProvinceProfile:

    @staticmethod
    def fields():

        return [

            # -----------------------------
            # Identidad
            # -----------------------------
            *FieldGroups.identity(),

            # -----------------------------
            # Administración
            # -----------------------------
            *FieldGroups.administrative(),

            # -----------------------------
            # Geometría
            # -----------------------------
            *FieldGroups.polygon(),

            # -----------------------------
            # Demografía
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