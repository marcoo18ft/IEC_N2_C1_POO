"""
repositorio_base.py
Clase abstracta con el CRUD genérico contra MySQL. Cada repositorio hijo solo
indica su tabla y cómo convertir una fila en objeto (_a_modelo), lo que permite
reutilizar el código (HERENCIA) y que cada hijo lo adapte (POLIMORFISMO).

Los nombres de tabla/columna salen de constantes del código; los VALORES siempre
viajan como parámetros (%s) para evitar inyección SQL.
"""
from abc import ABC, abstractmethod


class RepositorioBase(ABC):
    TABLA = ""
    COLUMNA_ID = ""
    USA_HABILITADO = True   # True: eliminar = baja lógica (habilitado = 0)

    def __init__(self, conexion):
        self._conexion = conexion

    @abstractmethod
    def _a_modelo(self, fila):
        """Convierte una fila (diccionario) de la BD en un objeto del modelo."""

    # ------------------------------------------------------------- CREATE
    def crear(self, modelo):
        datos = modelo.a_diccionario()
        columnas = ", ".join(datos.keys())
        marcadores = ", ".join(["%s"] * len(datos))
        sql = f"INSERT INTO {self.TABLA} ({columnas}) VALUES ({marcadores})"
        return self._conexion.ejecutar(sql, list(datos.values()))

    # --------------------------------------------------------------- READ
    def obtener_por_id(self, id_registro):
        sql = f"SELECT * FROM {self.TABLA} WHERE {self.COLUMNA_ID} = %s"
        filas = self._conexion.consultar(sql, [id_registro])
        if len(filas) == 0:
            return None
        return self._a_modelo(filas[0])

    def listar(self, solo_habilitados=True):
        sql = f"SELECT * FROM {self.TABLA}"
        if solo_habilitados and self.USA_HABILITADO:
            sql += " WHERE habilitado = 1"
        sql += f" ORDER BY {self.COLUMNA_ID}"
        return self._convertir(self._conexion.consultar(sql))

    def buscar_por(self, columna, valor):
        """Devuelve la lista de registros cuya columna sea igual al valor."""
        sql = f"SELECT * FROM {self.TABLA} WHERE {columna} = %s ORDER BY {self.COLUMNA_ID}"
        return self._convertir(self._conexion.consultar(sql, [valor]))

    # ------------------------------------------------------------- UPDATE
    def actualizar(self, modelo):
        datos = modelo.a_diccionario()
        asignaciones = ", ".join([f"{columna} = %s" for columna in datos])
        sql = f"UPDATE {self.TABLA} SET {asignaciones} WHERE {self.COLUMNA_ID} = %s"
        parametros = list(datos.values())
        parametros.append(modelo.id)
        return self._conexion.ejecutar(sql, parametros)

    def cambiar_habilitado(self, id_registro, habilitado):
        sql = f"UPDATE {self.TABLA} SET habilitado = %s WHERE {self.COLUMNA_ID} = %s"
        return self._conexion.ejecutar(sql, [int(habilitado), id_registro])

    # ------------------------------------------------------------- DELETE
    def eliminar(self, id_registro):
        if self.USA_HABILITADO:
            return self.cambiar_habilitado(id_registro, False)
        sql = f"DELETE FROM {self.TABLA} WHERE {self.COLUMNA_ID} = %s"
        return self._conexion.ejecutar(sql, [id_registro])

    # ---------------------------------------------------------- utilidades
    def _convertir(self, filas):
        modelos = []
        for fila in filas:
            modelos.append(self._a_modelo(fila))
        return modelos
