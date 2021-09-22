from simulacion_producto import Producto

class Listado_productos_simular():
     
    def __init__(self):
        self.final = None
        self.principio = None
    
    def ingresar_producto(self, nombre):
        nuevo_producto = Producto(nombre)

        if self.principio is None:
            self.principio = nuevo_producto
           
        else:
            producto_temporal = self.principio

            while producto_temporal.siguiente is not None:
                producto_temporal = producto_temporal.siguiente
            producto_temporal.siguiente = nuevo_producto

            self.final = nuevo_producto
            nuevo_producto.anterior = producto_temporal
            

    def get_producto(self, nombre_producto):
        producto_temporal = self.principio
        while producto_temporal is not None:
            if producto_temporal.nombre == nombre_producto:
                return producto_temporal
            producto_temporal = producto_temporal.siguiente
        return None