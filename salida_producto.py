from lista_salida_elaboracion import Lista_elaboracion_optima

class Salida_producto:

    def __init__(self, nombre, tiempo_total):
        self.nombre = nombre
        self.tiempo_total = tiempo_total
        self.lista_elaboracion_optima = Lista_elaboracion_optima()
        self.siguiente = None
        self.anterior = None