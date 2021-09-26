from simulacion_salida import Salida_simulacion

class Lista_salida_simulacion:
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.tamano = 0

    def ingresar_simulacion_salida(self, nombre):
        nueva_simulacion = Salida_simulacion(nombre)

        if self.inicio is None:
            self.inicio = nueva_simulacion
        
        else: 
            simulacion_temporal = self.inicio

            while simulacion_temporal.siguiente is not None:
                simulacion_temporal = simulacion_temporal.siguiente
            
            simulacion_temporal.siguiente = nueva_simulacion

            self.fin =nueva_simulacion
            nueva_simulacion.anterior = simulacion_temporal

    def get(self, nombre_simulacion):
        simulacion_temporal = self.inicio

        while simulacion_temporal is not None:
            if simulacion_temporal.nombre == nombre_simulacion:
                return simulacion_temporal
            simulacion_temporal = simulacion_temporal.siguiente
        
        return None