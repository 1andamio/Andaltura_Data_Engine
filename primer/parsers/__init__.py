"""
Sistema de analizadores.

Este paquete define la infraestructura para interpretar recursos
externos y transformarlos en estructuras de datos que puedan ser
procesadas por el resto del framework.
"""

from .parser import BaseParser

__all__ = [
    "BaseParser",
]