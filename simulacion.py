from simulacion_listado_productos import Listado_productos_simular

class simulacion():

    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.listado_productos = Listado_productos_simular()
        self.procesada = False
        self.siguiente = None
        self.anterior = None
