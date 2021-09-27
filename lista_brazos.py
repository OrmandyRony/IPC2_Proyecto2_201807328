from brazo import Brazo
import gc

class Lista_brazos:
    def __init__(self) -> None:
        self.principio = None
        self.final = None
        self.tamano = 0
    
    def crear_brazo(self, numero_linea):

        self.tamano += 1
        nuevo_brazo = Brazo(numero_linea)

        if self.principio is None:
            self.principio = nuevo_brazo
            self.final = nuevo_brazo
        else:
            brazo_temporal = self.principio

            while brazo_temporal.siguiente is not None:
                brazo_temporal = brazo_temporal.siguiente

            brazo_temporal.siguiente = nuevo_brazo
            nuevo_brazo.anterior = brazo_temporal

            self.final = nuevo_brazo

    def obtener_brazo(self, numero_linea):
        principio = self.principio

        while principio is not None:
            if principio.numero_linea == numero_linea:
                return principio
            principio = principio.siguiente

        return None 

    def brazo_existe(self, numero_linea):
        principio = self.principio

        while principio is not None:
            if principio.numero_linea == numero_linea:
                return False
            principio = principio.siguiente

        return True

    def producto_armado(self):
        cantidad_brazos_procesado = 0
        principio = self.principio

        while principio is not None:
            if principio.cola_movimientos.principio is None:
                cantidad_brazos_procesado += 1
            principio = principio.siguiente

        if cantidad_brazos_procesado == self.tamano:
            return False
        else:
            return True

    def despausar(self):
        principio = self.principio

        while principio is not None:
            if not principio.pausa:
                principio.pausa = True
            principio = principio.siguiente

    def vaciar(self):
        self.principio = None
        self.final = None
        self.tamano = 0
        gc.collect()
        
        
