from datos.auxiliar import validar_entero_positivo, validar_texto
from datos.modelos.base import ModeloBase


class FichaPaciente(ModeloBase):

    def __init__(self, id_paciente, motivo, diagnostico="", tratamiento="", id_ficha=None):
        super().__init__(id_ficha, True)
        self.id_paciente = id_paciente
        self.motivo = motivo
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento

    @property
    def id_ficha(self):
        return self._id

    @property
    def id_paciente(self):
        return self.__id_paciente

    @id_paciente.setter
    def id_paciente(self, valor):
        self.__id_paciente = validar_entero_positivo(valor, "id_paciente")

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

    def a_diccionario(self):
        return {
            "id_paciente": self.id_paciente,
            "motivo": self.motivo,
            "diagnostico": self.diagnostico,
            "tratamiento": self.tratamiento,
        }

    def mostrar(self):
        return (f"[{self.id}] Paciente ID: {self.id_paciente} | Motivo: {self.motivo} | "
                f"Diagnóstico: {self.diagnostico} | Tratamiento: {self.tratamiento}")
