"""
MDTA - Diccionario Maestro
Campos Administrativos

Campos reutilizables relacionados con la organización territorial
y administrativa.
"""

from models import Field
from mdta_types import DataType


# ==========================================================
# IDENTIFICADORES TERRITORIALES
# ==========================================================

PAIS_ID = Field(
    name="pais_id",
    datatype=DataType.INTEGER,
    indexed=True,
    description="Identificador del país."
)

COMUNIDAD_AUTONOMA_ID = Field(
    name="comunidad_autonoma_id",
    datatype=DataType.INTEGER,
    indexed=True,
    description="Identificador de la comunidad autónoma."
)

PROVINCIA_ID = Field(
    name="provincia_id",
    datatype=DataType.INTEGER,
    indexed=True,
    description="Identificador de la provincia."
)

COMARCA_ID = Field(
    name="comarca_id",
    datatype=DataType.INTEGER,
    indexed=True,
    description="Identificador de la comarca."
)

MUNICIPIO_ID = Field(
    name="municipio_id",
    datatype=DataType.INTEGER,
    indexed=True,
    description="Identificador del municipio."
)

NUCLEO_ID = Field(
    name="nucleo_id",
    datatype=DataType.INTEGER,
    indexed=True,
    description="Identificador del núcleo de población."
)

DISSEMINADO_ID = Field(
    name="diseminado_id",
    datatype=DataType.INTEGER,
    indexed=True,
    description="Identificador del diseminado."
)


# ==========================================================
# CÓDIGOS OFICIALES
# ==========================================================

CODIGO_POSTAL = Field(
    name="codigo_postal",
    datatype=DataType.TEXT,
    indexed=True,
    description="Código postal."
)

CODIGO_CATASTRAL = Field(
    name="codigo_catastral",
    datatype=DataType.TEXT,
    indexed=True,
    description="Referencia o código catastral."
)

CODIGO_NOMENCLATOR = Field(
    name="codigo_nomenclator",
    datatype=DataType.TEXT,
    indexed=True,
    description="Código del Nomenclátor oficial."
)

CODIGO_EUROSTAT = Field(
    name="codigo_eurostat",
    datatype=DataType.TEXT,
    indexed=True,
    description="Código estadístico europeo."
)


# ==========================================================
# JERARQUÍA ADMINISTRATIVA
# ==========================================================

CAPITAL = Field(
    name="capital",
    datatype=DataType.BOOLEAN,
    default=False,
    description="Indica si la entidad es capital administrativa."
)

NIVEL_ADMINISTRATIVO = Field(
    name="nivel_administrativo",
    datatype=DataType.INTEGER,
    description="Nivel jerárquico dentro del sistema territorial."
)

ORDEN_ADMINISTRATIVO = Field(
    name="orden_administrativo",
    datatype=DataType.INTEGER,
    description="Orden de representación."
)


# ==========================================================
# DEPENDENCIAS
# ==========================================================

PADRE_ID = Field(
    name="padre_id",
    datatype=DataType.INTEGER,
    indexed=True,
    description="Entidad administrativa superior."
)

RAIZ_ID = Field(
    name="raiz_id",
    datatype=DataType.INTEGER,
    indexed=True,
    description="Entidad raíz del árbol administrativo."
)


# ==========================================================
# ORGANISMOS
# ==========================================================

ORGANISMO_COMPETENTE = Field(
    name="organismo_competente",
    datatype=DataType.TEXT,
    description="Administración competente."
)

ORGANISMO_GESTOR = Field(
    name="organismo_gestor",
    datatype=DataType.TEXT,
    description="Entidad gestora."
)