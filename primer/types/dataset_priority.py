"""
Prioridades de un Dataset.
"""

from enum import Enum


class DatasetPriority(str, Enum):
    """
    Prioridad asignada a un Dataset.
    """

    LOW = "low"

    NORMAL = "normal"

    HIGH = "high"

    CRITICAL = "critical"