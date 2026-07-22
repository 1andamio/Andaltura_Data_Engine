"""
MDTA - SQLite Builder
"""

from __future__ import annotations

from models import Field
from mdta_types import DataType

from .base import SQLBuilder


class SQLiteBuilder(SQLBuilder):

    TYPE_MAPPING = {
        DataType.INTEGER: "INTEGER",
        DataType.FLOAT: "REAL",
        DataType.TEXT: "TEXT",
        DataType.BOOLEAN: "INTEGER",
        DataType.DATE: "TEXT",
        DataType.TIME: "TEXT",
        DataType.DATETIME: "TEXT",
        DataType.UUID: "TEXT",
        DataType.JSON: "TEXT",
        DataType.BLOB: "BLOB",
    }

    # ---------------------------------------------------------

    def _sql_type(self, field: Field) -> str:

        if field.datatype == DataType.DECIMAL:

            precision = field.precision or 18
            scale = field.scale or 6

            return f"NUMERIC({precision},{scale})"

        if field.datatype == DataType.GEOMETRY:

            return "BLOB"

        return self.TYPE_MAPPING[field.datatype]

        # ==========================================================
# FRAGMENTOS SQL
# ==========================================================

def _nullable_sql(self, field: Field) -> str:

    return "" if field.nullable else "NOT NULL"


# ----------------------------------------------------------


def _unique_sql(self, field: Field) -> str:

    return "UNIQUE" if field.unique else ""


# ----------------------------------------------------------


def _check_sql(self, field: Field) -> str:

    if field.check:

        return f"CHECK ({field.check})"

    return ""


# ----------------------------------------------------------


def _default_sql(self, field: Field) -> str:

    if field.default is None:

        return ""

    value = field.default

    if isinstance(value, bool):

        return f"DEFAULT {int(value)}"

    if isinstance(value, (int, float)):

        return f"DEFAULT {value}"

    value = str(value)

    upper = value.upper()

    if upper in {

        "CURRENT_DATE",

        "CURRENT_TIME",

        "CURRENT_TIMESTAMP",

        "NULL",

    }:

        return f"DEFAULT {upper}"

    escaped = value.replace("'", "''")

    return f"DEFAULT '{escaped}'"