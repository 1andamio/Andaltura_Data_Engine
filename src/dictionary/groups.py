"""
MDTA - Grupos de Campos

Agrupa campos reutilizables del Diccionario Maestro para construir
esquemas de tablas de forma consistente.
"""

from dictionary.identity import Identity
from dictionary.administrative import Administrative
from dictionary.geography import Geography
from dictionary.demography import Demography
from dictionary.audit import Audit
from dictionary.lifecycle import Lifecycle


class FieldGroups:

    # ==========================================================
    # IDENTIDAD
    # ==========================================================

    @staticmethod
    def identity():

        return [

            Identity.ID.clone(),
            Identity.UUID.clone(),
            Identity.NOMBRE.clone(),
            Identity.SLUG.clone(),

        ]

    # ==========================================================
    # ADMINISTRACIÓN
    # ==========================================================

    @staticmethod
    def administrative():

        return [

            Administrative.PAIS_ID.clone(),
            Administrative.COMUNIDAD_AUTONOMA_ID.clone(),
            Administrative.PROVINCIA_ID.clone(),
            Administrative.COMARCA_ID.clone(),
            Administrative.MUNICIPIO_ID.clone(),

        ]

    # ==========================================================
    # GEOMETRÍA PUNTUAL
    # ==========================================================

    @staticmethod
    def point():

        return [

            Geography.POINT.clone(),
            Geography.LATITUD.clone(),
            Geography.LONGITUD.clone(),
            Geography.SRID.clone(),

        ]

    # ==========================================================
    # GEOMETRÍA POLIGONAL
    # ==========================================================

    @staticmethod
    def polygon():

        return [

            Geography.MULTIPOLYGON.clone(),

            Geography.SUPERFICIE_KM2.clone(),
            Geography.PERIMETRO_KM.clone(),

            Geography.CENTROIDE_LAT.clone(),
            Geography.CENTROIDE_LON.clone(),

            Geography.SRID.clone(),

        ]

    # ==========================================================
    # DEMOGRAFÍA
    # ==========================================================

    @staticmethod
    def demography():

        return [

            Demography.POBLACION_TOTAL.clone(),
            Demography.DENSIDAD.clone(),
            Demography.ANIO_REFERENCIA.clone(),

        ]

    # ==========================================================
    # AUDITORÍA
    # ==========================================================

    @staticmethod
    def audit():

        return [

            Audit.CREATED_AT.clone(),
            Audit.UPDATED_AT.clone(),

            Audit.VERSION.clone(),

            Audit.SOURCE.clone(),
            Audit.IMPORT_DATE.clone(),

        ]

    # ==========================================================
    # CICLO DE VIDA
    # ==========================================================

    @staticmethod
    def lifecycle():

        return [

            Lifecycle.STATUS.clone(),
            Lifecycle.ACTIVE.clone(),
            Lifecycle.VISIBLE.clone(),
            Lifecycle.PUBLISHED.clone(),

        ]