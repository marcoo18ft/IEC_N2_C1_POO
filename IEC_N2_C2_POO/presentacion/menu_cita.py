from datos.auxiliar import validar_entero_positivo
from datos.modelos.cita import Cita
from presentacion.entrada import pedir_dato
from presentacion.menu_crud import MenuCrud


class MenuCita(MenuCrud):

    def __init__(self, negocio, estado_negocio):
        super().__init__("Citas", negocio)
        self._estado_negocio = estado_negocio

    def pedir_modelo(self, existente=None):
        e = existente
        id_paciente = pedir_dato("ID del paciente", "id", e.id_paciente if e else None)
        id_profesional = pedir_dato("ID del profesional", "id", e.id_profesional if e else None)
        print("\nEstados disponibles:")
        self.mostrar_lista(self._estado_negocio.listar())
        id_estado = pedir_dato("ID del estado", "id", e.id_estado if e else None)
        observaciones = pedir_dato("Observaciones (opcional)", "texto_opcional", e.observaciones if e else None)
        return Cita(id_paciente, id_profesional, id_estado, observaciones)

    def opciones_extra(self):
        return {"6": "Reservar cita (estado Reservada)",
                "7": "Confirmar cita",
                "8": "Cancelar cita",
                "9": "Listar citas por paciente y/o profesional"}

    def ejecutar_extra(self, opcion):
        if opcion == "6":
            id_paciente = pedir_dato("ID del paciente", "id")
            id_profesional = pedir_dato("ID del profesional", "id")
            observaciones = pedir_dato("Observaciones (opcional)", "texto_opcional")
            cita = self._negocio.reservar(id_paciente, id_profesional, observaciones)
            print(f"\n✔ Cita reservada con ID {cita.id}.")
        elif opcion == "7":
            self._negocio.confirmar(pedir_dato("ID de la cita", "id"))
            print("\n✔ Cita confirmada.")
        elif opcion == "8":
            self._negocio.cancelar(pedir_dato("ID de la cita", "id"))
            print("\n✔ Cita cancelada.")
        elif opcion == "9":
            texto_paciente = pedir_dato("ID del paciente (ENTER para omitir)", "texto_opcional")
            texto_profesional = pedir_dato("ID del profesional (ENTER para omitir)", "texto_opcional")
            id_paciente = None
            id_profesional = None
            if texto_paciente != "":
                id_paciente = validar_entero_positivo(texto_paciente, "ID del paciente")
            if texto_profesional != "":
                id_profesional = validar_entero_positivo(texto_profesional, "ID del profesional")
            self.mostrar_lista(self._negocio.listar_citas(id_paciente, id_profesional))
