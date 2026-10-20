from datos.modelos.estado import Estado
from datos.repositorio.repositorio_base import RepositorioBase


class EstadoRepositorio(RepositorioBase):
    TABLA = "estado"
    COLUMNA_ID = "id_estado"

    def _a_modelo(self, fila):
        return Estado(
            estado=fila["estado"],
            descripcion=fila["descripcion"],
            id_estado=fila["id_estado"],
            habilitado=fila["habilitado"],
        )

    def buscar_por_nombre(self, nombre):
        resultado = self.buscar_por("estado", nombre)
        if len(resultado) == 0:
            return None
        return resultado[0]
