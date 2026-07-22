"""
Normalizador de valores del SIMA.

Convierte los valores de texto en tipos Python.
"""

from __future__ import annotations

import re


class ValueNormalizer:
    """
    Convierte un texto del SIMA en un valor Python.
    """

    INTEGER_PATTERN = re.compile(r"^\d{1,3}(?:\.\d{3})*$")
    FLOAT_PATTERN = re.compile(r"^\d+(?:\.\d{3})*,\d+$")
    COORDINATE_PATTERN = re.compile(
        r"^-?\d+(?:\.\d+)?,\s*-?\d+(?:\.\d+)?$"
    )

    def normalize(self, value: str):

        value = value.strip()

        if value == "":
            return None

        # Coordenadas
        if self.COORDINATE_PATTERN.match(value):

            lat, lon = value.split(",")

            return (
                float(lat),
                float(lon),
            )

        # Entero español
        if self.INTEGER_PATTERN.match(value):

            return int(
                value.replace(".", "")
            )

        # Decimal español
        if self.FLOAT_PATTERN.match(value):

            return float(
                value.replace(".", "")
                     .replace(",", ".")
            )

        # Texto
        return value