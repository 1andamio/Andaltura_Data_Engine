"""
MDTA - Diccionario Maestro
Campos de Identidad

Este módulo define los campos básicos de identificación reutilizables
por cualquier entidad del modelo de datos.
"""

from models import Field
from mdta_types import DataType


# ------------------------------------------------------------------
# IDENTIFICADORES
# ------------------------------------------------------------------

ID = Field(
    name="id",
    datatype=DataType.INTEGER,
    primary_key=True,
    nullable=False,
    description="Identificador interno del registro."
)

UUID = Field(
    name="uuid",
    datatype=DataType.TEXT,
    unique=True,
    indexed=True,
    description="Identificador universal único."
)

CODIGO = Field(
    name="codigo",
    datatype=DataType.TEXT,
    indexed=True,
    description="Código interno o externo de la entidad."
)

CODIGO_INE = Field(
    name="codigo_ine",
    datatype=DataType.TEXT,
    unique=True,
    indexed=True,
    description="Código oficial del Instituto Nacional de Estadística."
)

SLUG = Field(
    name="slug",
    datatype=DataType.TEXT,
    nullable=False,
    unique=True,
    indexed=True,
    description="Identificador SEO utilizado en URLs."
)


# ------------------------------------------------------------------
# NOMBRES
# ------------------------------------------------------------------

NOMBRE = Field(
    name="nombre",
    datatype=DataType.TEXT,
    nullable=False,
    indexed=True,
    description="Nombre principal."
)

NOMBRE_OFICIAL = Field(
    name="nombre_oficial",
    datatype=DataType.TEXT,
    description="Nombre oficial completo."
)

NOMBRE_CORTO = Field(
    name="nombre_corto",
    datatype=DataType.TEXT,
    description="Nombre abreviado."
)

NOMBRE_ALTERNATIVO = Field(
    name="nombre_alternativo",
    datatype=DataType.TEXT,
    description="Otros nombres conocidos."
)


# ------------------------------------------------------------------
# DESCRIPCIÓN
# ------------------------------------------------------------------

DESCRIPCION = Field(
    name="descripcion",
    datatype=DataType.TEXT,
    description="Descripción general."
)

OBSERVACIONES = Field(
    name="observaciones",
    datatype=DataType.TEXT,
    description="Observaciones internas."
)

NOTAS = Field(
    name="notas",
    datatype=DataType.TEXT,
    description="Notas adicionales."
)


# ------------------------------------------------------------------
# ESTADO
# ------------------------------------------------------------------

ACTIVO = Field(
    name="activo",
    datatype=DataType.BOOLEAN,
    nullable=False,
    default=True,
    indexed=True,
    description="Indica si el registro está activo."
)

PUBLICADO = Field(
    name="publicado",
    datatype=DataType.BOOLEAN,
    nullable=False,
    default=False,
    indexed=True,
    description="Indica si el registro está publicado."
)