from datos.modelos.paciente import Paciente
from datos.repositorio.repositorio_base import RepositorioBase


class PacienteRepositorio(RepositorioBase):
    TABLA = "paciente"
    COLUMNA_ID = "id_paciente"

    def _a_modelo(self, fila):
        return Paciente(
            rut=fila["rut"],
            nombres=fila["nombres"],
            apellidos=fila["apellidos"],
            fecha_nacimiento=fila["fecha_nacimiento"],
            telefono=fila["telefono"],
            email=fila["email"],
            id_paciente=fila["id_paciente"],
            habilitado=fila["habilitado"],
        )
