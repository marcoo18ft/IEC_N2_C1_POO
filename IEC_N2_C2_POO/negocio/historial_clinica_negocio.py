from datos.auxiliar import ErrorValidacion
from negocio.negocio_base import NegocioBase


class HistorialClinicaNegocio(NegocioBase):

    def __init__(self, historial_repositorio, ficha_repositorio, cita_repositorio):
        super().__init__(historial_repositorio)
        self._ficha_repositorio = ficha_repositorio
        self._cita_repositorio = cita_repositorio

    def _validar_antes_de_guardar(self, historial):
        ficha = self._ficha_repositorio.obtener_por_id(historial.id_ficha)
        if ficha is None:
            raise ErrorValidacion(f"No existe una ficha con ID {historial.id_ficha}.")
        if ficha.id_paciente != historial.id_paciente:
            raise ErrorValidacion("La ficha indicada no pertenece a ese paciente.")
        cita = self._cita_repositorio.obtener_por_id(historial.id_cita)
        if cita is None:
            raise ErrorValidacion(f"No existe una cita con ID {historial.id_cita}.")
        if cita.id_paciente != historial.id_paciente:
            raise ErrorValidacion("La cita indicada no pertenece a ese paciente.")

    def registrar_historial(self, historial):
        return self.agregar(historial)

    def consultar_historial(self, id_paciente):
        return self._repositorio.listar_por_paciente(id_paciente)

    def modificar_historial(self, historial):
        self.modificar(historial)
