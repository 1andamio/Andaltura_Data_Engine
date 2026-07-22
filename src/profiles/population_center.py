"""
MDTA - Population Center Dictionary

Campos específicos para núcleos de población.
"""

from models import Field
from mdta_types import DataType


class PopulationCenter:

    # =====================================================
    # Identificación
    # =====================================================

    CODIGO_NOMENCLATOR = Field(
        name="codigo_nomenclator",
        datatype=DataType.TEXT,
        indexed=True,
        description="Código oficial del Nomenclátor."
    )

    CODIGO_ENTIDAD = Field(
        name="codigo_entidad",
        datatype=DataType.TEXT,
        indexed=True,
        description="Código de la entidad singular."
    )

    CODIGO_NUCLEO = Field(
        name="codigo_nucleo",
        datatype=DataType.TEXT,
        description="Código interno del núcleo."
    )

    # =====================================================
    # Clasificación
    # =====================================================

    TIPO_NUCLEO = Field(
        name="tipo_nucleo",
        datatype=DataType.TEXT,
        indexed=True,
        description="Tipo de núcleo de población."
    )

    CATEGORIA = Field(
        name="categoria",
        datatype=DataType.TEXT,
        indexed=True,
        description="Categoría administrativa."
    )

    ES_CAPITAL_MUNICIPAL = Field(
        name="es_capital_municipal",
        datatype=DataType.BOOLEAN,
        default=False,
        indexed=True,
        description="Indica si es la capital del municipio."
    )

    ES_DISSEMINADO = Field(
        name="es_diseminado",
        datatype=DataType.BOOLEAN,
        default=False,
        indexed=True,
        description="Indica si corresponde a población diseminada."
    )

    # =====================================================
    # Población
    # =====================================================

    POBLACION_RESIDENTE = Field(
        name="poblacion_residente",
        datatype=DataType.INTEGER,
        description="Población residente."
    )

    POBLACION_ESTACIONAL = Field(
        name="poblacion_estacional",
        datatype=DataType.INTEGER,
        description="Población estacional."
    )

    NUMERO_VIVIENDAS = Field(
        name="numero_viviendas",
        datatype=DataType.INTEGER,
        description="Número de viviendas."
    )

    # =====================================================
    # Localización
    # =====================================================

    CODIGO_POSTAL = Field(
        name="codigo_postal",
        datatype=DataType.TEXT,
        indexed=True,
        description="Código postal."
    )

    ALTITUD = Field(
        name="altitud",
        datatype=DataType.FLOAT,
        description="Altitud media."
    )

    DISTANCIA_CAPITAL = Field(
        name="distancia_capital",
        datatype=DataType.FLOAT,
        description="Distancia a la capital municipal."
    )

    # =====================================================
    # Estado
    # =====================================================

    HABITADO = Field(
        name="habitado",
        datatype=DataType.BOOLEAN,
        default=True,
        indexed=True,
        description="Indica si el núcleo está habitado."
    )

    FECHA_REFERENCIA = Field(
        name="fecha_referencia",
        datatype=DataType.DATE,
        description="Fecha de referencia de los datos."
    )

    FUENTE = Field(
        name="fuente",
        datatype=DataType.TEXT,
        description="Fuente oficial de los datos."
    )