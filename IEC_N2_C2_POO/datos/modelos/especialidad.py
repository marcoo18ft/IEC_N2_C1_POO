from datos.modelos.catalogo import Catalogo


class Especialidad(Catalogo):

    def __init__(self, especialidad, descripcion="", id_especialidad=None, habilitado=True):
        super().__init__(especialidad, descripcion, id_especialidad, habilitado)

    @property
    def id_especialidad(self):
        return self._id

    @property
    def especialidad(self):
        return self.nombre

    def a_diccionario(self):
        return {
            "especialidad": self.nombre,
            "descripcion": self.descripcion,
            "habilitado": int(self.habilitado),
        }

    def mostrar(self):
        return (f"[{self.id}] {self.nombre} | {self.descripcion} "
                f"| Habilitada: {self._texto_habilitado()}")
