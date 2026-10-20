"""
catalogo.py
Clase abstracta para las entidades tipo "catálogo" (nombre + descripción).
Especialidad y Estado heredan de ella.
"""
from abc import abstractmethod

from datos.auxiliar import validar_texto
from datos.modelos.base import ModeloBase


class Catalogo(ModeloBase):

    def __init__(self, nombre, descripcion="", id_registro=None, habilitado=True):
        super().__init__(id_registro, habilitado)
        self.nombre = nombre
        self.descripcion = descripcion

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = validar_texto(valor, "nombre", 100)

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, valor):
        self.__descripcion = validar_texto(valor, "descripcion", 255, obligatorio=False)

    @abstractmethod
    def a_diccionario(self):
        """Cada hijo usa sus propios nombres de columna."""
