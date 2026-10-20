from datos.auxiliar import formatear_hora
from datos.modelos.horario_atencion import HorarioAtencion
from datos.repositorio.repositorio_base import RepositorioBase


class HorarioAtencionRepositorio(RepositorioBase):
    TABLA = "horario_atencion"
    COLUMNA_ID = "id_horario"

    def _a_modelo(self, fila):
        return HorarioAtencion(
            id_profesional=fila["id_profesional"],
            fecha=fila["fecha"],
            hora_inicio=formatear_hora(fila["hora_inicio"]),
            hora_fin=formatear_hora(fila["hora_fin"]),
            duracion_bloque=fila["duracion_bloque"],
            id_horario=fila["id_horario"],
            habilitado=fila["habilitado"],
        )

    def listar_por_profesional(self, id_profesional):
        sql = ("SELECT * FROM horario_atencion WHERE id_profesional = %s AND habilitado = 1 "
               "ORDER BY fecha, hora_inicio")
        return self._convertir(self._conexion.consultar(sql, [id_profesional]))
