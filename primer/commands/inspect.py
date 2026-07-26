"""
Comando inspect.

Analiza un documento XML y muestra un resumen del modelo generado.
"""

from __future__ import annotations

from pathlib import Path

from primer.printers.entity_printer import EntityPrinter
from primer.printers.summary_printer import SummaryPrinter
from primer.printers.tree_printer import TreePrinter
from primer.readers.xml_reader import XMLReader


def inspect_command(filename: str | Path) -> None:
    """
    Inspecciona un documento XML.
    """

    # Leer el documento y construir el modelo
    reader = XMLReader()
    model = reader.read(filename)

    # Mostrar resumen
    print()
    print(SummaryPrinter().render(model, filename))

    # Mostrar árbol
    print()
    print(TreePrinter().render(model))

    # Mostrar entidades descubiertas
    print()
    print(EntityPrinter().render(model))