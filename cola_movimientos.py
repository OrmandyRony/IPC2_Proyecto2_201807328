from movimiento import Movimiento

class Cola_movimientos:
    def __init__(self) -> None:
        self.final = None
        self.principio = None
    
    def ingresar_movimiento(self, posicion):
        nuevo_movimiento = Movimiento(posicion)

        if self.principio is None:
            self.principio = nuevo_movimiento
            self.final = nuevo_movimiento
        
        else:
            nuevo_movimiento.siguiente = self.final
            self.final = nuevo_movimiento
            movimiento_temporal = self.principio

            while movimiento_temporal.anterior is not None:
                movimiento_temporal = movimiento_temporal.anterior
            
            movimiento_temporal.anterior = nuevo_movimiento

    def movimiento_realizado(self):
        self.principio = self.principio.anterior

    def mostrar_movimientos(self):
        principio = self.principio
        while principio is not None:
            print(principio.posicion)
            principio = principio.anterior
