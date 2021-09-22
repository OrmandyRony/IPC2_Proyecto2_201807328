from simulacion import simulacion

class Lista_simulaciones():
    def __init__(self) -> None:
        self.inicio = None
        self.fin = None
        self.size = 0

    def crear_simulacion(self, nombre_simulacion):
        nueva_simulacion = simulacion(nombre_simulacion)
        self.size += 1

        if self.inicio is None:
            self.inicio = nueva_simulacion
        
        else:
            simulacion_temporal = self.inicio
            while simulacion_temporal.siguiente is not None:
                simulacion_temporal = simulacion_temporal.siguiente
            simulacion_temporal.siguiente = nueva_simulacion

            self.fin = nueva_simulacion
            nueva_simulacion.anterior = simulacion_temporal 

    def get_simulacion(self, nombre):
        simulacion_temporal = self.inicio

        while simulacion_temporal is not None:
            if simulacion_temporal.nombre == nombre:
                return simulacion_temporal
            simulacion_temporal = simulacion_temporal.siguiente

        return None
