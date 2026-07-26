"""
Catálogo SQLite para Primer.

Este módulo almacena entidades descargadas desde servicios WFS.

Actualmente está preparado para el Nomenclátor Geográfico de Andalucía,
pero es completamente reutilizable.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Iterable


class CatalogDatabase:

    def __init__(
        self,
        database: str | Path,
    ) -> None:

        self.database = Path(database)

        self.connection = sqlite3.connect(self.database)

        self.connection.row_factory = sqlite3.Row

        self.create_tables()

    def create_tables(self) -> None:

        cursor = self.connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS named_places (

                local_id TEXT PRIMARY KEY,

                gml_id TEXT,

                namespace TEXT,

                name TEXT,

                feature_type TEXT,

                x REAL,

                y REAL,

                downloaded INTEGER NOT NULL DEFAULT 0,

                html_url TEXT,

                html_downloaded INTEGER NOT NULL DEFAULT 0,

                error TEXT,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

            );
            """
        )

        cursor.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_named_places_name
            ON named_places(name);
            """
        )

        cursor.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_named_places_type
            ON named_places(feature_type);
            """
        )

        cursor.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_named_places_downloaded
            ON named_places(downloaded);
            """
        )

        self.connection.commit()

    def insert_many(
        self,
        records: Iterable[dict],
    ) -> int:

        cursor = self.connection.cursor()

        total = 0

        for record in records:

            cursor.execute(
                """
                INSERT OR REPLACE INTO named_places(

                    local_id,
                    gml_id,
                    namespace,
                    name,
                    feature_type,
                    x,
                    y

                )

                VALUES(

                    :local_id,
                    :gml_id,
                    :namespace,
                    :name,
                    :feature_type,
                    :x,
                    :y

                )
                """,
                record,
            )

            total += 1

        self.connection.commit()

        return total

    def count(self) -> int:

        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM named_places
            """
        )

        return cursor.fetchone()[0]

    def pending(self) -> int:

        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM named_places
            WHERE downloaded = 0
            """
        )

        return cursor.fetchone()[0]

    def downloaded(self) -> int:

        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM named_places
            WHERE downloaded = 1
            """
        )

        return cursor.fetchone()[0]

    def close(self) -> None:

        self.connection.close()