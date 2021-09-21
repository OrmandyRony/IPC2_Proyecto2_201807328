from elaboracion import Elaboracion

class Producto():

    def __init__(self, nombre):
        self.nombre = nombre
        self.elaboracion = Elaboracion()
        self.siguiente = None
        self.anterior = None