"""
Clase base para todos los componentes del framework.

Define el contrato común que deben cumplir los componentes de Primer,
proporcionando una identidad única y mecanismos básicos de validación.
"""

from __future__ import annotations

from abc import ABC


class BaseComponent(ABC):
    """
    Clase base para todos los componentes del framework.
    """

    #: Nombre único del componente.
    name: str = ""

    #: Versión del componente.
    version: str = ""

    #: Descripción opcional.
    description: str = ""

    @classmethod
    def validate_definition(cls) -> None:
        """
        Comprueba que la definición del componente es válida.
        """

        if not cls.name:
            raise ValueError(
                f"{cls.__name__} debe definir 'name'."
            )

        if not cls.version:
            raise ValueError(
                f"{cls.__name__} debe definir 'version'."
            )

    @classmethod
    def metadata(cls) -> dict[str, object]:
        """
        Devuelve los metadatos públicos del componente.
        """

        return {
            "name": cls.name,
            "version": cls.version,
            "description": cls.description,
        }

    @classmethod
    def identifier(cls) -> str:
        """
        Devuelve el identificador único del componente.
        """

        return f"{cls.name}:{cls.version}"

    def __repr__(self) -> str:

        return (
            f"{self.__class__.__name__}"
            f"(name='{self.name}', "
            f"version='{self.version}')"
        )