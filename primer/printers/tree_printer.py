"""
Tree Printer

Genera una representación ASCII de un Model.
"""

from __future__ import annotations

from primer.core.model import Model, Node


class TreePrinter:
    """
    Genera un árbol ASCII a partir de un Model.
    """

    # ---------------------------------------------------------

    def render(self, model: Model) -> str:
        """
        Devuelve el árbol completo como texto.
        """

        root = model.root

        if root is None:
            return "<empty model>"

        lines: list[str] = []

        self._render_node(
            model=model,
            node=root,
            prefix="",
            is_last=True,
            lines=lines,
        )

        return "\n".join(lines)

    # ---------------------------------------------------------

    def _render_node(
        self,
        *,
        model: Model,
        node: Node,
        prefix: str,
        is_last: bool,
        lines: list[str],
    ) -> None:

        connector = "└── " if is_last else "├── "

        if node.is_root:
            lines.append(node.name)
        else:
            lines.append(f"{prefix}{connector}{node.name}")

        children = model.children(node)

        if node.is_root:
            child_prefix = ""
        else:
            child_prefix = prefix + ("    " if is_last else "│   ")

        for index, child in enumerate(children):

            self._render_node(
                model=model,
                node=child,
                prefix=child_prefix,
                is_last=index == len(children) - 1,
                lines=lines,
            )