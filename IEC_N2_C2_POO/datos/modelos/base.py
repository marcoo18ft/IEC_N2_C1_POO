"""
base.py
Clase abstracta de la que heredan todos los modelos (HERENCIA + ABSTRACCIÓN).
Guarda lo que comparten todas las entidades: el id y el estado habilitado.
"""
from abc import ABC, abstractmethod


class ModeloBase(ABC):

    def __init__(self, id_registro=None, habilitado=True):
        self._id = id_registro
        self.__habilitado = bool(habilitado)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        self._id = valor

    @property
    def habilitado(self):
        return self.__habilitado

    @habilitado.setter
    def habilitado(self, valor):
        self.__habilitado = bool(valor)

    @abstractmethod
    def a_diccionario(self):
        """Devuelve {columna: valor} para guardar en la BD (sin el id)."""

    @abstractmethod
    def mostrar(self):
        """Devuelve el texto que se muestra en consola (cada modelo lo redefine)."""

    def _texto_habilitado(self):
        if self.__habilitado:
            return "Sí"
        return "No"

    def __str__(self):
        return self.mostrar()
