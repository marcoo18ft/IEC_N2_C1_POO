from datos.auxiliar import ErrorValidacion
from negocio.negocio_base import NegocioBase


class FichaPacienteNegocio(NegocioBase):

    def __init__(self, ficha_repositorio, paciente_repositorio):
        super().__init__(ficha_repositorio)
        self._paciente_repositorio = paciente_repositorio

    def _validar_antes_de_guardar(self, ficha):
        self._exigir_habilitado(self._paciente_repositorio, ficha.id_paciente, "El paciente")
        existente = self._repositorio.obtener_por_paciente(ficha.id_paciente)
        if existente is not None and existente.id != ficha.id:
            raise ErrorValidacion("Ese paciente ya tiene una ficha (relación 1:1).")

    def consultar_ficha(self, id_paciente):
        ficha = self._repositorio.obtener_por_paciente(id_paciente)
        if ficha is None:
            raise ErrorValidacion(f"El paciente {id_paciente} no tiene ficha.")
        return ficha

    def modificar_ficha(self, ficha):
        self.modificar(ficha)

    def anular_ficha(self, id_ficha):
        self.eliminar(id_ficha)
