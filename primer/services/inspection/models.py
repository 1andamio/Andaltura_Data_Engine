"""
Modelos de datos utilizados por el subsistema de inspección.

Estas clases representan la información descubierta durante el análisis
de documentos XML/GML.

No contienen lógica de negocio; únicamente almacenan información.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class FieldInfo:
    """
    Información descubierta sobre un campo XML.

    Attributes
    ----------
    path:
        Ruta completa del elemento dentro del documento XML.

    tag:
        Nombre del elemento sin namespace.

    namespace:
        Namespace del elemento.

    occurrences:
        Número de veces que aparece el elemento durante el análisis.

    attributes:
        Conjunto de atributos encontrados en dicho elemento.
    """

    path: str

    tag: str

    namespace: str | None = None

    occurrences: int = 0

    attributes: set[str] = field(default_factory=set)

    def register(
        self,
        *,
        attributes: dict[str, str] | None = None,
    ) -> None:
        """
        Registra una nueva aparición del elemento.
        """

        self.occurrences += 1

        if attributes:
            self.attributes.update(attributes.keys())