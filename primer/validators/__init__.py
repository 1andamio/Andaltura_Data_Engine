"""
Sistema de validación.

Este paquete define la infraestructura para comprobar la integridad,
consistencia y calidad del modelo interno utilizado por Primer.
"""

from .validator import BaseValidator

__all__ = [
    "BaseValidator",
]