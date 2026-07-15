from modelos.servicio import Servicio
from excepciones.excepciones import ValidacionError


class Sala(Servicio):

    def __init__(
            self,
            codigo,
            nombre,
            costo_base,
            capacidad):

        super().__init__(
            codigo,
            nombre,
            costo_base
        )

        self.capacidad = capacidad

    @property
    def capacidad(self):
        return self.__capacidad

    @capacidad.setter
    def capacidad(self, valor):

        if valor <= 0:

            raise ValidacionError(
                "Capacidad inválida."
            )

        self.__capacidad = valor

    def calcular_costo(self, horas=1):

        return self.costo_base * horas

    def descripcion(self):

        return (
            f"Sala para "
            f"{self.capacidad} personas."
        )