from cola_movimientos import Cola_movimientos

class Brazo:
    def __init__(self, numero_linea) -> None:
        self.numero_linea = numero_linea
        self.cola_movimientos = Cola_movimientos()
        self.siguiente =  None
        self.anterior = None
        self.pausa = True

    