"""
Iterador de entidades WFS.

Se encarga de solicitar sucesivos GetFeature al servidor.
No interpreta el contenido recibido; simplemente devuelve
las respuestas al consumidor.
"""

from __future__ import annotations

from collections.abc import Iterator

from .client import WFSClient


class FeatureIterator(Iterator):
    """
    Iterador de peticiones GetFeature.

    Devuelve una respuesta WFS por cada lote solicitado.
    """

    def __init__(
        self,
        client: WFSClient,
        *,
        type_name: str,
        batch_size: int = 1000,
        output_format: str | None = None,
        **extra_params,
    ) -> None:

        self.client = client
        self.type_name = type_name
        self.batch_size = batch_size
        self.output_format = output_format
        self.extra_params = extra_params

        self.start_index = 0
        self.finished = False

    def __iter__(self) -> "FeatureIterator":
        return self

    def __next__(self):

        if self.finished:
            raise StopIteration

        response = self.client.get_feature(
            type_name=self.type_name,
            start_index=self.start_index,
            count=self.batch_size,
            output_format=self.output_format,
            **self.extra_params,
        )

        self.start_index += self.batch_size

        return response

    def reset(self) -> None:
        """
        Reinicia el iterador.
        """

        self.start_index = 0
        self.finished = False