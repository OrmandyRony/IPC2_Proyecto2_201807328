from lineas_ensamblaje import Lineas_ensamblaje
from lista_productos import Lista_productos
from lista_simulaciones import Lista_simulaciones
import re


class Maquina():

    def __init__(self) -> None:
        self.lineas_ensamblaje = Lineas_ensamblaje()
        self.lista_productos = Lista_productos()
        self.lista_simulaciones = Lista_simulaciones()

    def procesar_archivo(self, nombre_producto):
        # 1. Se le da un producto a ensamblar
        producto = self.lista_productos.get_producto(nombre_producto)

        """2. Se le da un conjunto de intrucciones
                a. Indicando linea de produccion
                b. Componente que deber ser ensamblado"""

        elaboracion = producto.elaboracion
        comando = elaboracion.inicio
        

        tiempo = 0
        while comando is not None:
            linea = ""
            componen = ""
            bandera = False
            for coman in comando.comando:
                if re.search('\d', coman):
                    linea += coman
                elif coman == "p":
                    break
            
            print(linea)

            for coman in comando.comando:

                if coman == "C":
                    bandera = True
                if bandera:
                    if re.search('\d', coman):
                        componen += coman
                    elif coman == "":
                        componen 

            print(componen)

            linea_ensamblanje = self.lineas_ensamblaje.get_linea(int(linea))
            component = linea_ensamblanje.lista_componentes.inicio
            componen = int(componen)

            # Robot hacia adelante
            if component.posicion < componen:
                while component is not None:
                    tiempo += component.tiempo
                    if component.posicion == componen:
                        break
                component = component.siguiente

            elif component.posicion > component:
                while component is not None:
                    tiempo += component.tiempo
                    if component.posicion == componen:
                        break
                component = component.anterior

            elif component.posicion == componen:
                tiempo += linea_ensamblanje.tiempo_ensamblaje
            
            

            comando = comando.siguiente

            



            




