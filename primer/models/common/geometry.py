"""
Modelos geométricos básicos.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Point:
    """
    Punto 2D.

    Coordenadas en el SRC original del servicio.
    """

    x: float
    y: float

    @classmethod
    def from_pos(cls, pos: str) -> "Point":
        """
        Crea un Point a partir del contenido de un <gml:pos>.

        Ejemplo:
            "428114.054 4177614.090"
        """

        x, y = pos.split()

        return cls(
            x=float(x),
            y=float(y),
        )

    def as_tuple(self) -> tuple[float, float]:
        """
        Devuelve (x, y).
        """

        return (self.x, self.y)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"