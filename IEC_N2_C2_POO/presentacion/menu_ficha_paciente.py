from datos.modelos.ficha_paciente import FichaPaciente
from presentacion.entrada import pedir_dato
from presentacion.menu_crud import MenuCrud


class MenuFichaPaciente(MenuCrud):

    def __init__(self, negocio):
        super().__init__("Fichas de pacientes", negocio)

    def pedir_modelo(self, existente=None):
        e = existente
        id_paciente = pedir_dato("ID del paciente", "id", e.id_paciente if e else None)
        motivo = pedir_dato("Motivo de consulta", "texto_largo", e.motivo if e else None)
        diagnostico = pedir_dato("Diagnóstico (opcional)", "texto_opcional", e.diagnostico if e else None)
        tratamiento = pedir_dato("Tratamiento (opcional)", "texto_opcional", e.tratamiento if e else None)
        return FichaPaciente(id_paciente, motivo, diagnostico, tratamiento)

    def opciones_extra(self):
        return {"6": "Consultar ficha de un paciente"}

    def ejecutar_extra(self, opcion):
        if opcion == "6":
            id_paciente = pedir_dato("ID del paciente", "id")
            print(self._negocio.consultar_ficha(id_paciente).mostrar())
