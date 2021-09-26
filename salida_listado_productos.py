from producto import Producto
from salida_producto import Salida_producto

class Salida_listado_productos:
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.tamano = 0

    def ingresar_producto_salida(self, nombre, tiempo_total):
        nuevo_producto = Salida_producto(nombre, tiempo_total)

        if self.inicio is None:
            self.inicio = nuevo_producto
        
        else:
            producto_temporal = self.inicio

            while producto_temporal.siguiente is not None:
                producto_temporal = producto_temporal.siguiente
            
            producto_temporal.siguiente = nuevo_producto

            self.fin = nuevo_producto
            nuevo_producto.anterior = producto_temporal

    def obtener(self, nombre):
        producto_temporal = self.inicio

        while producto_temporal is not None:
            if producto_temporal.nombre == nombre:
                return producto_temporal
            producto_temporal = producto_temporal.siguiente
    
        return None