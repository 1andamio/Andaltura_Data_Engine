"""
MDTA - SQL Build Result

Resultado de la generación de SQL a partir de un modelo MDTA.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class SQLBuildResult:
    """
    Contiene todas las sentencias SQL generadas por un motor.
    """

    create_table: str = ""

    indexes: list[str] = field(default_factory=list)

    foreign_keys: list[str] = field(default_factory=list)

    triggers: list[str] = field(default_factory=list)

    views: list[str] = field(default_factory=list)

    comments: list[str] = field(default_factory=list)

    metadata: list[str] = field(default_factory=list)

    # ---------------------------------------------------------

    @property
    def statements(self) -> list[str]:
        """
        Devuelve todas las sentencias SQL en el orden correcto.
        """

        sql = []

        if self.create_table:
            sql.append(self.create_table)

        sql.extend(self.indexes)
        sql.extend(self.foreign_keys)
        sql.extend(self.triggers)
        sql.extend(self.views)
        sql.extend(self.comments)
        sql.extend(self.metadata)

        return sql

    # ---------------------------------------------------------

    @property
    def script(self) -> str:
        """
        Devuelve un script SQL listo para ejecutar.
        """

        return "\n\n".join(self.statements)

    # ---------------------------------------------------------

    def __bool__(self) -> bool:
        return bool(self.statements)

    # ---------------------------------------------------------

    def __len__(self) -> int:
        return len(self.statements)