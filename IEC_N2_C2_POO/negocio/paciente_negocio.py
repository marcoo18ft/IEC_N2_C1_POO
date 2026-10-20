from negocio.negocio_base import NegocioBase


class PacienteNegocio(NegocioBase):

    def __init__(self, paciente_repositorio, historial_repositorio, cita_negocio):
        super().__init__(paciente_repositorio)
        self._historial_repositorio = historial_repositorio
        self._cita_negocio = cita_negocio

    def solicitar_cita(self, id_paciente, id_profesional, observaciones=""):
        return self._cita_negocio.reservar(id_paciente, id_profesional, observaciones)

    def consultar_historial(self, id_paciente):
        self.obtener(id_paciente)
        return self._historial_repositorio.listar_por_paciente(id_paciente)
