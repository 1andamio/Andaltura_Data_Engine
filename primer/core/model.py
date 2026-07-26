"""
Primer Universal Model

Representa la estructura lógica de cualquier fuente de datos
(XML, JSON, CSV, SQLite, GeoPackage, etc.).

El modelo contiene únicamente información estructural.
No almacena estadísticas de valores ni lógica de inspección.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterator


# ==========================================================
# ATTRIBUTE
# ==========================================================

@dataclass(slots=True)
class Attribute:
    """
    Atributo perteneciente a un nodo.
    """

    name: str

    namespace: str | None = None

    occurrences: int = 0


# ==========================================================
# NODE
# ==========================================================

@dataclass(slots=True)
class Node:
    """
    Nodo estructural del modelo.
    """

    path: str

    name: str

    namespace: str | None = None

    parent_path: str | None = None

    children_paths: list[str] = field(default_factory=list)

    attributes: dict[str, Attribute] = field(default_factory=dict)

    occurrences: int = 0

    order: int = 0

    @property
    def is_root(self) -> bool:
        return self.parent_path is None

    @property
    def depth(self) -> int:
        """
        Profundidad calculada a partir de la ruta.
        """

        return self.path.count("/")


# ==========================================================
# MODEL
# ==========================================================

@dataclass(slots=True)
class Model:
    """
    Modelo universal de Primer.
    """

    nodes: dict[str, Node] = field(default_factory=dict)

    metadata: dict[str, str] = field(default_factory=dict)

    # -----------------------------------------------------
    # Python API
    # -----------------------------------------------------

    def __len__(self) -> int:
        return len(self.nodes)

    def __contains__(self, path: str) -> bool:
        return path in self.nodes

    def __iter__(self) -> Iterator[Node]:
        yield from self.walk()

    # -----------------------------------------------------
    # Root
    # -----------------------------------------------------

    @property
    def root(self) -> Node | None:

        for node in self.nodes.values():

            if node.parent_path is None:
                return node

        return None

    # -----------------------------------------------------
    # Node creation
    # -----------------------------------------------------

    def add_node(
        self,
        *,
        path: str,
        name: str,
        namespace: str | None = None,
        parent_path: str | None = None,
        order: int = 0,
    ) -> Node:
        """
        Crea un nodo si todavía no existe.
        """

        existing = self.nodes.get(path)

        if existing is not None:
            return existing

        node = Node(
            path=path,
            name=name,
            namespace=namespace,
            parent_path=parent_path,
            order=order,
        )

        self.nodes[path] = node

        if parent_path:

            parent = self.nodes[parent_path]

            if path not in parent.children_paths:
                parent.children_paths.append(path)

        return node

    # -----------------------------------------------------
    # Queries
    # -----------------------------------------------------

    def find(self, path: str) -> Node | None:
        """
        Busca un nodo por su ruta.
        """

        return self.nodes.get(path)

    def find_by_name(
        self,
        name: str,
    ) -> list[Node]:
        """
        Busca todos los nodos con un nombre determinado.
        """

        return [
            node
            for node in self.nodes.values()
            if node.name == name
        ]

    def parent(
        self,
        node: Node,
    ) -> Node | None:
        """
        Devuelve el nodo padre.
        """

        if node.parent_path is None:
            return None

        return self.nodes.get(node.parent_path)

    def children(
        self,
        node: Node,
    ) -> list[Node]:
        """
        Devuelve los hijos ordenados.
        """

        children = [
            self.nodes[path]
            for path in node.children_paths
        ]

        children.sort(key=lambda n: n.order)

        return children

    # -----------------------------------------------------
    # Tree traversal
    # -----------------------------------------------------

    def walk(self) -> Iterator[Node]:
        """
        Recorre el árbol completo en profundidad (DFS).
        """

        root = self.root

        if root is None:
            return

        stack = [root]

        while stack:

            node = stack.pop()

            yield node

            children = self.children(node)

            stack.extend(reversed(children))

    # -----------------------------------------------------
    # Metadata
    # -----------------------------------------------------

    def namespaces(self) -> list[str]:
        """
        Devuelve todos los namespaces presentes.
        """

        return sorted({
            node.namespace
            for node in self.nodes.values()
            if node.namespace
        })

    def attributes(self) -> list[Attribute]:
        """
        Devuelve todos los atributos del modelo.
        """

        attrs: list[Attribute] = []

        for node in self.nodes.values():
            attrs.extend(node.attributes.values())

        return attrs

    # -----------------------------------------------------
    # Statistics
    # -----------------------------------------------------

    def stats(self) -> dict[str, int]:
        """
        Estadísticas básicas del modelo.
        """

        return {
            "nodes": len(self.nodes),
            "attributes": len(self.attributes()),
            "namespaces": len(self.namespaces()),
            "max_depth": max(
                (node.depth for node in self.nodes.values()),
                default=0,
            ),
        }