from datos.modelos.especialidad import Especialidad
from datos.repositorio.repositorio_base import RepositorioBase


class EspecialidadRepositorio(RepositorioBase):
    TABLA = "especialidad"
    COLUMNA_ID = "id_especialidad"

    def _a_modelo(self, fila):
        return Especialidad(
            especialidad=fila["especialidad"],
            descripcion=fila["descripcion"],
            id_especialidad=fila["id_especialidad"],
            habilitado=fila["habilitado"],
        )
