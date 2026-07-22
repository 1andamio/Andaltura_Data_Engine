"""
MDTA - Diccionario Maestro
Campos Demográficos
"""

from models import Field
from mdta_types import DataType


class Demography:

    # ==========================================================
    # POBLACIÓN
    # ==========================================================

    POBLACION_TOTAL = Field(
        name="poblacion_total",
        datatype=DataType.INTEGER,
        description="Población total."
    )

    POBLACION_HOMBRES = Field(
        name="poblacion_hombres",
        datatype=DataType.INTEGER,
        description="Población masculina."
    )

    POBLACION_MUJERES = Field(
        name="poblacion_mujeres",
        datatype=DataType.INTEGER,
        description="Población femenina."
    )

    HOGARES = Field(
        name="hogares",
        datatype=DataType.INTEGER,
        description="Número de hogares."
    )

    FAMILIAS = Field(
        name="familias",
        datatype=DataType.INTEGER,
        description="Número de familias."
    )

    DENSIDAD = Field(
        name="densidad_hab_km2",
        datatype=DataType.REAL,
        description="Habitantes por km²."
    )

    # ==========================================================
    # EVOLUCIÓN
    # ==========================================================

    POBLACION_1900 = Field(
        name="poblacion_1900",
        datatype=DataType.INTEGER,
        description="Población en 1900."
    )

    POBLACION_1950 = Field(
        name="poblacion_1950",
        datatype=DataType.INTEGER,
        description="Población en 1950."
    )

    POBLACION_2000 = Field(
        name="poblacion_2000",
        datatype=DataType.INTEGER,
        description="Población en 2000."
    )

    POBLACION_2010 = Field(
        name="poblacion_2010",
        datatype=DataType.INTEGER,
        description="Población en 2010."
    )

    POBLACION_2020 = Field(
        name="poblacion_2020",
        datatype=DataType.INTEGER,
        description="Población en 2020."
    )

    POBLACION_2025 = Field(
        name="poblacion_2025",
        datatype=DataType.INTEGER,
        description="Población en 2025."
    )

    # ==========================================================
    # VARIACIONES
    # ==========================================================

    CRECIMIENTO_ABSOLUTO = Field(
        name="crecimiento_absoluto",
        datatype=DataType.INTEGER,
        description="Incremento absoluto de población."
    )

    CRECIMIENTO_PORCENTUAL = Field(
        name="crecimiento_porcentual",
        datatype=DataType.REAL,
        description="Incremento porcentual."
    )

    SALDO_MIGRATORIO = Field(
        name="saldo_migratorio",
        datatype=DataType.INTEGER,
        description="Saldo migratorio."
    )

    SALDO_NATURAL = Field(
        name="saldo_natural",
        datatype=DataType.INTEGER,
        description="Saldo vegetativo."
    )

    # ==========================================================
    # ESTRUCTURA
    # ==========================================================

    EDAD_MEDIA = Field(
        name="edad_media",
        datatype=DataType.REAL,
        description="Edad media."
    )

    INDICE_ENVEJECIMIENTO = Field(
        name="indice_envejecimiento",
        datatype=DataType.REAL,
        description="Índice de envejecimiento."
    )

    TASA_NATALIDAD = Field(
        name="tasa_natalidad",
        datatype=DataType.REAL,
        description="Tasa de natalidad."
    )

    TASA_MORTALIDAD = Field(
        name="tasa_mortalidad",
        datatype=DataType.REAL,
        description="Tasa de mortalidad."
    )

    ESPERANZA_VIDA = Field(
        name="esperanza_vida",
        datatype=DataType.REAL,
        description="Esperanza de vida."
    )

    # ==========================================================
    # FECHA
    # ==========================================================

    ANIO_REFERENCIA = Field(
        name="anio_referencia",
        datatype=DataType.INTEGER,
        indexed=True,
        description="Año de referencia de los datos."
    )

    FUENTE_DEMOGRAFICA = Field(
        name="fuente_demografica",
        datatype=DataType.TEXT,
        description="Fuente estadística."
    )