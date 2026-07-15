from modelos.servicio import Servicio
from excepciones.excepciones import ValidacionError


class Equipo(Servicio):

    def __init__(
            self,
            codigo,
            nombre,
            costo_base,
            tipo):

        super().__init__(
            codigo,
            nombre,
            costo_base
        )

        self.tipo = tipo

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, valor):

        valor = valor.strip()

        if valor == "":

            raise ValidacionError(
                "Debe indicar un tipo."
            )

        self.__tipo = valor

    def calcular_costo(self, dias=1):

        return self.costo_base * dias

    def descripcion(self):

        return (
            f"Equipo tipo "
            f"{self.tipo}"
        )