"""
conexion.py
Maneja la conexión con MySQL usando el framework mysql-connector-python.
Los parámetros de conexión se leen desde el archivo .env (no se suben a GitHub).
"""
import os

import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

from datos.auxiliar import ErrorBaseDatos

RUTA_SQL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sql")


class Conexion:
    """Encapsula la conexión y las operaciones básicas contra la base de datos."""

    def __init__(self):
        load_dotenv()
        self._host = os.getenv("DB_HOST", "localhost")
        self._puerto = int(os.getenv("DB_PORT", "3306"))
        self._usuario = os.getenv("DB_USER", "root")
        self._clave = os.getenv("DB_PASSWORD", "")
        self._base = os.getenv("DB_NAME", "turnos_medicos")
        self._conexion = None

    # ------------------------------------------------------------ conexión
    def _parametros(self, con_base=True):
        parametros = {
            "host": self._host,
            "port": self._puerto,
            "user": self._usuario,
            "password": self._clave,
        }
        if con_base:
            parametros["database"] = self._base
        return parametros

    def conectar(self):
        """Abre la conexión si no existe o si se cerró."""
        try:
            if self._conexion is None or not self._conexion.is_connected():
                self._conexion = mysql.connector.connect(**self._parametros())
            return self._conexion
        except Error as error:
            raise ErrorBaseDatos(f"No se pudo conectar a la base de datos: {self._traducir_error(error)}")

    def cerrar(self):
        if self._conexion is not None and self._conexion.is_connected():
            self._conexion.close()
        self._conexion = None

    def probar_conexion(self):
        try:
            self.conectar()
            return True
        except ErrorBaseDatos:
            return False

    # ----------------------------------------------------------- consultas
    def consultar(self, sql, parametros=None):
        """Ejecuta un SELECT y devuelve una lista de diccionarios (una por fila)."""
        cursor = None
        try:
            cursor = self.conectar().cursor(dictionary=True)
            cursor.execute(sql, parametros or [])
            return cursor.fetchall()
        except Error as error:
            raise ErrorBaseDatos(self._traducir_error(error))
        finally:
            if cursor is not None:
                cursor.close()

    def ejecutar(self, sql, parametros=None):
        """Ejecuta INSERT / UPDATE / DELETE. Devuelve (id insertado o filas afectadas)."""
        cursor = None
        conexion = self.conectar()
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, parametros or [])
            conexion.commit()
            if cursor.lastrowid:
                return cursor.lastrowid
            return cursor.rowcount
        except Error as error:
            conexion.rollback()
            raise ErrorBaseDatos(self._traducir_error(error))
        finally:
            if cursor is not None:
                cursor.close()

    # ------------------------------------------------------ scripts SQL
    def ejecutar_script(self, nombre_archivo):
        """Ejecuta un archivo .sql de la carpeta datos/sql (crea BD, tablas y datos)."""
        ruta = os.path.join(RUTA_SQL, nombre_archivo)
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
        except OSError as error:
            raise ErrorBaseDatos(f"No se pudo leer el script {nombre_archivo}: {error}")

        lineas = []
        for linea in contenido.splitlines():
            if not linea.strip().startswith("--"):
                lineas.append(linea)
        sentencias = "\n".join(lineas).split(";")

        conexion = None
        cursor = None
        try:
            # Sin base de datos: el propio script hace CREATE DATABASE y USE.
            conexion = mysql.connector.connect(**self._parametros(con_base=False))
            cursor = conexion.cursor()
            for sentencia in sentencias:
                if sentencia.strip() != "":
                    cursor.execute(sentencia)
            conexion.commit()
        except Error as error:
            raise ErrorBaseDatos(f"Error al ejecutar {nombre_archivo}: {self._traducir_error(error)}")
        finally:
            if cursor is not None:
                cursor.close()
            if conexion is not None:
                conexion.close()

    # --------------------------------------------------------- utilidades
    @staticmethod
    def _traducir_error(error):
        """Convierte errores técnicos de MySQL en mensajes entendibles."""
        if error.errno == 1062:
            return "Ya existe un registro con ese valor (dato duplicado)."
        if error.errno == 1451:
            return "No se puede eliminar: el registro está siendo usado por otros datos."
        if error.errno == 1452:
            return "El registro relacionado (llave foránea) no existe."
        if error.errno == 1045:
            return "Usuario o contraseña incorrectos. Revise el archivo .env."
        if error.errno == 1049:
            return "La base de datos no existe. Use la opción 'Inicializar base de datos' del menú."
        return str(error)
