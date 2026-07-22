"""
=========================================================
Andaltura Data Engine

Campos administrativos
=========================================================
"""

from models import Field
from mdta_types import DataType


def codigo_ine() -> Field:
    return Field(
        name="codigo_ine",
        datatype=DataType.TEXT,
        nullable=False,
        unique=True,
        indexed=True,
        description="Código oficial INE"
    )


def codigo_iso() -> Field:
    return Field(
        name="codigo_iso",
        datatype=DataType.TEXT,
        unique=True,
        indexed=True,
        description="Código ISO"
    )


def provincia_id() -> Field:
    return Field(
        name="provincia_id",
        datatype=DataType.INTEGER,
        nullable=False,
        indexed=True,
        foreign_key="provincias(id)",
        description="Provincia"
    )


def municipio_id() -> Field:
    return Field(
        name="municipio_id",
        datatype=DataType.INTEGER,
        nullable=False,
        indexed=True,
        foreign_key="municipios(id)",
        description="Municipio"
    )


def comarca_id() -> Field:
    return Field(
        name="comarca_id",
        datatype=DataType.INTEGER,
        indexed=True,
        foreign_key="comarcas(id)",
        description="Comarca"
    )