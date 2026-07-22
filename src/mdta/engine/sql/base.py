"""
MDTA - Base SQL Builder

Clase base para todos los motores SQL.

Implementa el algoritmo general de generación de SQL utilizando
el patrón Template Method. Las clases derivadas únicamente deben
implementar las partes específicas de cada motor.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from models import Field, Table, Schema

from .build_result import SQLBuildResult


class SQLBuilder(ABC):
    """
    Clase base para todos los generadores SQL.
    """

    # ==========================================================
    # API PÚBLICA
    # ==========================================================

    def build_table(self, table: Table) -> SQLBuildResult:
        """
        Genera todas las sentencias SQL necesarias para una tabla.
        """

        result = SQLBuildResult()

        columns = [
            self._build_column(field)
            for field in table
        ]

        constraints = self._build_table_constraints(table)

        result.create_table = self._build_create_table(
            table,
            columns,
            constraints,
        )

        result.indexes.extend(
            self._build_indexes(table)
        )

        result.triggers.extend(
            self._build_triggers(table)
        )

        result.views.extend(
            self._build_views(table)
        )

        result.comments.extend(
            self._build_comments(table)
        )

        result.metadata.extend(
            self._build_metadata(table)
        )

        return result

    # ----------------------------------------------------------

    def build_schema(self, schema: Schema) -> list[SQLBuildResult]:
        """
        Genera todas las tablas de un esquema.
        """

        return [
            self.build_table(table)
            for table in schema
        ]

    # ----------------------------------------------------------

    def build_database(
        self,
        schemas: list[Schema],
    ) -> list[SQLBuildResult]:
        """
        Genera todas las tablas de todos los esquemas.
        """

        results: list[SQLBuildResult] = []

        for schema in schemas:
            results.extend(
                self.build_schema(schema)
            )

        return results

    # ==========================================================
    # MÉTODOS ABSTRACTOS
    # ==========================================================

    @abstractmethod
    def _build_column(
        self,
        field: Field,
    ) -> str:
        """
        Genera la definición SQL de una columna.
        """
        raise NotImplementedError

    # ----------------------------------------------------------

    def _build_table_constraints(
        self,
        table: Table,
    ) -> list[str]:
        """
        Genera restricciones de tabla.

        Por defecto no genera ninguna.
        """

        return []

    # ----------------------------------------------------------

    @abstractmethod
    def _build_create_table(
        self,
        table: Table,
        columns: list[str],
        constraints: list[str],
    ) -> str:
        """
        Genera la sentencia CREATE TABLE.
        """
        raise NotImplementedError

    # ----------------------------------------------------------

    def _build_indexes(
        self,
        table: Table,
    ) -> list[str]:
        """
        Genera índices.
        """

        return []

    # ----------------------------------------------------------

    def _build_triggers(
        self,
        table: Table,
    ) -> list[str]:
        """
        Genera triggers.
        """

        return []

    # ----------------------------------------------------------

    def _build_views(
        self,
        table: Table,
    ) -> list[str]:
        """
        Genera vistas.
        """

        return []

    # ----------------------------------------------------------

    def _build_comments(
        self,
        table: Table,
    ) -> list[str]:
        """
        Genera comentarios del motor.
        """

        return []

    # ----------------------------------------------------------

    def _build_metadata(
        self,
        table: Table,
    ) -> list[str]:
        """
        Genera metadatos específicos del motor.
        """

        return []