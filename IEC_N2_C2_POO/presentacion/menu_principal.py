"""
menu_principal.py
Menú de nivel superior: permite navegar por los menús CRUD de cada entidad.
"""
from datos.auxiliar import ErrorBaseDatos
from presentacion.entrada import pausar, pedir_si_no


class MenuPrincipal:

    def __init__(self, menus, conexion):
        self._menus = menus          # {"1": MenuCrud, "2": MenuCrud, ...}
        self._conexion = conexion

    def ejecutar(self):
        if not self._conexion.probar_conexion():
            print("\n⚠ No hay conexión con la base de datos.")
            print("  Revise el archivo .env o use la opción 9 para inicializarla.")

        while True:
            print("\n========== SISTEMA DE TURNOS MÉDICOS ==========")
            for numero in self._menus:
                print(f"{numero}. {self._menus[numero].titulo}")
            print("9. Inicializar base de datos (scripts SQL)")
            print("0. Salir")
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "0":
                self._conexion.cerrar()
                print("\nHasta luego.")
                return
            elif opcion in self._menus:
                self._menus[opcion].ejecutar()
            elif opcion == "9":
                self._inicializar_base_datos()
                pausar()
            else:
                print("Opción inválida.")

    def _inicializar_base_datos(self):
        print("\nSe creará la base de datos y las tablas (si no existen) y se cargarán los datos base.")
        if not pedir_si_no("¿Desea continuar?"):
            return
        try:
            self._conexion.ejecutar_script("crear_tablas.sql")
            self._conexion.ejecutar_script("datos_iniciales.sql")
            print("\n✔ Base de datos lista.")
        except ErrorBaseDatos as error:
            print(f"\n⚠ {error}")
