"""
Excepciones personalizadas del proyecto Software FJ.
"""


class SistemaError(Exception):
    """Clase base para las excepciones del sistema."""
    pass


class ClienteError(SistemaError):
    """Errores relacionados con clientes."""
    pass


class ServicioError(SistemaError):
    """Errores relacionados con servicios."""
    pass


class ReservaError(SistemaError):
    """Errores relacionados con reservas."""
    pass


class ValidacionError(SistemaError):
    """Errores de validación."""
    pass


class ClienteDuplicadoError(ClienteError):
    """Cliente ya registrado."""
    pass


class ServicioDuplicadoError(ServicioError):
    """Servicio ya registrado."""
    pass


class ReservaDuplicadaError(ReservaError):
    """Reserva ya registrada."""
    pass