"""
Summary Printer

Genera un resumen textual de un Model.
"""

from __future__ import annotations

from pathlib import Path

from primer.core.model import Model


class SummaryPrinter:
    """
    Genera un resumen textual del modelo.
    """

    def render(self, model: Model, filename: str | Path | None = None) -> str:

        summary = model.stats()

        lines: list[str] = []

        lines.append("Primer XML Inspector")
        lines.append("-" * 40)

        if filename is not None:
            lines.append(f"Documento     : {Path(filename).name}")

        lines.append(f"Nodos         : {summary['nodes']}")
        lines.append(f"Atributos     : {summary['attributes']}")
        lines.append(f"Namespaces    : {summary['namespaces']}")
        lines.append(f"Profundidad   : {summary['max_depth']}")

        if model.root:
            lines.append(f"Nodo raíz     : {model.root.name}")

        lines.append("-" * 40)

        return "\n".join(lines)