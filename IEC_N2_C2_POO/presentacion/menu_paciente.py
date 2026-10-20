from datos.modelos.paciente import Paciente
from presentacion.entrada import pedir_dato
from presentacion.menu_crud import MenuCrud


class MenuPaciente(MenuCrud):

    def __init__(self, negocio):
        super().__init__("Pacientes", negocio)

    def pedir_modelo(self, existente=None):
        e = existente
        rut = pedir_dato("RUT", "rut", e.rut if e else None)
        nombres = pedir_dato("Nombres", "texto", e.nombres if e else None)
        apellidos = pedir_dato("Apellidos", "texto", e.apellidos if e else None)
        nacimiento_actual = None
        if e:
            nacimiento_actual = e.fecha_nacimiento.strftime("%d-%m-%Y")
        fecha_nacimiento = pedir_dato("Fecha de nacimiento (dd-mm-aaaa)", "fecha_nacimiento", nacimiento_actual)
        telefono = pedir_dato("Teléfono", "telefono", e.telefono if e else None)
        email = pedir_dato("Email", "email", e.email if e else None)
        return Paciente(rut, nombres, apellidos, fecha_nacimiento, telefono, email)

    def opciones_extra(self):
        return {"6": "Solicitar cita",
                "7": "Consultar historial clínico"}

    def ejecutar_extra(self, opcion):
        if opcion == "6":
            id_paciente = pedir_dato("ID del paciente", "id")
            id_profesional = pedir_dato("ID del profesional", "id")
            observaciones = pedir_dato("Observaciones (opcional)", "texto_opcional")
            cita = self._negocio.solicitar_cita(id_paciente, id_profesional, observaciones)
            print(f"\n✔ Cita solicitada. Cita ID {cita.id} (Reservada).")
        elif opcion == "7":
            id_paciente = pedir_dato("ID del paciente", "id")
            self.mostrar_lista(self._negocio.consultar_historial(id_paciente))
