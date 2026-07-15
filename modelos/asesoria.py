from modelos.servicio import Servicio
from excepciones.excepciones import ValidacionError


class Asesoria(Servicio):

    def __init__(
            self,
            codigo,
            nombre,
            costo_base,
            especialista):

        super().__init__(
            codigo,
            nombre,
            costo_base
        )

        self.especialista = especialista

    @property
    def especialista(self):
        return self.__especialista

    @especialista.setter
    def especialista(self, valor):

        valor = valor.strip()

        if valor == "":

            raise ValidacionError(
                "Debe indicar un especialista."
            )

        self.__especialista = valor.title()

    def calcular_costo(self, horas=1):

        return self.costo_base * horas

    def descripcion(self):

        return (
            f"Asesoría especializada por "
            f"{self.especialista}"
        )