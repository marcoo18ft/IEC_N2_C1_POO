from negocio.negocio_base import NegocioBase


class EstadoNegocio(NegocioBase):

    def obtener_estado(self, id_estado):
        return self.obtener(id_estado)

    def cambiar_estado(self, id_estado, habilitado):
        """Habilita o deshabilita un estado."""
        self.obtener(id_estado)
        self._repositorio.cambiar_habilitado(id_estado, habilitado)
