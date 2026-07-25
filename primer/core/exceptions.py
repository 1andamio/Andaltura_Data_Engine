"""
Jerarquía de excepciones del framework Primer.

Define las excepciones comunes utilizadas por los distintos
componentes del framework para representar errores de conexión,
procesamiento, validación y configuración.
"""


class PrimerError(Exception):
    """
    Excepción base del framework.

    Todas las excepciones específicas de Primer deben heredar de esta
    clase para facilitar su captura y tratamiento.
    """


class ConnectionError(PrimerError):
    """
    Error durante la comunicación con un recurso externo.
    """


class DownloadError(PrimerError):
    """
    Error producido durante la descarga de un recurso.
    """


class ParseError(PrimerError):
    """
    Error al interpretar o analizar un recurso.
    """


class ValidationError(PrimerError):
    """
    Error de validación de datos.
    """


class ConfigurationError(PrimerError):
    """
    Error en la configuración del framework.
    """


class ResourceNotFoundError(PrimerError):
    """
    El recurso solicitado no existe o no puede localizarse.
    """


class UnsupportedFormatError(PrimerError):
    """
    El formato del recurso no está soportado.
    """


class AuthenticationError(ConnectionError):
    """
    Error de autenticación frente a un servicio externo.
    """


class AuthorizationError(ConnectionError):
    """
    El servicio externo deniega el acceso al recurso solicitado.
    """


class TimeoutError(ConnectionError):
    """
    La operación excedió el tiempo máximo permitido.
    """