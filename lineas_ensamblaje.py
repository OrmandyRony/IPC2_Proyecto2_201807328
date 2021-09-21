from linea_ensamblaje import Linea_ensamblaje

class Lineas_ensamblaje():
    def __init__(self) -> None:
        self.inicio = None
        self.fin = None
        self.size = 0

    def crear_linea(self, nombre_linea, tiempo_ensamblaje):
        nueva_linea = Linea_ensamblaje(nombre_linea, tiempo_ensamblaje)
        self.size += 1

        if self.inicio is None:
            self.inicio = nueva_linea
        
        else:
            linea_temporal = self.inicio
            while linea_temporal.siguiente  is not None:
                linea_temporal = linea_temporal.siguiente
            linea_temporal.siguiente = nueva_linea

            self.fin = nueva_linea
            nueva_linea.anterior = linea_temporal
    
    def get_linea(self, nombre_linea):
        linea_temporal = self.inicio
        while linea_temporal is not None:
            if linea_temporal.nombre_linea == nombre_linea:
                return linea_temporal
            linea_temporal = linea_temporal.siguiente
        return None
