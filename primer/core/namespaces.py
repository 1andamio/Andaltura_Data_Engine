"""
Namespace Registry.

Mantiene la relación entre URIs y prefijos utilizados
durante la lectura de documentos XML.
"""

from __future__ import annotations


class NamespaceRegistry:

    def __init__(self):

        self._uri_to_prefix: dict[str, str] = {}

        self._prefix_to_uri: dict[str, str] = {}

    # -----------------------------------------------------

    def register(
        self,
        prefix: str,
        uri: str,
    ) -> None:

        self._uri_to_prefix[uri] = prefix

        self._prefix_to_uri[prefix] = uri

    # -----------------------------------------------------

    def prefix(
        self,
        uri: str | None,
    ) -> str | None:

        if uri is None:
            return None

        return self._uri_to_prefix.get(uri)

    # -----------------------------------------------------

    def uri(
        self,
        prefix: str | None,
    ) -> str | None:

        if prefix is None:
            return None

        return self._prefix_to_uri.get(prefix)

    # -----------------------------------------------------

    def qualified_name(
        self,
        uri: str | None,
        local_name: str,
    ) -> str:

        prefix = self.prefix(uri)

        if prefix:

            return f"{prefix}:{local_name}"

        return local_name

    # -----------------------------------------------------

    def __len__(self):

        return len(self._uri_to_prefix)

    def __contains__(self, uri: str):

        return uri in self._uri_to_prefix

    def items(self):

        return self._uri_to_prefix.items()