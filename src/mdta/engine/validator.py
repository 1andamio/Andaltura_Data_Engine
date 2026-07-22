"""
MDTA - Schema Validator
"""

from __future__ import annotations

from models import Table, Field


class ValidationError(Exception):
    """Error de validación del esquema."""
    pass


class Validator:

    # ==========================================================
    # Validación pública
    # ==========================================================

    def validate(self, table: Table) -> None:

        self._validate_duplicate_fields(table)

        self._validate_primary_keys(table)

        self._validate_geometry(table)

    # ==========================================================
    # Campos duplicados
    # ==========================================================

    def _validate_duplicate_fields(
        self,
        table: Table,
    ) -> None:

        seen = set()

        for field in table:

            if field.name in seen:

                raise ValidationError(
                    f"Campo duplicado: {field.name}"
                )

            seen.add(field.name)

    # ==========================================================
    # Primary Keys
    # ==========================================================

    def _validate_primary_keys(
        self,
        table: Table,
    ) -> None:

        primary_keys = [

            field

            for field in table

            if field.primary_key

        ]

        if len(primary_keys) > 1:

            raise ValidationError(
                "Solo puede existir una Primary Key."
            )

    # ==========================================================
    # Geometría
    # ==========================================================

    def _validate_geometry(
        self,
        table: Table,
    ) -> None:

        for field in table:

            if field.geometry_type is None:

                continue

            if field.srid is None:

                raise ValidationError(
                    f"{field.name}: falta SRID."
                )