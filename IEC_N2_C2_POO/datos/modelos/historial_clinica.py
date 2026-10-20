from datos.auxiliar import formatear_fecha_hora, validar_entero_positivo, validar_texto
from datos.modelos.base import ModeloBase


class HistorialClinica(ModeloBase):

    def __init__(self, id_ficha, id_paciente, id_cita, motivo, diagnostico="", tratamiento="",
                 observaciones="", id_historial=None, fecha_actualizacion=None):
        super().__init__(id_historial, True)
        self.id_ficha = id_ficha
        self.id_paciente = id_paciente
        self.id_cita = id_cita
        self.motivo = motivo
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
        self.observaciones = observaciones
        self.__fecha_actualizacion = fecha_actualizacion  # la asigna la BD (solo lectura)

    @property
    def id_historial(self):
        return self._id

    @property
    def id_ficha(self):
        return self.__id_ficha

    @id_ficha.setter
    def id_ficha(self, valor):
        self.__id_ficha = validar_entero_positivo(valor, "id_ficha")

    @property
    def id_paciente(self):
        return self.__id_paciente

    @id_paciente.setter
    def id_paciente(self, valor):
        self.__id_paciente = validar_entero_positivo(valor, "id_paciente")

    @property
    def id_cita(self):
        return self.__id_cita

    @id_cita.setter
    def id_cita(self, valor):
        self.__id_cita = validar_entero_positivo(valor, "id_cita")

    @property
    def motivo(self):
        return self.__motivo

    @motivo.setter
    def motivo(self, valor):
        self.__motivo = validar_texto(valor, "motivo", 255)

    @property
    def diagnostico(self):
        return self.__diagnostico

    @diagnostico.setter
    def diagnostico(self, valor):
        self.__diagnostico = validar_texto(valor, "diagnostico", 255, obligatorio=False)

    @property
    def tratamiento(self):
        return self.__tratamiento

    @tratamiento.setter
    def tratamiento(self, valor):
        self.__tratamiento = validar_texto(valor, "tratamiento", 255, obligatorio=False)

    @property
    def observaciones(self):
        return self.__observaciones

    @observaciones.setter
    def observaciones(self, valor):
        self.__observaciones = validar_texto(valor, "observaciones", 255, obligatorio=False)

    @property
    def fecha_actualizacion(self):
        return self.__fecha_actualizacion

    def a_diccionario(self):
        return {
            "id_ficha": self.id_ficha,
            "id_paciente": self.id_paciente,
            "id_cita": self.id_cita,
            "motivo": self.motivo,
            "diagnostico": self.diagnostico,
            "tratamiento": self.tratamiento,
            "observaciones": self.observaciones,
        }

    def mostrar(self):
        return (f"[{self.id}] Ficha ID: {self.id_ficha} | Paciente ID: {self.id_paciente} | "
                f"Cita ID: {self.id_cita} | Motivo: {self.motivo} | Diagnóstico: {self.diagnostico} | "
                f"Tratamiento: {self.tratamiento} | Obs: {self.observaciones} | "
                f"Actualizado: {formatear_fecha_hora(self.fecha_actualizacion)}")
