"""
=========================================================
Andaltura Data Engine

MDTA - Esquema de Provincias
=========================================================
"""

from mdta_types import DataType
from models import Field, Table


PROVINCIAS = Table(

    name="provincias",

    description="Provincias de Andalucía",

    fields=[

        Field(
            name="id",
            datatype=DataType.INTEGER,
            primary_key=True,
            nullable=False,
            description="Identificador interno"
        ),

        Field(
            name="codigo_ine",
            datatype=DataType.TEXT,
            nullable=False,
            unique=True,
            indexed=True,
            description="Código oficial INE"
        ),

        Field(
            name="nombre",
            datatype=DataType.TEXT,
            nullable=False,
            indexed=True,
            description="Nombre oficial"
        ),

        Field(
            name="slug",
            datatype=DataType.TEXT,
            nullable=False,
            unique=True,
            indexed=True,
            description="Slug SEO"
        ),

        Field(
            name="capital",
            datatype=DataType.TEXT,
            description="Capital provincial"
        ),

        Field(
            name="superficie_km2",
            datatype=DataType.REAL,
            description="Superficie en km²"
        ),

        Field(
            name="poblacion",
            datatype=DataType.INTEGER,
            description="Población total"
        ),

        Field(
            name="created_at",
            datatype=DataType.DATETIME,
            description="Fecha de creación"
        ),

        Field(
            name="updated_at",
            datatype=DataType.DATETIME,
            description="Última actualización"
        )

    ]

)