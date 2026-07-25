"""
Registro de validadores.

Permite registrar y crear dinámicamente los validadores
disponibles en el framework.
"""

from __future__ import annotations

from typing import Type

from ..core.exceptions import ConfigurationError
from .validator import BaseValidator


class ValidatorRegistry:
    """
    Registro global de validadores.
    """

    _validators: dict[str, Type[BaseValidator]] = {}

    @classmethod
    def register(
        cls,
        validator_class: Type[BaseValidator],
    ) -> None:
        """
        Registra un validador.
        """

        validator_class.validate_definition()

        cls._validators[
            validator_class.name.lower()
        ] = validator_class

    @classmethod
    def unregister(
        cls,
        name: str,
    ) -> None:
        """
        Elimina un validador del registro.
        """

        cls._validators.pop(
            name.lower(),
            None,
        )

    @classmethod
    def exists(
        cls,
        name: str,
    ) -> bool:
        """
        Indica si un validador está registrado.
        """

        return name.lower() in cls._validators

    @classmethod
    def get(
        cls,
        name: str,
    ) -> Type[BaseValidator]:
        """
        Devuelve la clase asociada a un validador.
        """

        try:
            return cls._validators[name.lower()]

        except KeyError as exc:
            raise ConfigurationError(
                f"Validador no registrado: '{name}'."
            ) from exc

    @classmethod
    def create(
        cls,
        name: str,
    ) -> BaseValidator:
        """
        Crea una instancia del validador solicitado.
        """

        return cls.get(name)()

    @classmethod
    def names(cls) -> list[str]:
        """
        Devuelve los nombres de los validadores registrados.
        """

        return sorted(cls._validators)

    @classmethod
    def validators(
        cls,
    ) -> list[Type[BaseValidator]]:
        """
        Devuelve todas las clases registradas.
        """

        return list(cls._validators.values())

    @classmethod
    def count(cls) -> int:
        """
        Devuelve el número de validadores registrados.
        """

        return len(cls._validators)

    @classmethod
    def clear(cls) -> None:
        """
        Elimina todos los validadores registrados.
        """

        cls._validators.clear()