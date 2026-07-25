"""
Registro de exportadores.

Permite registrar y crear dinámicamente los exportadores
disponibles en el framework.
"""

from __future__ import annotations

from typing import Type

from ..core.exceptions import ConfigurationError
from .exporter import BaseExporter


class ExporterRegistry:
    """
    Registro global de exportadores.
    """

    _exporters: dict[str, Type[BaseExporter]] = {}

    @classmethod
    def register(
        cls,
        exporter_class: Type[BaseExporter],
    ) -> None:
        """
        Registra un exportador.
        """

        exporter_class.validate_definition()

        cls._exporters[
            exporter_class.name.lower()
        ] = exporter_class

    @classmethod
    def unregister(
        cls,
        name: str,
    ) -> None:
        """
        Elimina un exportador del registro.
        """

        cls._exporters.pop(
            name.lower(),
            None,
        )

    @classmethod
    def exists(
        cls,
        name: str,
    ) -> bool:
        """
        Indica si un exportador está registrado.
        """

        return name.lower() in cls._exporters

    @classmethod
    def get(
        cls,
        name: str,
    ) -> Type[BaseExporter]:
        """
        Devuelve la clase asociada a un exportador.
        """

        try:
            return cls._exporters[name.lower()]

        except KeyError as exc:
            raise ConfigurationError(
                f"Exportador no registrado: '{name}'."
            ) from exc

    @classmethod
    def create(
        cls,
        name: str,
    ) -> BaseExporter:
        """
        Crea una instancia del exportador solicitado.
        """

        return cls.get(name)()

    @classmethod
    def names(cls) -> list[str]:
        """
        Devuelve los nombres de los exportadores registrados.
        """

        return sorted(cls._exporters)

    @classmethod
    def exporters(
        cls,
    ) -> list[Type[BaseExporter]]:
        """
        Devuelve todas las clases registradas.
        """

        return list(cls._exporters.values())

    @classmethod
    def count(cls) -> int:
        """
        Devuelve el número de exportadores registrados.
        """

        return len(cls._exporters)

    @classmethod
    def clear(cls) -> None:
        """
        Elimina todos los exportadores registrados.
        """

        cls._exporters.clear()