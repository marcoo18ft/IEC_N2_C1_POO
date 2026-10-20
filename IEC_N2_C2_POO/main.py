"""
main.py
Punto de entrada del Sistema de Turnos Médicos.
Arma las capas (datos -> negocio -> presentación) y lanza el menú principal.
Ejecutar con:  python main.py
"""
from datos.conexion import Conexion
from datos.repositorio import (CitaRepositorio, EspecialidadRepositorio, EstadoRepositorio,
                               FichaPacienteRepositorio, HistorialClinicaRepositorio,
                               HorarioAtencionRepositorio, PacienteRepositorio,
                               ProfesionalRepositorio)
from negocio import (CitaNegocio, EspecialidadNegocio, EstadoNegocio, FichaPacienteNegocio,
                     HistorialClinicaNegocio, HorarioAtencionNegocio, PacienteNegocio,
                     ProfesionalNegocio)
from presentacion import MenuPrincipal
from presentacion.menu_cita import MenuCita
from presentacion.menu_especialidad import MenuEspecialidad
from presentacion.menu_estado import MenuEstado
from presentacion.menu_ficha_paciente import MenuFichaPaciente
from presentacion.menu_historial_clinica import MenuHistorialClinica
from presentacion.menu_horario_atencion import MenuHorarioAtencion
from presentacion.menu_paciente import MenuPaciente
from presentacion.menu_profesional import MenuProfesional


def main():
    conexion = Conexion()

    # Capa de datos
    especialidad_repo = EspecialidadRepositorio(conexion)
    estado_repo = EstadoRepositorio(conexion)
    profesional_repo = ProfesionalRepositorio(conexion)
    paciente_repo = PacienteRepositorio(conexion)
    horario_repo = HorarioAtencionRepositorio(conexion)
    cita_repo = CitaRepositorio(conexion)
    ficha_repo = FichaPacienteRepositorio(conexion)
    historial_repo = HistorialClinicaRepositorio(conexion)

    # Capa de negocio
    especialidad_negocio = EspecialidadNegocio(especialidad_repo)
    estado_negocio = EstadoNegocio(estado_repo)
    cita_negocio = CitaNegocio(cita_repo, paciente_repo, profesional_repo, estado_repo)
    profesional_negocio = ProfesionalNegocio(profesional_repo, especialidad_repo, horario_repo, cita_negocio)
    paciente_negocio = PacienteNegocio(paciente_repo, historial_repo, cita_negocio)
    horario_negocio = HorarioAtencionNegocio(horario_repo, profesional_repo)
    ficha_negocio = FichaPacienteNegocio(ficha_repo, paciente_repo)
    historial_negocio = HistorialClinicaNegocio(historial_repo, ficha_repo, cita_repo)

    # Capa de presentación
    menus = {
        "1": MenuEspecialidad(especialidad_negocio),
        "2": MenuProfesional(profesional_negocio, especialidad_negocio),
        "3": MenuHorarioAtencion(horario_negocio),
        "4": MenuPaciente(paciente_negocio),
        "5": MenuCita(cita_negocio, estado_negocio),
        "6": MenuEstado(estado_negocio),
        "7": MenuFichaPaciente(ficha_negocio),
        "8": MenuHistorialClinica(historial_negocio),
    }
    MenuPrincipal(menus, conexion).ejecutar()


if __name__ == "__main__":
    main()
