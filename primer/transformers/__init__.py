"""
Sistema de transformación.

Este paquete define la infraestructura para convertir las estructuras
de datos normalizadas en el modelo interno utilizado por Primer.
"""

from .transformer import BaseTransformer

__all__ = [
    "BaseTransformer",
]