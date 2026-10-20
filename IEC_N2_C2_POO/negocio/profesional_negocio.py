from negocio.negocio_base import NegocioBase


class ProfesionalNegocio(NegocioBase):

    def __init__(self, profesional_repositorio, especialidad_repositorio, horario_repositorio, cita_negocio):
        super().__init__(profesional_repositorio)
        self._especialidad_repositorio = especialidad_repositorio
        self._horario_repositorio = horario_repositorio
        self._cita_negocio = cita_negocio

    def _validar_antes_de_guardar(self, profesional):
        self._exigir_habilitado(self._especialidad_repositorio, profesional.id_especialidad,
                                "La especialidad")

    def consultar_agenda(self, id_profesional):
        """Devuelve las jornadas habilitadas del profesional, ordenadas por fecha."""
        self.obtener(id_profesional)
        return self._horario_repositorio.listar_por_profesional(id_profesional)

    def agendar_hora(self, id_profesional, id_paciente, observaciones=""):
        """Crea una cita en estado Reservada para el profesional."""
        return self._cita_negocio.reservar(id_paciente, id_profesional, observaciones)
