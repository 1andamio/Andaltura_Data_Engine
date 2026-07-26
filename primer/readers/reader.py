"""
Lector XML de Primer.

Convierte cualquier documento XML en un Model.
"""

from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path

from primer.core.model import Attribute, Model, Node


class XMLReader:
    """
    Lector genérico de documentos XML.
    """

    # ---------------------------------------------------------

    def read(self, file: str | Path) -> Model:
        """
        Lee un archivo XML.
        """

        tree = ET.parse(file)

        return self.read_tree(tree)

    # ---------------------------------------------------------

    def read_tree(
        self,
        tree: ET.ElementTree,
    ) -> Model:
        """
        Lee un árbol XML.
        """

        return self.read_element(tree.getroot())

    # ---------------------------------------------------------

    def read_element(
        self,
        root: ET.Element,
    ) -> Model:
        """
        Construye un modelo a partir de un elemento XML.
        """

        model = Model()

        self._walk(
            model=model,
            element=root,
            parent=None,
            parent_path="",
        )

        return model

    # ---------------------------------------------------------

    def _walk(
        self,
        *,
        model: Model,
        element: ET.Element,
        parent: Node | None,
        parent_path: str,
    ) -> None:
        """
        Recorre recursivamente el árbol XML.
        """

        namespace, name = self._split_tag(element.tag)

        path = (
            f"{parent_path}/{name}"
            if parent_path
            else name
        )

        node = model.get_or_create(
            path=path,
            name=name,
            namespace=namespace,
            parent=parent,
        )

        node.occurrences += 1

        # ------------------------------------
        # atributos
        # ------------------------------------

        for attr in element.attrib:

            attr_ns, attr_name = self._split_tag(attr)

            attribute = node.attributes.get(attr_name)

            if attribute is None:

                attribute = Attribute(
                    name=attr_name,
                    namespace=attr_ns,
                )

                node.attributes[attr_name] = attribute

            attribute.occurrences += 1

        # ------------------------------------
        # hijos
        # ------------------------------------

        for child in element:

            self._walk(
                model=model,
                element=child,
                parent=node,
                parent_path=path,
            )

    # ---------------------------------------------------------

    @staticmethod
    def _split_tag(
        tag: str,
    ) -> tuple[str | None, str]:
        """
        Separa namespace y nombre local.
        """

        if tag.startswith("{"):

            namespace, name = tag[1:].split("}", 1)

            return namespace, name

        return None, tag