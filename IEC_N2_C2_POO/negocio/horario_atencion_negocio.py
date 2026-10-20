from datos.auxiliar import ErrorValidacion, hora_a_minutos
from negocio.negocio_base import NegocioBase


class HorarioAtencionNegocio(NegocioBase):

    def __init__(self, horario_repositorio, profesional_repositorio):
        super().__init__(horario_repositorio)
        self._profesional_repositorio = profesional_repositorio

    def _validar_antes_de_guardar(self, horario):
        self._exigir_habilitado(self._profesional_repositorio, horario.id_profesional, "El profesional")

        # Regla: un profesional no puede tener dos jornadas que se solapen el mismo día.
        for otro in self._repositorio.listar_por_profesional(horario.id_profesional):
            if otro.id == horario.id or otro.fecha != horario.fecha:
                continue
            inicia_antes_de_terminar = hora_a_minutos(horario.hora_inicio) < hora_a_minutos(otro.hora_fin)
            termina_despues_de_iniciar = hora_a_minutos(horario.hora_fin) > hora_a_minutos(otro.hora_inicio)
            if inicia_antes_de_terminar and termina_despues_de_iniciar:
                raise ErrorValidacion(
                    f"La jornada se solapa con otra del mismo día ({otro.hora_inicio} - {otro.hora_fin}).")

    def registrar_jornada(self, horario):
        return self.agregar(horario)

    def modificar_jornada(self, horario):
        self.modificar(horario)
