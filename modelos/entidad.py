from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase base abstracta del sistema.
    """

    def __init__(self, codigo):
        self.codigo = codigo

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):

        valor = str(valor).strip()

        if valor == "":
            raise ValueError(
                "El código no puede estar vacío."
            )

        self.__codigo = valor

    @abstractmethod
    def mostrar(self):
        pass

    def __str__(self):
        return self.codigo