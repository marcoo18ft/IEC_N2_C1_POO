from datos.modelos.profesional import Profesional
from presentacion.entrada import pedir_dato
from presentacion.menu_crud import MenuCrud


class MenuProfesional(MenuCrud):

    def __init__(self, negocio, especialidad_negocio):
        super().__init__("Profesionales", negocio)
        self._especialidad_negocio = especialidad_negocio

    def pedir_modelo(self, existente=None):
        e = existente
        rut = pedir_dato("RUT", "rut", e.rut if e else None)
        nombres = pedir_dato("Nombres", "texto", e.nombres if e else None)
        apellidos = pedir_dato("Apellidos", "texto", e.apellidos if e else None)
        print("\nEspecialidades disponibles:")
        self.mostrar_lista(self._especialidad_negocio.listar())
        id_especialidad = pedir_dato("ID de la especialidad", "id", e.id_especialidad if e else None)
        telefono = pedir_dato("Teléfono", "telefono", e.telefono if e else None)
        email = pedir_dato("Email", "email", e.email if e else None)
        return Profesional(rut, nombres, apellidos, id_especialidad, telefono, email)

    def opciones_extra(self):
        return {"6": "Consultar agenda de un profesional",
                "7": "Agendar hora (reservar cita)"}

    def ejecutar_extra(self, opcion):
        if opcion == "6":
            id_profesional = pedir_dato("ID del profesional", "id")
            self.mostrar_lista(self._negocio.consultar_agenda(id_profesional))
        elif opcion == "7":
            id_profesional = pedir_dato("ID del profesional", "id")
            id_paciente = pedir_dato("ID del paciente", "id")
            observaciones = pedir_dato("Observaciones (opcional)", "texto_opcional")
            cita = self._negocio.agendar_hora(id_profesional, id_paciente, observaciones)
            print(f"\n✔ Hora agendada. Cita ID {cita.id} (Reservada).")
