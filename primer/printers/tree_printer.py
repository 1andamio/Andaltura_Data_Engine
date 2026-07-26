"""
Impresión del árbol de un Model.

Convierte el modelo interno de Primer en una representación
jerárquica fácilmente legible.
"""

from __future__ import annotations

from primer.core.model import Model, Node


class TreePrinter:
    """
    Imprime un árbol jerárquico a partir de un Model.
    """

    def render(self, model: Model) -> str:
        """
        Devuelve el árbol completo como texto.
        """

        root = model.root

        if root is None:
            return "<modelo vacío>"

        lines: list[str] = []

        self._render_node(
            node=root,
            prefix="",
            is_last=True,
            lines=lines,
        )

        return "\n".join(lines)

    # ------------------------------------------------------------

    def _render_node(
        self,
        *,
        node: Node,
        prefix: str,
        is_last: bool,
        lines: list[str],
    ) -> None:

        if prefix == "":
            lines.append(node.name)
        else:
            branch = "└── " if is_last else "├── "
            lines.append(prefix + branch + node.name)

        children = sorted(
            node.children.values(),
            key=lambda n: n.name.lower(),
        )

        if prefix == "":
            next_prefix = ""
        else:
            next_prefix = prefix + ("    " if is_last else "│   ")

        total = len(children)

        for index, child in enumerate(children):

            self._render_node(
                node=child,
                prefix=next_prefix,
                is_last=index == total - 1,
                lines=lines,
            )