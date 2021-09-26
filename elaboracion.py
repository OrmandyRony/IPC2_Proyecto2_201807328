from comando import Comando

class Elaboracion():
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.tamano = 0

    def insertar_comando(self, comando, linea, posicion):
        nuevo_comando = Comando(comando, linea, posicion)
        self.tamano += 1

        if self.inicio is None:
            self.inicio = nuevo_comando

        else: 
            comando_temporal = self.inicio

            while comando_temporal.siguiente is not None:
                comando_temporal = comando_temporal.siguiente
            comando_temporal.siguiente = nuevo_comando

            self.fin = nuevo_comando
            nuevo_comando.anterior = comando_temporal
