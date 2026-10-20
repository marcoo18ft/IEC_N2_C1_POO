from datos.modelos.ficha_paciente import FichaPaciente
from datos.repositorio.repositorio_base import RepositorioBase


class FichaPacienteRepositorio(RepositorioBase):
    TABLA = "ficha_paciente"
    COLUMNA_ID = "id_ficha"
    USA_HABILITADO = False

    def _a_modelo(self, fila):
        return FichaPaciente(
            id_paciente=fila["id_paciente"],
            motivo=fila["motivo"],
            diagnostico=fila["diagnostico"],
            tratamiento=fila["tratamiento"],
            id_ficha=fila["id_ficha"],
        )

    def obtener_por_paciente(self, id_paciente):
        resultado = self.buscar_por("id_paciente", id_paciente)
        if len(resultado) == 0:
            return None
        return resultado[0]
