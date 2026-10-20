from datos.modelos.especialidad import Especialidad
from presentacion.entrada import pedir_dato
from presentacion.menu_crud import MenuCrud


class MenuEspecialidad(MenuCrud):

    def __init__(self, negocio):
        super().__init__("Especialidades", negocio)

    def pedir_modelo(self, existente=None):
        e = existente
        nombre = pedir_dato("Nombre de la especialidad", "texto", e.nombre if e else None)
        descripcion = pedir_dato("Descripción (opcional)", "texto_opcional", e.descripcion if e else None)
        return Especialidad(nombre, descripcion)
