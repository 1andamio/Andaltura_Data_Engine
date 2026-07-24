"""
Normalización de valores obtenidos del SIMA.
"""

from __future__ import annotations

import re


class ValueNormalizer:
    """
    Convierte los valores de texto del SIMA en tipos Python.

    Esta clase centraliza toda la lógica de conversión utilizada por los
    distintos parsers del importador.
    """

    INTEGER_PATTERN = re.compile(r"^\d{1,3}(?:\.\d{3})*$")
    FLOAT_PATTERN = re.compile(r"^\d+(?:\.\d{3})*,\d+$")
    COORDINATE_PATTERN = re.compile(
        r"^-?\d+(?:\.\d+)?,\s*-?\d+(?:\.\d+)?$"
    )

    # ------------------------------------------------------------------

    def normalize(self, value: str):
        """
        Convierte automáticamente un valor del SIMA.
        """

        value = self.clean_text(value)

        if value == "":
            return None

        if self.is_coordinate(value):
            return self.to_coordinate(value)

        if self.is_integer(value):
            return self.to_int(value)

        if self.is_float(value):
            return self.to_float(value)

        return value

    # ------------------------------------------------------------------

    @staticmethod
    def clean_text(value: str) -> str:
        """
        Elimina espacios sobrantes.
        """

        return " ".join(value.strip().split())

    # ------------------------------------------------------------------

    @staticmethod
    def is_empty(value: str | None) -> bool:
        """
        Indica si el valor está vacío.
        """

        return value is None or value.strip() == ""

    # ------------------------------------------------------------------

    def is_integer(self, value: str) -> bool:
        """
        Indica si el valor representa un entero español.
        """

        return bool(self.INTEGER_PATTERN.fullmatch(value))

    # ------------------------------------------------------------------

    def is_float(self, value: str) -> bool:
        """
        Indica si el valor representa un decimal español.
        """

        return bool(self.FLOAT_PATTERN.fullmatch(value))

    # ------------------------------------------------------------------

    def is_coordinate(self, value: str) -> bool:
        """
        Indica si el valor representa unas coordenadas.
        """

        return bool(self.COORDINATE_PATTERN.fullmatch(value))

    # ------------------------------------------------------------------

    @staticmethod
    def to_int(value: str) -> int:
        """
        Convierte un entero español.

        Ejemplo:
            8.628 -> 8628
        """

        return int(value.replace(".", ""))

    # ------------------------------------------------------------------

    @staticmethod
    def to_float(value: str) -> float:
        """
        Convierte un decimal español.

        Ejemplo:
            12.345,67 -> 12345.67
        """

        return float(
            value.replace(".", "")
                 .replace(",", ".")
        )

    # ------------------------------------------------------------------

    @staticmethod
    def to_coordinate(value: str) -> tuple[float, float]:
        """
        Convierte unas coordenadas en una tupla.
        """

        lat, lon = value.split(",")

        return (
            float(lat),
            float(lon),
        )