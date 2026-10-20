# Sistema de Turnos Médicos — Evaluación 2 POO (INACAP Temuco)

Aplicación de consola en Python con arquitectura de 3 capas, POO y persistencia en MySQL.
El diagrama de clases UML está en la raíz: `diagrama_de_clases_principal_programacion.drawio`.

## Estructura

```
IEC_N2_C2_POO/
├── datos/
│   ├── modelos/        Clases del diagrama UML (una por archivo)
│   ├── repositorio/    Persistencia: CRUD con consultas SQL
│   ├── sql/            crear_tablas.sql y datos_iniciales.sql
│   ├── __init__.py
│   ├── auxiliar.py     Validaciones, conversiones de fecha/hora y excepciones
│   ├── conexion.py     Conexión a MySQL (mysql-connector-python + .env)
│   └── models.py       Importación centralizada de los modelos
├── negocio/            Reglas de negocio (validaciones, estados de cita, etc.)
├── presentacion/       Menús de consola
├── .env                Parámetros de conexión (NO se sube a GitHub)
├── .gitignore
├── main.py             Inicia la aplicación (menú con CRUD)
├── README.md
└── requirements.txt
```

## Principios de POO aplicados

| Principio | Dónde |
|---|---|
| Abstracción | `ModeloBase`, `Catalogo`, `Persona`, `RepositorioBase`, `MenuCrud` (clases abstractas con `ABC`) |
| Encapsulamiento | Atributos privados (`__rut`, `__email`...) con `@property` que validan el dato; `_id` protegido para las clases hijas |
| Herencia | `Persona` → `Profesional`, `Paciente`; `Catalogo` → `Especialidad`, `Estado`; todos → `ModeloBase`; cada repositorio, negocio y menú hereda de su base |
| Polimorfismo | Sobrescritura: `mostrar()`, `a_diccionario()`, `_a_modelo()`, `_validar_antes_de_guardar()` y `pedir_modelo()` se redefinen en cada hija. Sobrecarga (Python, con argumentos por defecto): `CitaNegocio.reservar()` y `CitaNegocio.listar_citas()` |

## Instalación y uso

1. Tener MySQL instalado y en ejecución.
2. Instalar dependencias: `pip install -r requirements.txt`
3. Copiar `.env.example` a `.env` y escribir usuario y clave de MySQL.
4. Ejecutar: `python main.py`
5. En el menú principal elegir **9. Inicializar base de datos** (crea la BD `turnos_medicos`, las tablas y los estados/especialidades base).
6. Usar los menús 1 a 8 para el CRUD de cada entidad.

## Reglas de negocio principales

- RUT chileno validado con módulo 11; correo y teléfono con formato válido.
- Un profesional no puede tener dos jornadas que se solapen el mismo día.
- Citas: `Reservada → Confirmada` y `Reservada/Confirmada → Cancelada`.
- Un paciente tiene una sola ficha (relación 1:1) y el historial se valida contra su ficha y su cita.
- Eliminar: baja lógica (`habilitado = 0`) en tablas con ese campo; borrado real en `cita`, `ficha_paciente` e `historial_clinica`.

## Métodos del diagrama UML y dónde están

Los modelos (`datos/modelos`) guardan atributos y validaciones; los métodos de comportamiento del diagrama están en la capa de negocio:

| Clase | Métodos del diagrama | Implementación |
|---|---|---|
| Especialidad | agregar, modificar | `NegocioBase.agregar / modificar` |
| Profesional | consultarAgenda, agendarHora | `ProfesionalNegocio.consultar_agenda / agendar_hora` |
| HorarioAtencion | registrarJornada, modificarJornada | `HorarioAtencionNegocio.registrar_jornada / modificar_jornada` |
| Paciente | solicitarCita, consultarHistorial | `PacienteNegocio.solicitar_cita / consultar_historial` |
| Cita | reservar, confirmar, cancelar | `CitaNegocio.reservar / confirmar / cancelar` |
| Estado | obtenerEstado, cambiarEstado | `EstadoNegocio.obtener_estado / cambiar_estado` |
| Ficha_paciente | consultar_Ficha, modificar_Ficha, anular_Ficha | `FichaPacienteNegocio.consultar_ficha / modificar_ficha / anular_ficha` |
| Historial_clinica | registrar, consultar, modificar | `HistorialClinicaNegocio.registrar_historial / consultar_historial / modificar_historial` |
