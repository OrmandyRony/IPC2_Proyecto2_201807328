from producto import Producto

class Lista_productos():
     
    def __init__(self):
        self.final = None
        self.principio = None
    
    def ingresar_producto(self, nombre):
        nuevo_producto = Producto(nombre)

        if self.principio is None:
            self.principio = nuevo_producto
            self.final = nuevo_producto
        else:
            nuevo_producto.siguiente = self.final
            self.final = nuevo_producto
            nodo = self.principio
            while nodo.anterior is not None:
                nodo = nodo.anterior
            
            nodo.anterior = nuevo_producto

    def get_producto(self, nombre_producto):
        producto_temporal = self.principio
        while producto_temporal is not None:
            if producto_temporal.nombre == nombre_producto:
                return producto_temporal
            producto_temporal = producto_temporal.siguiente
        return None