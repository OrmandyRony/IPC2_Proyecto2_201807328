class Comando:
    def __init__(self, comando, linea, posicion):
        self.comando = comando
        self.linea = linea
        self.posicion = posicion
        self.siguiente = None
        self.anterior = None