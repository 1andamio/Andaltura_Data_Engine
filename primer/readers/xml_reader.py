"""
XML Reader

Convierte un documento XML en un Model de Primer.
"""

from __future__ import annotations

from pathlib import Path
from xml.etree import ElementTree as ET

from primer.core.model import Attribute, Model


class XMLReader:
    """
    Lector de documentos XML.
    """

    name = "XMLReader"

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def read(self, filename: str | Path) -> Model:
        """
        Lee un documento XML y construye un Model.
        """

        filename = Path(filename)

        tree = ET.parse(filename)
        root = tree.getroot()

        model = Model()

        model.metadata["reader"] = self.name
        model.metadata["filename"] = filename.name
        model.metadata["path"] = str(filename)

        self._walk(
            model=model,
            element=root,
            parent_path=None,
            order=0,
        )

        return model

    # ---------------------------------------------------------
    # Internal
    # ---------------------------------------------------------

    def _walk(
        self,
        *,
        model: Model,
        element: ET.Element,
        parent_path: str | None,
        order: int,
    ) -> None:
        """
        Recorre recursivamente el árbol XML.
        """

        namespace, name = self._split_tag(element.tag)

        qualified_name = (
            f"{namespace}:{name}"
            if namespace
            else name
        )

        path = (
            qualified_name
            if parent_path is None
            else f"{parent_path}/{qualified_name}"
        )

        node = model.add_node(
            path=path,
            name=name,
            namespace=namespace,
            parent_path=parent_path,
            order=order,
        )

        node.occurrences += 1

        # -----------------------------------------------------
        # Attributes
        # -----------------------------------------------------

        for attr_name in element.attrib:

            attr_namespace, attr_local = self._split_tag(attr_name)

            key = (
                f"{attr_namespace}:{attr_local}"
                if attr_namespace
                else attr_local
            )

            attribute = node.attributes.get(key)

            if attribute is None:

                attribute = Attribute(
                    name=attr_local,
                    namespace=attr_namespace,
                )

                node.attributes[key] = attribute

            attribute.occurrences += 1

        # -----------------------------------------------------
        # Children
        # -----------------------------------------------------

        for index, child in enumerate(element):

            self._walk(
                model=model,
                element=child,
                parent_path=path,
                order=index,
            )

    # ---------------------------------------------------------
    # Helpers
    # ---------------------------------------------------------

    @staticmethod
    def _split_tag(tag: str) -> tuple[str | None, str]:
        """
        Divide un tag XML en namespace y nombre.

        Ejemplo:

            {http://www.opengis.net/gml/3.2}Point

        devuelve:

            ("3.2", "Point")
        """

        if tag.startswith("{"):

            uri, name = tag[1:].split("}")

            namespace = uri.rsplit("/", 1)[-1]

            return namespace, name

        return None, tag