class Elaboracion_optima:
    def __init__(self, tiempo, numero_linea, accion) -> None:
        self.tiempo = tiempo
        self.numero_linea = numero_linea
        self.accion = accion
        self.siguiente = None
        self.anterior = None
        
