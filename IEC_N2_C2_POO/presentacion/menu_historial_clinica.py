from datos.modelos.historial_clinica import HistorialClinica
from presentacion.entrada import pedir_dato
from presentacion.menu_crud import MenuCrud


class MenuHistorialClinica(MenuCrud):

    def __init__(self, negocio):
        super().__init__("Historial clínico", negocio)

    def pedir_modelo(self, existente=None):
        e = existente
        id_ficha = pedir_dato("ID de la ficha", "id", e.id_ficha if e else None)
        id_paciente = pedir_dato("ID del paciente", "id", e.id_paciente if e else None)
        id_cita = pedir_dato("ID de la cita", "id", e.id_cita if e else None)
        motivo = pedir_dato("Motivo", "texto_largo", e.motivo if e else None)
        diagnostico = pedir_dato("Diagnóstico (opcional)", "texto_opcional", e.diagnostico if e else None)
        tratamiento = pedir_dato("Tratamiento (opcional)", "texto_opcional", e.tratamiento if e else None)
        observaciones = pedir_dato("Observaciones (opcional)", "texto_opcional", e.observaciones if e else None)
        return HistorialClinica(id_ficha, id_paciente, id_cita, motivo, diagnostico, tratamiento, observaciones)

    def opciones_extra(self):
        return {"6": "Consultar historial de un paciente"}

    def ejecutar_extra(self, opcion):
        if opcion == "6":
            id_paciente = pedir_dato("ID del paciente", "id")
            self.mostrar_lista(self._negocio.consultar_historial(id_paciente))
