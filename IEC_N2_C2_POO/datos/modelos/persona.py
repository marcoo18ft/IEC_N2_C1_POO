"""
persona.py
Clase abstracta con los datos comunes de las personas del sistema.
Profesional y Paciente heredan de ella. Los atributos son privados (__rut, ...)
y se acceden por propiedades que validan el dato (ENCAPSULAMIENTO).
El id (_id) es protegido: solo lo usan las clases hijas.
"""
from abc import abstractmethod

from datos.auxiliar import normalizar_rut, validar_email, validar_telefono, validar_texto
from datos.modelos.base import ModeloBase


class Persona(ModeloBase):

    def __init__(self, rut, nombres, apellidos, telefono, email, id_registro=None, habilitado=True):
        super().__init__(id_registro, habilitado)
        self.rut = rut
        self.nombres = nombres
        self.apellidos = apellidos
        self.telefono = telefono
        self.email = email

    @property
    def rut(self):
        return self.__rut

    @rut.setter
    def rut(self, valor):
        self.__rut = normalizar_rut(valor)

    @property
    def nombres(self):
        return self.__nombres

    @nombres.setter
    def nombres(self, valor):
        self.__nombres = validar_texto(valor, "nombres", 100)

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, valor):
        self.__apellidos = validar_texto(valor, "apellidos", 100)

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):
        self.__telefono = validar_telefono(valor)

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valor):
        self.__email = validar_email(valor)

    @property
    def nombre_completo(self):
        return f"{self.__nombres} {self.__apellidos}"

    def _datos_persona(self):
        """Columnas comunes; los hijos agregan las suyas."""
        return {
            "rut": self.rut,
            "nombres": self.nombres,
            "apellidos": self.apellidos,
            "telefono": self.telefono,
            "email": self.email,
            "habilitado": int(self.habilitado),
        }

    @abstractmethod
    def a_diccionario(self):
        """Cada hijo completa los datos con sus atributos propios."""
