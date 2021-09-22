class Componente():
    def __init__(self, componente) -> None:
        self.posicion = componente
        self.siguiente = None
        self.anterior = None
        self.tiempo = 1