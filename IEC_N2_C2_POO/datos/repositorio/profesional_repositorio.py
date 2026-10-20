from datos.modelos.profesional import Profesional
from datos.repositorio.repositorio_base import RepositorioBase


class ProfesionalRepositorio(RepositorioBase):
    TABLA = "profesional"
    COLUMNA_ID = "id_profesional"

    def _a_modelo(self, fila):
        return Profesional(
            rut=fila["rut"],
            nombres=fila["nombres"],
            apellidos=fila["apellidos"],
            id_especialidad=fila["id_especialidad"],
            telefono=fila["telefono"],
            email=fila["email"],
            id_profesional=fila["id_profesional"],
            habilitado=fila["habilitado"],
        )

    def listar_por_especialidad(self, id_especialidad):
        return self.buscar_por("id_especialidad", id_especialidad)
