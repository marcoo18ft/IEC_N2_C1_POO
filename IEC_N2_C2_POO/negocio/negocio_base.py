"""
negocio_base.py
Lógica común de la capa de negocio: CRUD con validaciones. Los hijos
sobrescriben _validar_antes_de_guardar() para agregar sus propias reglas
(POLIMORFISMO) y reutilizan el resto (HERENCIA).
"""
from datos.auxiliar import ErrorValidacion


class NegocioBase:

    def __init__(self, repositorio):
        self._repositorio = repositorio

    def _validar_antes_de_guardar(self, modelo):
        """Gancho para reglas de negocio propias de cada entidad."""
        return None

    def _exigir_habilitado(self, repositorio, id_registro, nombre_entidad):
        """Verifica que el registro relacionado exista y esté habilitado."""
        registro = repositorio.obtener_por_id(id_registro)
        if registro is None:
            raise ErrorValidacion(f"No existe {nombre_entidad} con ID {id_registro}.")
        if not registro.habilitado:
            raise ErrorValidacion(f"{nombre_entidad} con ID {id_registro} está deshabilitado.")
        return registro

    def agregar(self, modelo):
        self._validar_antes_de_guardar(modelo)
        nuevo_id = self._repositorio.crear(modelo)
        modelo.id = nuevo_id
        return nuevo_id

    def modificar(self, modelo):
        if modelo.id is None:
            raise ErrorValidacion("Debe indicar el ID del registro a modificar.")
        self.obtener(modelo.id)
        self._validar_antes_de_guardar(modelo)
        self._repositorio.actualizar(modelo)

    def obtener(self, id_registro):
        modelo = self._repositorio.obtener_por_id(id_registro)
        if modelo is None:
            raise ErrorValidacion(f"No existe un registro con ID {id_registro}.")
        return modelo

    def listar(self, solo_habilitados=True):
        return self._repositorio.listar(solo_habilitados)

    def eliminar(self, id_registro):
        self.obtener(id_registro)
        self._repositorio.eliminar(id_registro)
