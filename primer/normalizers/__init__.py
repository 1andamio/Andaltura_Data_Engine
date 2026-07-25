"""
Sistema de normalización.

Este paquete define la infraestructura para homogeneizar las
estructuras de datos obtenidas por los analizadores antes de su
transformación al modelo interno del framework.
"""

from .normalizer import BaseNormalizer

__all__ = [
    "BaseNormalizer",
]