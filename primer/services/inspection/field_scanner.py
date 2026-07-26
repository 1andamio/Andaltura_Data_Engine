"""
Escáner genérico de estructuras XML.

Recorre recursivamente cualquier árbol XML y registra todos los elementos
encontrados junto con su ruta, namespace y atributos.

No realiza ninguna interpretación de los datos; únicamente descubre la
estructura del documento.
"""

from __future__ import annotations

from xml.etree.ElementTree import Element

from .models import FieldInfo


class FieldScanner:
    """
    Descubre automáticamente la estructura de un documento XML.

    Cada elemento encontrado se registra mediante un objeto FieldInfo,
    identificado por su ruta completa dentro del árbol XML.
    """

    def __init__(self) -> None:
        self._fields: dict[str, FieldInfo] = {}

    @property
    def fields(self) -> dict[str, FieldInfo]:
        """
        Devuelve todos los campos descubiertos.
        """
        return self._fields

    def clear(self) -> None:
        """
        Elimina toda la información almacenada.
        """
        self._fields.clear()

    def scan(self, root: Element) -> None:
        """
        Inicia el análisis del árbol XML.

        Parameters
        ----------
        root
            Elemento raíz del documento XML.
        """
        self.clear()
        self._scan_element(root, parent_path="")

    # ------------------------------------------------------------------

    def _scan_element(
        self,
        element: Element,
        parent_path: str,
    ) -> None:
        """
        Analiza un elemento y todos sus descendientes.
        """

        namespace, tag = self._split_tag(element.tag)

        path = f"{parent_path}/{tag}" if parent_path else tag

        field = self._fields.get(path)

        if field is None:
            field = FieldInfo(
                path=path,
                tag=tag,
                namespace=namespace,
            )
            self._fields[path] = field

        field.register(attributes=element.attrib)

        for child in element:
            self._scan_element(child, path)

    # ------------------------------------------------------------------

    @staticmethod
    def _split_tag(tag: str) -> tuple[str | None, str]:
        """
        Separa namespace y nombre del elemento.

        Ejemplos
        --------

        '{http://www.opengis.net/gml/3.2}Point'

            -> ('http://www.opengis.net/gml/3.2', 'Point')

        'Point'

            -> (None, 'Point')
        """

        if tag.startswith("{"):
            namespace, local = tag[1:].split("}", 1)
            return namespace, local

        return None, tag