from abc import ABC, abstractmethod

from modelos.entidad import Entidad
from excepciones.excepciones import ValidacionError


class Servicio(Entidad, ABC):

    def __init__(self, codigo, nombre, costo_base):

        super().__init__(codigo)

        self.nombre = nombre
        self.costo_base = costo_base

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):

        valor = valor.strip()

        if len(valor) < 3:

            raise ValidacionError(
                "Nombre del servicio inválido."
            )

        self.__nombre = valor.title()

    @property
    def costo_base(self):
        return self.__costo_base

    @costo_base.setter
    def costo_base(self, valor):

        if valor <= 0:

            raise ValidacionError(
                "El costo debe ser mayor que cero."
            )

        self.__costo_base = float(valor)

    @abstractmethod
    def calcular_costo(self, *args):
        pass

    @abstractmethod
    def descripcion(self):
        pass

    def mostrar(self):

        return (
            f"Código      : {self.codigo}\n"
            f"Servicio    : {self.nombre}\n"
            f"Costo Base  : ${self.costo_base:,.0f}"
        )