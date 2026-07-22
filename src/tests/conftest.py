
"""
tests/conftest.py

Fixtures compartidas para todas las pruebas del MDTA.
"""

import pytest

from mdta_types import DataType, GeometryType
from models import Field, Table, Schema
from engine.sql.sqlite import SQLiteBuilder


# ==========================================================
# BUILDERS
# ==========================================================

@pytest.fixture
def builder():
    return SQLiteBuilder()


# ==========================================================
# FIELDS
# ==========================================================

@pytest.fixture
def field_integer():
    return Field("id", DataType.INTEGER)


@pytest.fixture
def field_text():
    return Field("name", DataType.TEXT)


@pytest.fixture
def field_decimal():
    return Field(
        "amount",
        DataType.DECIMAL,
        precision=12,
        scale=2,
    )


@pytest.fixture
def field_geometry():
    return Field(
        "geom",
        DataType.GEOMETRY,
        geometry_type=GeometryType.POLYGON,
        srid=25830,
    )


@pytest.fixture
def field_pk():
    return Field(
        "id",
        DataType.INTEGER,
        primary_key=True,
        nullable=False,
    )


@pytest.fixture
def field_fk():
    return Field(
        "province_id",
        DataType.INTEGER,
        foreign_table="province",
        foreign_field="id",
    )


# ==========================================================
# TABLES
# ==========================================================

@pytest.fixture
def table_empty():
    return Table("empty", [])


@pytest.fixture
def table_municipios(field_pk, field_text):
    return Table(
        "municipios",
        [
            field_pk,
            field_text,
        ],
    )


@pytest.fixture
def table_provincias(field_pk):
    return Table(
        "provincias",
        [
            field_pk,
            Field("nombre", DataType.TEXT),
        ],
    )


# ==========================================================
# SCHEMAS
# ==========================================================

@pytest.fixture
def schema_test(table_municipios, table_provincias):
    return Schema(
        "territorio",
        [
            table_municipios,
            table_provincias,
        ],
    )
