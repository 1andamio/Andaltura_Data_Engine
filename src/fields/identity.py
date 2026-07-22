"""
=========================================================
Andaltura Data Engine

Campos de identidad
=========================================================
"""

from models import Field
from mdta_types import DataType


def id() -> Field:
    """
    Identificador interno.
    """
    return Field(
        name="id",
        datatype=DataType.INTEGER,
        primary_key=True,
        nullable=False,
        description="Identificador interno"
    )


def nombre() -> Field:
    """
    Nombre oficial.
    """
    return Field(
        name="nombre",
        datatype=DataType.TEXT,
        nullable=False,
        indexed=True,
        description="Nombre oficial"
    )


def slug() -> Field:
    """
    Slug SEO.
    """
    return Field(
        name="slug",
        datatype=DataType.TEXT,
        nullable=False,
        unique=True,
        indexed=True,
        description="Slug SEO"
    )