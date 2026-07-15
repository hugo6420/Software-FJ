import re

from modelos.entidad import Entidad
from excepciones.excepciones import ValidacionError


class Cliente(Entidad):

    def __init__(
            self,
            codigo,
            nombre,
            correo,
            telefono):

        super().__init__(codigo)

        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):

        valor = valor.strip()

        if len(valor) < 3:

            raise ValidacionError(
                "Nombre inválido."
            )

        self.__nombre = valor.title()

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):

        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not re.match(patron, valor):

            raise ValidacionError(
                "Correo inválido."
            )

        self.__correo = valor.lower()

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):

        valor = str(valor)

        if not valor.isdigit():

            raise ValidacionError(
                "Teléfono inválido."
            )

        if len(valor) < 7 or len(valor) > 15:

            raise ValidacionError(
                "Longitud del teléfono inválida."
            )

        self.__telefono = valor

    def mostrar(self):

        return (
            f"Código     : {self.codigo}\n"
            f"Nombre     : {self.nombre}\n"
            f"Correo     : {self.correo}\n"
            f"Teléfono   : {self.telefono}"
        )