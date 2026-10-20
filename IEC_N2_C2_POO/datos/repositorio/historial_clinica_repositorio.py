from datos.modelos.historial_clinica import HistorialClinica
from datos.repositorio.repositorio_base import RepositorioBase


class HistorialClinicaRepositorio(RepositorioBase):
    TABLA = "historial_clinica"
    COLUMNA_ID = "id_historial"
    USA_HABILITADO = False

    def _a_modelo(self, fila):
        return HistorialClinica(
            id_ficha=fila["id_ficha"],
            id_paciente=fila["id_paciente"],
            id_cita=fila["id_cita"],
            motivo=fila["motivo"],
            diagnostico=fila["diagnostico"],
            tratamiento=fila["tratamiento"],
            observaciones=fila["observaciones"],
            id_historial=fila["id_historial"],
            fecha_actualizacion=fila["fecha_actualizacion"],
        )

    def listar_por_paciente(self, id_paciente):
        return self.buscar_por("id_paciente", id_paciente)
