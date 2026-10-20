from datos.modelos.estado import Estado
from presentacion.entrada import pedir_dato, pedir_si_no
from presentacion.menu_crud import MenuCrud


class MenuEstado(MenuCrud):

    def __init__(self, negocio):
        super().__init__("Estados de cita", negocio)

    def pedir_modelo(self, existente=None):
        e = existente
        nombre = pedir_dato("Nombre del estado", "texto", e.nombre if e else None)
        descripcion = pedir_dato("Descripción (opcional)", "texto_opcional", e.descripcion if e else None)
        return Estado(nombre, descripcion)

    def opciones_extra(self):
        return {"6": "Habilitar / deshabilitar un estado"}

    def ejecutar_extra(self, opcion):
        if opcion == "6":
            id_estado = pedir_dato("ID del estado", "id")
            estado = self._negocio.obtener_estado(id_estado)
            print(estado.mostrar())
            habilitar = pedir_si_no("¿Habilitar el estado? (n = deshabilitar)")
            self._negocio.cambiar_estado(id_estado, habilitar)
            print("\n✔ Estado actualizado.")
