"""
Exportador genérico de objetos del MDTA.

Actualmente exporta a JSON, pero está preparado para crecer con
otros formatos (SQLite, GeoPackage, CSV, etc.).
"""

from __future__ import annotations

import json
from dataclasses import asdict, is_dataclass
from pathlib import Path
from typing import Any


class Exporter:
    """Exportador genérico."""

    @staticmethod
    def to_dict(obj: Any) -> dict:
        """
        Convierte cualquier dataclass en un diccionario.
        """

        if not is_dataclass(obj):
            raise TypeError(
                f"El objeto {type(obj).__name__} no es una dataclass."
            )

        return asdict(obj)

    @staticmethod
    def save_json(obj: Any, filename: str | Path) -> Path:
        """
        Guarda el objeto como JSON.
        """

        filename = Path(filename)

        filename.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with filename.open(
            "w",
            encoding="utf-8",
        ) as f:

            json.dump(
                Exporter.to_dict(obj),
                f,
                indent=4,
                ensure_ascii=False,
            )

        return filename