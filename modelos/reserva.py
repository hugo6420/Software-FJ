from excepciones.excepciones import (
    ReservaError,
    ValidacionError
)

from utilidades.logger import Logger


class Reserva:

    def __init__(self, codigo, cliente, servicio, duracion):

        if not codigo.strip():
            raise ValidacionError("Código inválido.")

        if duracion <= 0:
            raise ValidacionError("La duración debe ser mayor que cero.")

        self.codigo = codigo
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):

        if self.estado == "Confirmada":
            raise ReservaError("La reserva ya está confirmada.")

        self.estado = "Confirmada"

        Logger.info(f"Reserva {self.codigo} confirmada.")

    def cancelar(self):

        if self.estado == "Cancelada":
            raise ReservaError("La reserva ya fue cancelada.")

        self.estado = "Cancelada"

        Logger.warning(f"Reserva {self.codigo} cancelada.")

    def calcular_total(self):

        try:

            return self.servicio.calcular_costo(
                self.duracion
            )

        except Exception as e:

            raise ReservaError(
                "Error calculando el total."
            ) from e

        finally:

            Logger.info(
                f"Reserva {self.codigo} procesada."
            )

    def mostrar(self):

        return (
            f"Código      : {self.codigo}\n"
            f"Cliente     : {self.cliente.nombre}\n"
            f"Servicio    : {self.servicio.nombre}\n"
            f"Duración    : {self.duracion}\n"
            f"Estado      : {self.estado}\n"
            f"Total       : ${self.calcular_total():,.0f}"
        )