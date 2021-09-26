from salida_listado_productos import Salida_listado_productos

class Salida_simulacion:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.listado_productos = Salida_listado_productos()
        self.siguiente = None
        self.anterior = None