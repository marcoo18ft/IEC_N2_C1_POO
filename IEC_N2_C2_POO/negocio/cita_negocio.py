from datos.auxiliar import ErrorValidacion
from datos.modelos.cita import Cita
from negocio.negocio_base import NegocioBase

ESTADO_RESERVADA = "Reservada"
ESTADO_CONFIRMADA = "Confirmada"
ESTADO_CANCELADA = "Cancelada"


class CitaNegocio(NegocioBase):

    def __init__(self, cita_repositorio, paciente_repositorio, profesional_repositorio, estado_repositorio):
        super().__init__(cita_repositorio)
        self._paciente_repositorio = paciente_repositorio
        self._profesional_repositorio = profesional_repositorio
        self._estado_repositorio = estado_repositorio

    def _validar_antes_de_guardar(self, cita):
        self._exigir_habilitado(self._paciente_repositorio, cita.id_paciente, "El paciente")
        self._exigir_habilitado(self._profesional_repositorio, cita.id_profesional, "El profesional")
        self._exigir_habilitado(self._estado_repositorio, cita.id_estado, "El estado")

    def _id_estado(self, nombre):
        estado = self._estado_repositorio.buscar_por_nombre(nombre)
        if estado is None:
            raise ErrorValidacion(
                f"No existe el estado '{nombre}'. Use 'Inicializar base de datos' en el menú principal.")
        return estado.id

    def reservar(self, id_paciente, id_profesional, observaciones=""):
        # Sobrecarga en Python: se puede llamar con 2 o con 3 argumentos (valor por defecto).
        cita = Cita(id_paciente, id_profesional, self._id_estado(ESTADO_RESERVADA), observaciones)
        self.agregar(cita)
        return cita

    def confirmar(self, id_cita):
        self._cambiar_estado(id_cita, ESTADO_CONFIRMADA, [ESTADO_RESERVADA])

    def cancelar(self, id_cita):
        self._cambiar_estado(id_cita, ESTADO_CANCELADA, [ESTADO_RESERVADA, ESTADO_CONFIRMADA])

    def _cambiar_estado(self, id_cita, nuevo_estado, estados_permitidos):
        cita = self.obtener(id_cita)
        actual = self._estado_repositorio.obtener_por_id(cita.id_estado)
        if actual.nombre not in estados_permitidos:
            raise ErrorValidacion(
                f"No se puede pasar a '{nuevo_estado}' una cita que está '{actual.nombre}'.")
        cita.id_estado = self._id_estado(nuevo_estado)
        self._repositorio.actualizar(cita)

    def listar_por_paciente(self, id_paciente):
        return self._repositorio.listar_por_paciente(id_paciente)

    def listar_citas(self, id_paciente=None, id_profesional=None):
        """Sobrecarga en Python: el mismo método filtra por paciente, por profesional,
        por ambos o por ninguno, según los argumentos que reciba."""
        if id_paciente is not None:
            citas = self._repositorio.listar_por_paciente(id_paciente)
        elif id_profesional is not None:
            return self._repositorio.listar_por_profesional(id_profesional)
        else:
            return self._repositorio.listar()
        if id_profesional is None:
            return citas
        filtradas = []
        for cita in citas:
            if cita.id_profesional == id_profesional:
                filtradas.append(cita)
        return filtradas
