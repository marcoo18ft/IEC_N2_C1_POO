from datos.modelos.catalogo import Catalogo


class Estado(Catalogo):

    def __init__(self, estado, descripcion="", id_estado=None, habilitado=True):
        super().__init__(estado, descripcion, id_estado, habilitado)

    @property
    def id_estado(self):
        return self._id

    @property
    def estado(self):
        return self.nombre

    def a_diccionario(self):
        return {
            "estado": self.nombre,
            "descripcion": self.descripcion,
            "habilitado": int(self.habilitado),
        }

    def mostrar(self):
        return (f"[{self.id}] {self.nombre} | {self.descripcion} "
                f"| Habilitado: {self._texto_habilitado()}")
