"""
Registro de normalizadores.

Permite registrar y crear dinámicamente los normalizadores
disponibles en el framework.
"""

from __future__ import annotations

from typing import Type

from ..core.exceptions import ConfigurationError
from .normalizer import BaseNormalizer


class NormalizerRegistry:
    """
    Registro global de normalizadores.
    """

    _normalizers: dict[str, Type[BaseNormalizer]] = {}

    @classmethod
    def register(
        cls,
        normalizer_class: Type[BaseNormalizer],
    ) -> None:
        """
        Registra un normalizador.
        """

        normalizer_class.validate_definition()

        cls._normalizers[
            normalizer_class.name.lower()
        ] = normalizer_class

    @classmethod
    def unregister(
        cls,
        name: str,
    ) -> None:
        """
        Elimina un normalizador del registro.
        """

        cls._normalizers.pop(
            name.lower(),
            None,
        )

    @classmethod
    def exists(
        cls,
        name: str,
    ) -> bool:
        """
        Indica si un normalizador está registrado.
        """

        return name.lower() in cls._normalizers

    @classmethod
    def get(
        cls,
        name: str,
    ) -> Type[BaseNormalizer]:
        """
        Devuelve la clase asociada a un normalizador.
        """

        try:
            return cls._normalizers[name.lower()]

        except KeyError as exc:
            raise ConfigurationError(
                f"Normalizador no registrado: '{name}'."
            ) from exc

    @classmethod
    def create(
        cls,
        name: str,
    ) -> BaseNormalizer:
        """
        Crea una instancia del normalizador solicitado.
        """

        return cls.get(name)()

    @classmethod
    def names(cls) -> list[str]:
        """
        Devuelve los nombres de los normalizadores registrados.
        """

        return sorted(cls._normalizers)

    @classmethod
    def normalizers(
        cls,
    ) -> list[Type[BaseNormalizer]]:
        """
        Devuelve todas las clases registradas.
        """

        return list(cls._normalizers.values())

    @classmethod
    def count(cls) -> int:
        """
        Devuelve el número de normalizadores registrados.
        """

        return len(cls._normalizers)

    @classmethod
    def clear(cls) -> None:
        """
        Elimina todos los normalizadores registrados.
        """

        cls._normalizers.clear()