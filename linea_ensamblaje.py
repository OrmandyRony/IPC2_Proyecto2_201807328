from lista_componentes import Lista_componenetes

class Linea_ensamblaje():
    def __init__(self, nombre_Linea, tiempo_ensamblaje):
        self.nombre_linea = nombre_Linea
        self.tiempo_ensamblaje = tiempo_ensamblaje

        self.lista_componentes = Lista_componenetes()
        self.siguiente = None
        self.anterior = None
