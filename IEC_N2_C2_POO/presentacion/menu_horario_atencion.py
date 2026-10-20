from datos.auxiliar import formatear_fecha
from datos.modelos.horario_atencion import HorarioAtencion
from presentacion.entrada import pedir_dato
from presentacion.menu_crud import MenuCrud


class MenuHorarioAtencion(MenuCrud):

    def __init__(self, negocio):
        super().__init__("Horarios de atención", negocio)

    def pedir_modelo(self, existente=None):
        e = existente
        id_profesional = pedir_dato("ID del profesional", "id", e.id_profesional if e else None)
        fecha_actual = None
        if e:
            fecha_actual = formatear_fecha(e.fecha)
        fecha = pedir_dato("Fecha (dd-mm-aaaa)", "fecha", fecha_actual)
        hora_inicio = pedir_dato("Hora de inicio (HH:MM)", "hora", e.hora_inicio if e else None)
        hora_fin = pedir_dato("Hora de fin (HH:MM)", "hora", e.hora_fin if e else None)
        duracion = pedir_dato("Duración del bloque en minutos", "id", e.duracion_bloque if e else 30)
        return HorarioAtencion(id_profesional, fecha, hora_inicio, hora_fin, duracion)
