from datos.auxiliar import formatear_fecha, validar_fecha_nacimiento
from datos.modelos.persona import Persona


class Paciente(Persona):

    def __init__(self, rut, nombres, apellidos, fecha_nacimiento, telefono, email,
                 id_paciente=None, habilitado=True):
        super().__init__(rut, nombres, apellidos, telefono, email, id_paciente, habilitado)
        self.fecha_nacimiento = fecha_nacimiento

    @property
    def id_paciente(self):
        return self._id

    @property
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, valor):
        self.__fecha_nacimiento = validar_fecha_nacimiento(valor)

    def a_diccionario(self):
        datos = self._datos_persona()
        datos["fecha_nacimiento"] = self.fecha_nacimiento
        return datos

    def mostrar(self):
        return (f"[{self.id}] {self.nombre_completo} | RUT {self.rut} | "
                f"Nac: {formatear_fecha(self.fecha_nacimiento)} | {self.telefono} | {self.email} | "
                f"Habilitado: {self._texto_habilitado()}")
