from datos.auxiliar import validar_entero_positivo
from datos.modelos.persona import Persona


class Profesional(Persona):

    def __init__(self, rut, nombres, apellidos, id_especialidad, telefono, email,
                 id_profesional=None, habilitado=True):
        super().__init__(rut, nombres, apellidos, telefono, email, id_profesional, habilitado)
        self.id_especialidad = id_especialidad

    @property
    def id_profesional(self):
        return self._id

    @property
    def id_especialidad(self):
        return self.__id_especialidad

    @id_especialidad.setter
    def id_especialidad(self, valor):
        self.__id_especialidad = validar_entero_positivo(valor, "id_especialidad")

    def a_diccionario(self):
        datos = self._datos_persona()
        datos["id_especialidad"] = self.id_especialidad
        return datos

    def mostrar(self):
        return (f"[{self.id}] {self.nombre_completo} | RUT {self.rut} | "
                f"Especialidad ID: {self.id_especialidad} | {self.telefono} | {self.email} | "
                f"Habilitado: {self._texto_habilitado()}")
