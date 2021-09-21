from lineas_ensamblaje import Lineas_ensamblaje
from lista_productos import Lista_productos
import xml.etree.ElementTree as ET
import re

def cargar_archivo(ruta, lineas_ensamblaje, lista_productos):
    tree = ET.parse(ruta)
    root = tree.getroot()
    
    for maquina in root:
        for linea_produccion in maquina.iter('CantidadLineasProduccion'):
            print(linea_produccion.text)
        
        for listado_lineas_produccion in maquina.iter('ListadoLineasProduccion'):
            for linea_produccion in listado_lineas_produccion.iter('LineaProduccion'):
                id_numero = 0
                numero_componentes = 0
                tiempo = 0
                for tiempo_ensamblaje in linea_produccion.iter('TiempoEnsamblaje'):
                    tiempo = int(tiempo_ensamblaje.text)

                for numero in linea_produccion.iter('Numero'):
                    id_numero = int(numero.text)
                    lineas_ensamblaje.crear_linea(id_numero, tiempo)

                for cantidad_componentes in linea_produccion.iter('CantidadComponentes'):
                    linea = lineas_ensamblaje.get_linea(id_numero)
                    numero_componentes = int(cantidad_componentes.text)
                    for i in range(1, numero_componentes + 1):
                        linea.lista_componentes.insertar(i)


        
        for listado_productos in maquina.iter('ListadoProductos'):
            for productos in listado_productos.iter('Producto'):
                nombre_producto = " "
                for nombre in productos.iter('nombre'):
                    nombre_producto = str(nombre.text)
        
                    lista_productos.ingresar_producto(nombre_producto)
                for elaboracio in productos.iter('elaboracion'):
                    producto = lista_productos.get_producto(nombre_producto)
                    comandos = elaboracio.text
                    comandos +=  " "
                    comando = ""
                    for i in comandos:
                        if re.search('\d', i):
                            comando += i
                        elif i == "L":
                            comando += i
                        elif i == "C":
                            comando += i
                        elif i == "p":
                            comando += i
                        elif i == " ":
                            producto.elaboracion.insertar_comando(comando)
                            comando = ""
                           
def menu():
    print("")
    opcion = ""
    lineas_ensamblaje = Lineas_ensamblaje()
    lista_productos = Lista_productos()
    print("------------------------Digital Intelligence-------------")
    while opcion != "6":
        print("""Menú principal
1. Cargar archivo
2. Procesar archivo
3. Escribir archivo XML de salida 
4. Escribir archibo HTML de salida
5. Generar gráfica
6. Salida
""")
        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            filename = input("Ingrese el archivo: ")
            file = './' + filename
            cargar_archivo(file, lineas_ensamblaje, lista_productos)

if __name__ == '__main__':
    menu()