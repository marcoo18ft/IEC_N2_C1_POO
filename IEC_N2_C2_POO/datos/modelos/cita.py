from datos.auxiliar import formatear_fecha_hora, validar_entero_positivo, validar_texto
from datos.modelos.base import ModeloBase


class Cita(ModeloBase):

    def __init__(self, id_paciente, id_profesional, id_estado, observaciones="",
                 id_cita=None, fecha_registro=None):
        super().__init__(id_cita, True)
        self.id_paciente = id_paciente
        self.id_profesional = id_profesional
        self.id_estado = id_estado
        self.observaciones = observaciones
        self.__fecha_registro = fecha_registro  # la asigna la BD (solo lectura)

    @property
    def id_cita(self):
        return self._id

    @property
    def id_paciente(self):
        return self.__id_paciente

    @id_paciente.setter
    def id_paciente(self, valor):
        self.__id_paciente = validar_entero_positivo(valor, "id_paciente")

    @property
    def id_profesional(self):
        return self.__id_profesional

    @id_profesional.setter
    def id_profesional(self, valor):
        self.__id_profesional = validar_entero_positivo(valor, "id_profesional")

    @property
    def id_estado(self):
        return self.__id_estado

    @id_estado.setter
    def id_estado(self, valor):
        self.__id_estado = validar_entero_positivo(valor, "id_estado")

    @property
    def observaciones(self):
        return self.__observaciones

    @observaciones.setter
    def observaciones(self, valor):
        self.__observaciones = validar_texto(valor, "observaciones", 255, obligatorio=False)

    @property
    def fecha_registro(self):
        return self.__fecha_registro

    def a_diccionario(self):
        return {
            "id_paciente": self.id_paciente,
            "id_profesional": self.id_profesional,
            "id_estado": self.id_estado,
            "observaciones": self.observaciones,
        }

    def mostrar(self):
        return (f"[{self.id}] Paciente ID: {self.id_paciente} | Profesional ID: {self.id_profesional} | "
                f"Estado ID: {self.id_estado} | Registrada: {formatear_fecha_hora(self.fecha_registro)} | "
                f"Obs: {self.observaciones}")
