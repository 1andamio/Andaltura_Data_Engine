"""
Entity Printer.

Genera una representación textual de las entidades descubiertas.
"""

from __future__ import annotations

from primer.discoverers.entity_discoverer import Entity


class EntityPrinter:
    """
    Genera una tabla de entidades descubiertas.
    """

    def render(self, entities: list[Entity]) -> str:

        lines: list[str] = []

        lines.append("ENTIDADES")
        lines.append("-" * 40)

        if not entities:
            lines.append("No se han descubierto entidades.")
            return "\n".join(lines)

        lines.append(
            f"{'Nombre':30}"
            f"{'Namespace':12}"
            f"{'Apariciones'}"
        )

        lines.append("-" * 54)

        for entity in entities:

            lines.append(
                f"{entity.name:30}"
                f"{(entity.namespace or '-'):12}"
                f"{entity.occurrences}"
            )

        return "\n".join(lines)