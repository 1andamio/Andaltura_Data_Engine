"""
=========================================================
Andaltura Data Engine

Validador del esquema MDTA
=========================================================
"""

from models import Table


class SchemaValidator:
    """
    Valida la definición de las tablas antes de generar SQL.
    """

    @staticmethod
    def validate_table(table: Table) -> None:

        field_names = set()

        primary_keys = 0

        for field in table.fields:

            # No permitir nombres duplicados
            if field.name in field_names:
                raise ValueError(
                    f"La tabla '{table.name}' tiene el campo duplicado '{field.name}'."
                )

            field_names.add(field.name)

            # Solo puede haber una PK
            if field.primary_key:

                primary_keys += 1

                if field.nullable:
                    raise ValueError(
                        f"La clave primaria '{field.name}' no puede ser NULL."
                    )

        if primary_keys == 0:
            raise ValueError(
                f"La tabla '{table.name}' no tiene clave primaria."
            )

        if primary_keys > 1:
            raise ValueError(
                f"La tabla '{table.name}' tiene varias claves primarias."
            )