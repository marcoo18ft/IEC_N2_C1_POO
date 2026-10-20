from datos.auxiliar import (convertir_fecha, formatear_fecha, hora_a_minutos,
                            validar_entero_positivo, validar_hora, ErrorValidacion)
from datos.modelos.base import ModeloBase


class HorarioAtencion(ModeloBase):

    def __init__(self, id_profesional, fecha, hora_inicio, hora_fin, duracion_bloque=30,
                 id_horario=None, habilitado=True):
        super().__init__(id_horario, habilitado)
        self.id_profesional = id_profesional
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.duracion_bloque = duracion_bloque
        if hora_a_minutos(self.hora_fin) <= hora_a_minutos(self.hora_inicio):
            raise ErrorValidacion("La hora de fin debe ser posterior a la hora de inicio.")

    @property
    def id_horario(self):
        return self._id

    @property
    def id_profesional(self):
        return self.__id_profesional

    @id_profesional.setter
    def id_profesional(self, valor):
        self.__id_profesional = validar_entero_positivo(valor, "id_profesional")

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, valor):
        self.__fecha = convertir_fecha(valor)

    @property
    def hora_inicio(self):
        return self.__hora_inicio

    @hora_inicio.setter
    def hora_inicio(self, valor):
        self.__hora_inicio = validar_hora(valor)

    @property
    def hora_fin(self):
        return self.__hora_fin

    @hora_fin.setter
    def hora_fin(self, valor):
        self.__hora_fin = validar_hora(valor)

    @property
    def duracion_bloque(self):
        return self.__duracion_bloque

    @duracion_bloque.setter
    def duracion_bloque(self, valor):
        self.__duracion_bloque = validar_entero_positivo(valor, "duracion_bloque")

    def a_diccionario(self):
        return {
            "id_profesional": self.id_profesional,
            "fecha": self.fecha,
            "hora_inicio": self.hora_inicio,
            "hora_fin": self.hora_fin,
            "duracion_bloque": self.duracion_bloque,
            "habilitado": int(self.habilitado),
        }

    def mostrar(self):
        return (f"[{self.id}] Profesional ID: {self.id_profesional} | {formatear_fecha(self.fecha)} | "
                f"{self.hora_inicio} - {self.hora_fin} | Bloques de {self.duracion_bloque} min | "
                f"Habilitado: {self._texto_habilitado()}")
