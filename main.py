from maquina import Maquina
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
                    linea = ""
                    posicion = ""

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
                            comando = ""

                            for coman in comando:
                                if re.search('\d', coman):
                                    linea += coman
                                elif coman == "p":
                                    break
                            
                            for coman in comando:
                                if coman == "C":
                                    bandera = True
                                if bandera:
                                    if re.search('\d', coman):
                                        posicion += coman
                        
                        producto.elaboracion.insertar_comando(comando, int(linea), int(posicion))
                                    
                            
                        

def cargar_archivo_2(ruta, maquina_intelligence):
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
                    maquina_intelligence.lineas_ensamblaje.crear_linea(id_numero, tiempo)

                for cantidad_componentes in linea_produccion.iter('CantidadComponentes'):
                    linea = maquina_intelligence.lineas_ensamblaje.get_linea(id_numero)
                    numero_componentes = int(cantidad_componentes.text)
                    for i in range(0, numero_componentes + 1):
                        linea.lista_componentes.insertar(i)


        
        for listado_productos in maquina.iter('ListadoProductos'):
            for productos in listado_productos.iter('Producto'):
                nombre_producto = " "
                for nombre in productos.iter('nombre'):
                    nombre_producto = str(nombre.text)
        
                    maquina_intelligence.lista_productos.ingresar_producto(nombre_producto)
                for elaboracio in productos.iter('elaboracion'):
                    producto = maquina_intelligence.lista_productos.get_producto(nombre_producto)
                    comandos = elaboracio.text
                    comandos +=  " "
                    comando = ""
                    linea = ""
                    posicion = ""

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
                            bandera = False
                            for coman in comando:
                                if re.search('\d', coman):
                                    linea += coman
                                elif coman == "p":
                                    break
                            
                            for coman in comando:
                                if coman == "C":
                                    bandera = True
                                if bandera:
                                    if re.search('\d', coman):
                                        posicion += coman

                            producto.elaboracion.insertar_comando(comando, int(linea), int(posicion))
                            comando = ""
                            linea = ""
                            posicion = ""

                            
                        
                                    
                           
def cargar_archivo_simular(ruta, lista_simulaciones):
    tree = ET.parse(ruta)
    root = tree.getroot()
    nombre_simulacion = ""
    for simulacion in root:
        
        for nombre in simulacion.iter('Nombre'):
            nombre_simulacion = nombre.text
            lista_simulaciones.crear_simulacion(nombre_simulacion)
        
        for Listado_productos in simulacion.iter('ListadoProductos'):
            simulaciono = lista_simulaciones.get_simulacion(nombre_simulacion)
            for producto in Listado_productos.iter('Producto'):
                simulaciono.listado_productos.ingresar_producto(producto.text)                

def menu():
    print("")
    opcion = ""
    
    maquina_intelligence = Maquina()
    print("------------------------Digital Intelligence-------------")
    while opcion != "7":
        print("""Menú principal
1. Cargar archivo de maquina
2. Cargar archivo de productos a simular
3. Procesar archivo
4. Escribir archivo XML de salida 
5. Escribir archibo HTML de salida
6. Generar gráfica
7. Salida
""")
        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            filename = input("Ingrese el archivo: ")
            file = './' + filename
            #cargar_archivo(file, lineas_ensamblaje, lista_productos)
            cargar_archivo_2(file, maquina_intelligence)
        if opcion == "2":
            filename = input("Ingrese el nombre del archivo a simular: ")
            file = './' + filename

            cargar_archivo_simular(file, maquina_intelligence.lista_simulaciones)

        if opcion == '3':
            maquina_intelligence.procesar_archivo('\niWatch\n')

        if opcion == '4':
            pass
                                                  
if __name__ == '__main__':
    menu()