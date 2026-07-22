"""
tests/test_models.py

Pruebas unitarias para los modelos fundamentales del MDTA.

Ejecutar:
    pytest tests/test_models.py -v
"""

import pytest

from models import Field, Table, Schema
from mdta_types import DataType, GeometryType


class TestField:

    def test_create_minimal_field(self):
        field = Field(name="id", datatype=DataType.INTEGER)

        assert field.name == "id"
        assert field.datatype == DataType.INTEGER
        assert field.nullable is True
        assert field.primary_key is False

    def test_create_complete_field(self):
        field = Field(
            name="geom",
            datatype=DataType.GEOMETRY,
            nullable=False,
            unique=True,
            indexed=True,
            geometry_type=GeometryType.POLYGON,
            srid=25830,
        )

        assert field.is_geometry
        assert field.unique
        assert field.indexed
        assert field.srid == 25830

    def test_clone(self):
        original = Field("name", DataType.TEXT)
        clone = original.clone(name="title")

        assert original.name == "name"
        assert clone.name == "title"
        assert clone.datatype == DataType.TEXT

    def test_is_numeric(self):
        assert Field("n", DataType.INTEGER).is_numeric
        assert not Field("t", DataType.TEXT).is_numeric

    def test_is_foreign_key(self):
        field = Field(
            "province_id",
            DataType.INTEGER,
            foreign_table="province",
            foreign_field="id",
        )

        assert field.is_foreign_key


class TestTable:

    def test_add_and_get_field(self):
        table = Table("municipios", [])

        field = Field("id", DataType.INTEGER)

        table.add_field(field)

        assert table.has_field("id")
        assert table.get_field("id") is field

    def test_remove_field(self):
        table = Table(
            "municipios",
            [
                Field("id", DataType.INTEGER),
                Field("name", DataType.TEXT),
            ],
        )

        table.remove_field("name")

        assert not table.has_field("name")
        assert len(table) == 1

    def test_primary_key(self):
        table = Table(
            "municipios",
            [
                Field("id", DataType.INTEGER, primary_key=True),
                Field("name", DataType.TEXT),
            ],
        )

        assert table.primary_key_field().name == "id"


class TestSchema:

    def test_add_and_get_table(self):
        schema = Schema("territorio", [])

        table = Table("municipios", [])

        schema.add_table(table)

        assert schema.has_table("municipios")
        assert schema.get_table("municipios") is table

    def test_remove_table(self):
        schema = Schema(
            "territorio",
            [
                Table("municipios", []),
                Table("provincias", []),
            ],
        )

        schema.remove_table("municipios")

        assert not schema.has_table("municipios")
        assert len(schema) == 1
