"""
Clase base para todos los proveedores de datos.

Define el contrato que deben implementar los proveedores encargados
de obtener recursos desde fuentes externas.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from collections.abc import Iterable
from typing import Any

from ..models import ExternalResource


class BaseProvider(ABC):
    """
    Clase base para cualquier proveedor de datos.

    Un proveedor es responsable de establecer la comunicación con una
    fuente externa, localizar recursos, descargarlos y convertirlos en
    objetos que puedan ser procesados por el resto del framework.
    """

    #: Identificador único del proveedor.
    provider_name: str = ""

    #: Versión del proveedor.
    provider_version: str = ""

    @classmethod
    def validate_definition(cls) -> None:
        """
        Comprueba que la definición del proveedor es válida.
        """

        if not cls.provider_name:
            raise ValueError(
                f"{cls.__name__} debe definir 'provider_name'."
            )

        if not cls.provider_version:
            raise ValueError(
                f"{cls.__name__} debe definir 'provider_version'."
            )

    @abstractmethod
    def connect(self) -> None:
        """
        Establece la conexión con la fuente de datos.
        """

    @abstractmethod
    def disconnect(self) -> None:
        """
        Finaliza la conexión con la fuente de datos.
        """

    @abstractmethod
    def search(
        self,
        query: Any,
    ) -> Iterable[ExternalResource]:
        """
        Busca recursos que cumplan un determinado criterio.
        """

    @abstractmethod
    def download(
        self,
        resource: ExternalResource,
    ) -> Any:
        """
        Descarga el contenido asociado a un recurso.
        """

    @abstractmethod
    def parse(
        self,
        source: Any,
    ) -> Iterable[ExternalResource]:
        """
        Interpreta los datos originales obtenidos desde la fuente.
        """

    @abstractmethod
    def normalize(
        self,
        resource: ExternalResource,
    ) -> ExternalResource:
        """
        Normaliza un recurso antes de su procesamiento.
        """

    @abstractmethod
    def validate(
        self,
        resource: ExternalResource,
    ) -> bool:
        """
        Comprueba que un recurso cumple los requisitos mínimos de
        calidad y consistencia.
        """

    @abstractmethod
    def synchronize(self) -> None:
        """
        Sincroniza la fuente de datos con el estado actual.
        """