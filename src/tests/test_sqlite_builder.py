"""
tests/test_sqlite_builder.py

Batería inicial de pruebas para SQLiteBuilder del MDTA.
"""

import pytest

from mdta_types import DataType
from models import Field, Table
from engine.sql.sqlite import SQLiteBuilder


@pytest.fixture
def builder():
    return SQLiteBuilder()


class TestColumnGeneration:

    @pytest.mark.parametrize(
        "datatype,expected",
        [
            (DataType.INTEGER, "INTEGER"),
            (DataType.FLOAT, "REAL"),
            (DataType.TEXT, "TEXT"),
            (DataType.BOOLEAN, "INTEGER"),
            (DataType.DATE, "TEXT"),
            (DataType.TIME, "TEXT"),
            (DataType.DATETIME, "TEXT"),
            (DataType.UUID, "TEXT"),
            (DataType.JSON, "TEXT"),
            (DataType.BLOB, "BLOB"),
        ],
    )
    def test_simple_types(self, builder, datatype, expected):
        field = Field("value", datatype)
        assert expected in builder._build_column(field)

    def test_decimal(self, builder):
        field = Field("amount", DataType.DECIMAL, precision=12, scale=3)
        assert "NUMERIC(12,3)" in builder._build_column(field)

    def test_geometry(self, builder):
        assert "BLOB" in builder._build_column(Field("geom", DataType.GEOMETRY))

    def test_primary_key(self, builder):
        assert "PRIMARY KEY" in builder._build_column(Field("id", DataType.INTEGER, primary_key=True))

    def test_not_null(self, builder):
        assert "NOT NULL" in builder._build_column(Field("name", DataType.TEXT, nullable=False))

    def test_unique(self, builder):
        assert "UNIQUE" in builder._build_column(Field("code", DataType.TEXT, unique=True))

    def test_default(self, builder):
        assert "DEFAULT 1" in builder._build_column(Field("enabled", DataType.BOOLEAN, default=True))

    def test_check(self, builder):
        assert "CHECK (age>=0)" in builder._build_column(Field("age", DataType.INTEGER, check="age>=0"))


class TestCreateTable:

    def test_create_table(self, builder):
        table = Table("municipios", [Field("id", DataType.INTEGER, primary_key=True)])
        result = builder.build_table(table)
        assert "CREATE TABLE IF NOT EXISTS municipios" in result.create_table

    def test_index_generation(self, builder):
        table = Table("municipios", [
            Field("id", DataType.INTEGER, primary_key=True),
            Field("name", DataType.TEXT, indexed=True)
        ])
        result = builder.build_table(table)
        assert len(result.indexes) == 1

    def test_script(self, builder):
        table = Table("municipios", [
            Field("id", DataType.INTEGER, primary_key=True),
            Field("name", DataType.TEXT, indexed=True)
        ])
        script = builder.build_table(table).script
        assert "CREATE TABLE" in script
        assert "CREATE INDEX" in script
