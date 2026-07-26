"""
Clase base para todos los discoverers.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from primer.core.model import Model


class Discoverer(ABC):
    """
    Clase base para todos los procesos de descubrimiento.
    """

    @abstractmethod
    def discover(self, model: Model):
        """
        Ejecuta el descubrimiento sobre un modelo.
        """
        raise NotImplementedError