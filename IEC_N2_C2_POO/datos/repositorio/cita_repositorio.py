from datos.modelos.cita import Cita
from datos.repositorio.repositorio_base import RepositorioBase


class CitaRepositorio(RepositorioBase):
    TABLA = "cita"
    COLUMNA_ID = "id_cita"
    USA_HABILITADO = False   # la tabla cita no tiene columna habilitado

    def _a_modelo(self, fila):
        return Cita(
            id_paciente=fila["id_paciente"],
            id_profesional=fila["id_profesional"],
            id_estado=fila["id_estado"],
            observaciones=fila["observaciones"],
            id_cita=fila["id_cita"],
            fecha_registro=fila["fecha_registro"],
        )

    def listar_por_paciente(self, id_paciente):
        return self.buscar_por("id_paciente", id_paciente)

    def listar_por_profesional(self, id_profesional):
        return self.buscar_por("id_profesional", id_profesional)
