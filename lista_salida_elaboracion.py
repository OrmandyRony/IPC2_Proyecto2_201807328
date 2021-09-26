from salida_elaboracion import Elaboracion_optima

class Lista_elaboracion_optima:
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.tamano = 0

    def insertar(self, tiempo, numero_linea, accion):
        nueva_elaboracion = Elaboracion_optima(tiempo, numero_linea, accion)
        self.tamano += 1

        if self.inicio is None:
            self.inicio = nueva_elaboracion
        
        else:
            elaboracion_temporal = self.inicio

            while elaboracion_temporal.siguiente is not None:
                elaboracion_temporal = elaboracion_temporal.siguiente
            
            elaboracion_temporal.siguiente = nueva_elaboracion

            self.fin = nueva_elaboracion
            nueva_elaboracion.anterior = elaboracion_temporal
