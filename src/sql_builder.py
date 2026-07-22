"""
=========================================================
Andaltura Data Engine

SQL Builder

Genera las sentencias SQL a partir de los modelos del MDTA.
=========================================================
"""

from models import Table


class SQLBuilder:
    """
    Generador de SQL para SQLite.
    """

    @staticmethod
    def build(table: Table) -> list[str]:
        """
        Devuelve todas las sentencias SQL necesarias
        para crear una tabla.
        """

        sql = [
            SQLBuilder.create_table(table)
        ]

        sql.extend(SQLBuilder.create_indexes(table))

        return sql

    @staticmethod
    def create_table(table: Table) -> str:
        """
        Genera la sentencia CREATE TABLE.
        """

        columns = []

        for field in table.fields:

            columns.append(SQLBuilder.build_column(field))

        sql = f"""
CREATE TABLE IF NOT EXISTS {table.name} (
    {",\n    ".join(columns)}
);
"""

        return sql.strip()

    @staticmethod
    def create_indexes(table: Table) -> list[str]:
        """
        Genera todos los índices de una tabla.
        """

        indexes = []

        for field in table.fields:

            if not field.indexed:
                continue

            index_name = f"idx_{table.name}_{field.name}"

            sql = f"""
CREATE INDEX IF NOT EXISTS {index_name}
ON {table.name} ({field.name});
"""

            indexes.append(sql.strip())

        return indexes

    @staticmethod
    def build_column(field) -> str:
        """
        Genera la definición SQL de un campo.
        """

        parts = [

            field.name,

            field.datatype.value

        ]

        if field.primary_key:

            parts.append("PRIMARY KEY")

            if field.datatype.value == "INTEGER":
                parts.append("AUTOINCREMENT")

        if not field.nullable:
            parts.append("NOT NULL")

        if field.unique:
            parts.append("UNIQUE")

        if field.default is not None:

            if isinstance(field.default, str):
                parts.append(f"DEFAULT '{field.default}'")

            else:
                parts.append(f"DEFAULT {field.default}")

        if field.foreign_key:

            table_name, field_name = field.foreign_key.split(".")

            parts.append(
                f"REFERENCES {table_name}({field_name})"
            )

        return " ".join(parts)