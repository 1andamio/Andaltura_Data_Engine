"""
MDTA - Database Engine

Motor de acceso a base de datos.

No conoce la estructura de las tablas ni genera SQL.
Su única responsabilidad es ejecutar consultas y gestionar
la conexión.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any


class Database:

    def __init__(self, database: str | Path):

        self.database = Path(database)

        self.connection: sqlite3.Connection | None = None

    # ---------------------------------------------------------
    # Conexión
    # ---------------------------------------------------------

    def connect(self) -> sqlite3.Connection:

        if self.connection is None:

            self.connection = sqlite3.connect(self.database)

            self.connection.row_factory = sqlite3.Row

            self.connection.execute("PRAGMA foreign_keys = ON")

        return self.connection

    # ---------------------------------------------------------

    def close(self) -> None:

        if self.connection is not None:

            self.connection.close()

            self.connection = None

    # ---------------------------------------------------------
    # Transacciones
    # ---------------------------------------------------------

    def commit(self) -> None:

        self.connect().commit()

    # ---------------------------------------------------------

    def rollback(self) -> None:

        self.connect().rollback()

    # ---------------------------------------------------------
    # Ejecución
    # ---------------------------------------------------------

    def execute(
        self,
        sql: str,
        parameters: tuple[Any, ...] = (),
    ) -> sqlite3.Cursor:

        cursor = self.connect().cursor()

        cursor.execute(sql, parameters)

        return cursor

    # ---------------------------------------------------------

    def executemany(
        self,
        sql: str,
        rows: list[tuple],
    ) -> sqlite3.Cursor:

        cursor = self.connect().cursor()

        cursor.executemany(sql, rows)

        return cursor

    # ---------------------------------------------------------

    def executescript(self, script: str) -> None:

        self.connect().executescript(script)

    # ---------------------------------------------------------
    # Consultas
    # ---------------------------------------------------------

    def fetchone(
        self,
        sql: str,
        parameters: tuple[Any, ...] = (),
    ) -> sqlite3.Row | None:

        return self.execute(sql, parameters).fetchone()

    # ---------------------------------------------------------

    def fetchall(
        self,
        sql: str,
        parameters: tuple[Any, ...] = (),
    ) -> list[sqlite3.Row]:

        return self.execute(sql, parameters).fetchall()

    # ---------------------------------------------------------
    # Utilidades
    # ---------------------------------------------------------

    def table_exists(self, table_name: str) -> bool:

        row = self.fetchone(
            """
            SELECT name
            FROM sqlite_master
            WHERE type='table'
            AND name=?
            """,
            (table_name,),
        )

        return row is not None

    # ---------------------------------------------------------

    def drop_table(self, table_name: str) -> None:

        self.execute(
            f'DROP TABLE IF EXISTS "{table_name}"'
        )

    # ---------------------------------------------------------

    def vacuum(self) -> None:

        self.execute("VACUUM")

    # ---------------------------------------------------------

    def optimize(self) -> None:

        self.execute("PRAGMA optimize")

    # ---------------------------------------------------------
    # Context Manager
    # ---------------------------------------------------------

    def __enter__(self):

        self.connect()

        return self

    # ---------------------------------------------------------

    def __exit__(self, exc_type, exc, tb):

        if exc is None:

            self.commit()

        else:

            self.rollback()

        self.close()