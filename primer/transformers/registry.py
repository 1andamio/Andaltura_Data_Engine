"""
Registro de transformadores.

Permite registrar y crear dinámicamente los transformadores
disponibles en el framework.
"""

from __future__ import annotations

from typing import Type

from ..core.exceptions import ConfigurationError
from .transformer import BaseTransformer


class TransformerRegistry:
    """
    Registro global de transformadores.
    """

    _transformers: dict[str, Type[BaseTransformer]] = {}

    @classmethod
    def register(
        cls,
        transformer_class: Type[BaseTransformer],
    ) -> None:
        """
        Registra un transformador.
        """

        transformer_class.validate_definition()

        cls._transformers[
            transformer_class.name.lower()
        ] = transformer_class

    @classmethod
    def unregister(
        cls,
        name: str,
    ) -> None:
        """
        Elimina un transformador del registro.
        """

        cls._transformers.pop(
            name.lower(),
            None,
        )

    @classmethod
    def exists(
        cls,
        name: str,
    ) -> bool:
        """
        Indica si un transformador está registrado.
        """

        return name.lower() in cls._transformers

    @classmethod
    def get(
        cls,
        name: str,
    ) -> Type[BaseTransformer]:
        """
        Devuelve la clase asociada a un transformador.
        """

        try:
            return cls._transformers[name.lower()]

        except KeyError as exc:
            raise ConfigurationError(
                f"Transformador no registrado: '{name}'."
            ) from exc

    @classmethod
    def create(
        cls,
        name: str,
    ) -> BaseTransformer:
        """
        Crea una instancia del transformador solicitado.
        """

        return cls.get(name)()

    @classmethod
    def names(cls) -> list[str]:
        """
        Devuelve los nombres de los transformadores registrados.
        """

        return sorted(cls._transformers)

    @classmethod
    def transformers(
        cls,
    ) -> list[Type[BaseTransformer]]:
        """
        Devuelve todas las clases registradas.
        """

        return list(cls._transformers.values())

    @classmethod
    def count(cls) -> int:
        """
        Devuelve el número de transformadores registrados.
        """

        return len(cls._transformers)

    @classmethod
    def clear(cls) -> None:
        """
        Elimina todos los transformadores registrados.
        """

        cls._transformers.clear()