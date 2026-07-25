"""
Registro central de proveedores.

Mantiene el catálogo de proveedores disponibles y permite registrar,
consultar y crear instancias de forma centralizada.
"""

from __future__ import annotations

from typing import Type

from .exceptions import ConfigurationError
from .provider import BaseProvider


class ProviderRegistry:
    """
    Registro global de proveedores.

    Actúa como punto central para el registro y creación de proveedores
    disponibles dentro del framework.
    """

    _providers: dict[str, Type[BaseProvider]] = {}

    @classmethod
    def register(
        cls,
        provider_class: Type[BaseProvider],
    ) -> None:
        """
        Registra una nueva clase de proveedor.
        """

        name = provider_class.provider_name.lower()

        if name in cls._providers:
            raise ConfigurationError(
                f"El proveedor '{name}' ya está registrado."
            )

        cls._providers[name] = provider_class

    @classmethod
    def unregister(
        cls,
        name: str,
    ) -> None:
        """
        Elimina un proveedor del registro.
        """

        cls._providers.pop(name.lower(), None)

    @classmethod
    def exists(
        cls,
        name: str,
    ) -> bool:
        """
        Indica si un proveedor está registrado.
        """

        return name.lower() in cls._providers

    @classmethod
    def get(
        cls,
        name: str,
    ) -> Type[BaseProvider]:
        """
        Devuelve la clase asociada a un proveedor.
        """

        provider = cls._providers.get(name.lower())

        if provider is None:
            raise ConfigurationError(
                f"Proveedor no registrado: '{name}'."
            )

        return provider

    @classmethod
    def create(
        cls,
        name: str,
    ) -> BaseProvider:
        """
        Crea una nueva instancia del proveedor solicitado.
        """

        return cls.get(name)()

    @classmethod
    def names(
        cls,
    ) -> list[str]:
        """
        Devuelve los nombres de los proveedores registrados.
        """

        return sorted(cls._providers.keys())

    @classmethod
    def providers(
        cls,
    ) -> list[Type[BaseProvider]]:
        """
        Devuelve todas las clases de proveedores registradas.
        """

        return list(cls._providers.values())

    @classmethod
    def count(
        cls,
    ) -> int:
        """
        Devuelve el número de proveedores registrados.
        """

        return len(cls._providers)

    @classmethod
    def clear(
        cls,
    ) -> None:
        """
        Elimina todos los proveedores registrados.
        """

        cls._providers.clear()