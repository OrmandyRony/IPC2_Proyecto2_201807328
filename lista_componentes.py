from componente import Componente

class Lista_componenetes():
    def __init__(self) -> None:
        self.inicio = None
        self.fin = None
        self.tamano = 0

    def insertar(self, componente):
        nuevo_componente = Componente(componente)
        self.tamano += 1

        if self.inicio is None:
            self.inicio = nuevo_componente
        else: 
            temporal = self.inicio

            while temporal.siguiente is not None:
                temporal = temporal.siguiente
            temporal.siguiente = nuevo_componente

            self.fin = nuevo_componente
            nuevo_componente.anterior = temporal
    
    def get_componente(self, componente):
        componente_bus = self.inicio
        while componente_bus is not None:
            if componente == componente_bus.componente:
                return componente
            componente_bus = componente_bus.siguiente
        return None
        