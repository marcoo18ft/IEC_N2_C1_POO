"""
menu_crud.py
Clase abstracta con el menú CRUD que comparten todas las entidades.
Cada menú hijo define cómo pedir los datos (pedir_modelo) y, si necesita,
opciones extra del diagrama (opciones_extra / ejecutar_extra).
"""
from abc import ABC, abstractmethod

from datos.auxiliar import ErrorBaseDatos, ErrorValidacion
from presentacion.entrada import pausar, pedir_dato, pedir_si_no


class MenuCrud(ABC):

    def __init__(self, titulo, negocio):
        self._titulo = titulo
        self._negocio = negocio

    @property
    def titulo(self):
        return self._titulo

    @abstractmethod
    def pedir_modelo(self, existente=None):
        """Pide los datos por consola y devuelve el objeto. Si hay 'existente', ENTER conserva su valor."""

    def opciones_extra(self):
        """Devuelve {'6': 'texto'} con opciones adicionales (por defecto ninguna)."""
        return {}

    def ejecutar_extra(self, opcion):
        """Ejecuta la opción extra elegida (los hijos lo sobrescriben)."""
        return None

    # ----------------------------------------------------------- menú
    def ejecutar(self):
        while True:
            self._mostrar_menu()
            opcion = input("Seleccione una opción: ").strip()
            if opcion == "0":
                return
            try:
                self._procesar(opcion)
            except (ErrorValidacion, ErrorBaseDatos) as error:
                print(f"\n⚠ {error}")
            pausar()

    def _mostrar_menu(self):
        print(f"\n===== {self._titulo.upper()} =====")
        print("1. Agregar")
        print("2. Listar")
        print("3. Buscar por ID")
        print("4. Modificar")
        print("5. Eliminar")
        extras = self.opciones_extra()
        for numero in extras:
            print(f"{numero}. {extras[numero]}")
        print("0. Volver")

    def _procesar(self, opcion):
        if opcion == "1":
            self._agregar()
        elif opcion == "2":
            self._listar()
        elif opcion == "3":
            self._buscar()
        elif opcion == "4":
            self._modificar()
        elif opcion == "5":
            self._eliminar()
        elif opcion in self.opciones_extra():
            self.ejecutar_extra(opcion)
        else:
            print("Opción inválida.")

    # ----------------------------------------------------------- CRUD
    def _agregar(self):
        modelo = self.pedir_modelo()
        nuevo_id = self._negocio.agregar(modelo)
        print(f"\n✔ Registro agregado con ID {nuevo_id}.")

    def _listar(self):
        self.mostrar_lista(self._negocio.listar())

    def _buscar(self):
        id_registro = pedir_dato("ID a buscar", "id")
        print(self._negocio.obtener(id_registro).mostrar())

    def _modificar(self):
        id_registro = pedir_dato("ID a modificar", "id")
        existente = self._negocio.obtener(id_registro)
        print(existente.mostrar())
        print("(ENTER mantiene el valor entre corchetes)")
        modelo = self.pedir_modelo(existente)
        modelo.id = existente.id
        modelo.habilitado = existente.habilitado
        self._negocio.modificar(modelo)
        print("\n✔ Registro modificado.")

    def _eliminar(self):
        id_registro = pedir_dato("ID a eliminar", "id")
        registro = self._negocio.obtener(id_registro)
        print(registro.mostrar())
        if pedir_si_no("¿Confirma la eliminación?"):
            self._negocio.eliminar(id_registro)
            print("\n✔ Registro eliminado.")
        else:
            print("Operación cancelada.")

    @staticmethod
    def mostrar_lista(registros):
        if len(registros) == 0:
            print("\nNo hay registros.")
            return
        print()
        for registro in registros:
            print(registro.mostrar())
