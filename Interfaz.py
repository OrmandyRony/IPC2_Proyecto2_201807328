from os import system, startfile
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import xml.etree.ElementTree as ET
import re


# Modulos creados
from maquina import Maquina

maquina_intelligence = Maquina()
lista_simulaciones = maquina_intelligence.lista_simulaciones
lista_productos = []
lista_productos_grafica = []
lista_lineas_ensamblaje = []

root = Tk()
root.iconbitmap("brazo_robot.ico")
root.title("Digital Intelligence")
root.geometry("550x710")

producto_spin = StringVar()
grafo_spin = StringVar()

# Funciones de la interfaz
def info_adicional():
    messagebox.showinfo("Digital Intelligence", "Simulador de lineas de ensamblaje 2021")

def aviso_licencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")


def salir_aplicacion():
    #valor = messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")
    valor = messagebox.askokcancel("Salir", "¿Deseas salir de la aplicación?")

    if valor == True:
        root.destroy()

def cerrar_documento():
    valor = messagebox.askretrycancel("Reintentar", "Noes posible cerrar. Documento bloqueado")
    # funciona con true y false
    if valor == False:
        root.destroy()

def abre_fichero_maquina():
    global ruta_archivo_maquina
    ruta_archivo_maquina = filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=( ("Ficheros de pxla", "*.xml"), ("Ficheros de Texto", "*.txt"))) # especificar el inicio de la ruta
    cargar_archivo_maquina(ruta_archivo_maquina)

def abre_fichero_simulacion():
    ruta_archivo_simulacion  = filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=( ("Ficheros de pxla", "*.xml"), ("Ficheros de Texto", "*.txt"))) # especificar el inicio de la ruta
    cargar_archivo_simulacion(ruta_archivo_simulacion)

def limpiar_text():    
    r = Text(root, width=65, height=25)
    #scrollbar = Scrollbar(root, command=r.yview)
    #scrollbar.pack(side=RIGHT, fill=Y)
    r.place(x=20, y= 100)
    r.insert(INSERT, "t(s)\tLinea\tMovimientos\n")
    imprimir.config(text="0")
    lista_lineas_ensamblaje.clear()

def actualizar():
    spin_producto = Spinbox(root, values=(lista_productos), textvariable=producto_spin).place(x=5, y=5)
    

def actualizar_lista_grafo():
    spin_grafo = Spinbox(root, values=lista_productos_grafica, textvariable=grafo_spin).place(x=250, y=5)

def tiempo_total(tiempo):
    imprimir.config(text=tiempo)

def actualizar_tablero():
    r = Text(root, width=65, height=25)
    r.insert(INSERT, "t(s)\tLinea\t\tMovimientos\n")
    for elemento in lista_lineas_ensamblaje:
        r.insert(INSERT,elemento)
        r.place(x=20, y=100)
 
      

def procesar_archivo(nombre_producto):
        # 1. Se le da un producto a ensamblar
        producto = maquina_intelligence.lista_productos.get_producto(nombre_producto)
        maquina_intelligence.lista_salida_simulacion.ingresar_simulacion_salida(producto.nombre)
        
        salida_simulacion = maquina_intelligence.lista_salida_simulacion.get(producto.nombre)
        salida_simulacion.listado_productos.ingresar_producto_salida(producto.nombre, 0)
        salida_producto = salida_simulacion.listado_productos.obtener(producto.nombre)
       
        # print("Entro")
        """2. Se le da un conjunto de intrucciones
                a. Indicando linea de produccion
                b. Componente que deber ser ensamblado"""

        elaboracion = producto.elaboracion
        comando = elaboracion.inicio
        linea_ensamblanje = maquina_intelligence.lineas_ensamblaje.get_linea(comando.linea)
        

        tiempo = 1
        cantidad_lineas = maquina_intelligence.lineas_ensamblaje.size
        cantidad_comandos = elaboracion.tamano

        # Crea los brazos roboticos a utilizar
        while comando is not None:
            if maquina_intelligence.lista_brazos.brazo_existe(comando.linea):
                maquina_intelligence.lista_brazos.crear_brazo(comando.linea)
            comando = comando.siguiente

        # Ingresar movimientos
        comando = elaboracion.inicio
        while comando is not None:
            brazo = maquina_intelligence.lista_brazos.obtener_brazo(comando.linea)
            brazo.cola_movimientos.ingresar_movimiento(comando.posicion)
            comando = comando.siguiente

        comando = elaboracion.inicio
        
        brazo = maquina_intelligence.lista_brazos.principio
        numero_linea = brazo.numero_linea
        listo = maquina_intelligence.lista_brazos.producto_armado()
        tiempo_dezplazo = 1
        brazo_temporal = maquina_intelligence.lista_brazos.principio
       
        prioridad = elaboracion.inicio

        while listo:
            bandera = True
            linea_ensamblanje = maquina_intelligence.lineas_ensamblaje.get_linea(numero_linea)
            componente = linea_ensamblanje.lista_componentes.get_componente(linea_ensamblanje.posicion_dinamica)
            if brazo.cola_movimientos.principio is not None:
                posicion = brazo.cola_movimientos.principio.posicion
            else:
                pass
                #while brazo.cola_movimientos.principio is None:
                #    brazo = brazo.siguiente
                #posicion = brazo.cola_movimientos.principio.posicion
            

            #Brazo hacia adelante
            if componente.posicion < posicion and brazo.pausa:
                comando = comando.siguiente
                componente = componente.siguiente
                linea_ensamblanje.mover_posicion(componente.posicion)
                texto = str(tiempo) + "s\tLínea " + str(numero_linea) + "\t\tComponente "+ str(componente.posicion) +"\n"
                salida_producto.lista_elaboracion_optima.insertar(tiempo, numero_linea, "Movimiento")
                lista_lineas_ensamblaje.append(texto)
                #print("Tiempo\tLínea", numero_linea)
                #print(tiempo, "s\tComponente",componente.posicion )

            #Brazo hacia atras
            elif componente.posicion > posicion and brazo.pausa:
                comando = comando.siguiente
                componente = componente.anterior
                linea_ensamblanje.mover_posicion(componente.posicion)
                texto = str(tiempo) + "s\tLínea " + str(numero_linea) + "\t\tComponente "+ str(componente.posicion) +"\n"
                salida_producto.lista_elaboracion_optima.insertar(tiempo, numero_linea, "Movimiento")
                lista_lineas_ensamblaje.append(texto)
                #print("Tiempo\tLínea", numero_linea)
                #print(tiempo, "s\tComponente",componente.posicion )

            #Brazo ensambla componente
            elif (componente.posicion == posicion and prioridad.linea == numero_linea):
                tiempo += linea_ensamblanje.tiempo_ensamblaje
                linea_ensamblanje.mover_posicion(componente.posicion)
                brazo.cola_movimientos.movimiento_realizado()

                if brazo.cola_movimientos.principio is None:
                    brazo.pausa = False
               
                prioridad = prioridad.siguiente
                if brazo_temporal.siguiente is not None:
                    brazo_temporal = brazo_temporal.siguiente
                else:
                    brazo_temporal = maquina_intelligence.lista_brazos.principio
                brazo = maquina_intelligence.lista_brazos.principio
                texto = str(tiempo) + "s\tLínea " + str(numero_linea) + "\t\tEnsamblar Componente "+ str(componente.posicion) +"\n"
                salida_producto.lista_elaboracion_optima.insertar(tiempo, numero_linea,"Ensamblar")
                lista_lineas_ensamblaje.append(texto)
                #print("Tiempo\tLínea", numero_linea)
                #print(tiempo, "s\tEnsamblar Componente",componente.posicion )
                tiempo += tiempo_dezplazo 
                numero_linea = brazo.numero_linea
                comando = elaboracion.inicio
                bandera = False
            else:
                texto = str(tiempo) + "s\tLínea " + str(numero_linea) + "\t\tNo hacer nada\n"
                lista_lineas_ensamblaje.append(texto)
                salida_producto.lista_elaboracion_optima.insertar(tiempo, numero_linea, "No hacer nada")

            if prioridad is not None:
                
                if bandera:
                    if not (componente.posicion == prioridad.posicion and prioridad.linea == numero_linea):
                        # Simular una lista circular
                        
                        if brazo.siguiente is not None:
                            brazo = brazo.siguiente
                        else:
                            brazo = maquina_intelligence.lista_brazos.principio
                            comando = elaboracion.inicio
                            tiempo += tiempo_dezplazo 
                        numero_linea = brazo.numero_linea
            actualizar_tablero()  
            listo = maquina_intelligence.lista_brazos.producto_armado()
        
        
        salida_producto.tiempo_total = tiempo - 1
        tiempo_total(tiempo -1)
        reporte_html = generar_reporte(salida_producto)
        escribir_archivo("reporte_simulacion"+salida_producto.nombre, reporte_html)
        
        escribir_archivo_salida(salida_producto)
        maquina_intelligence.lista_brazos.vaciar()
        
        #print("Producto armado")

def escribir_archivo(ruta, contenido):
    ruta += ".html"

    characters = "\""

    for x in range(len(characters)):
        ruta = ruta.replace(characters[x],"")

    try:
        with open(ruta, 'x') as file:
            file.write(contenido)
            print('Se escribio en el archivo correctamente')
    except:
        print('No se pudo abrir el fichero porque existe: ' + ruta)
    #print('----------------------------------')

def escribir_archivo_salida(salida_producto):
    simulacion_escribir = ET.Element("SalidaSimulacion")
    
    ET.SubElement(simulacion_escribir, "Nombre").text = str(salida_producto.nombre)
    
    listado_productos = ET.SubElement(simulacion_escribir, "ListadoProductos")
    producto = ET.SubElement(listado_productos, "Producto")
    ET.SubElement(producto, "Nombre").text = str(salida_producto.nombre)
    ET.SubElement(producto, "TiempoTotal").text = str(salida_producto.tiempo_total)

    elaboracion_optima = ET.SubElement(producto, "ElaboracionOptima")

    elaboracion_temporal = salida_producto.lista_elaboracion_optima.inicio
    
    while elaboracion_temporal is not None:
        tiempo = ET.SubElement(elaboracion_optima, "Tiempo", NoSegundo = str(elaboracion_temporal.tiempo))
        ET.SubElement(tiempo, "LineaEnsamblaje", NoLinea = str(elaboracion_temporal.numero_linea)).text = elaboracion_temporal.accion
        elaboracion_temporal = elaboracion_temporal.siguiente



    archivo1 = ET.ElementTree(simulacion_escribir)
    archivo1.write("simulacion_maquina"+salida_producto.nombre+".xml")


def tabla_datos_html(salida_producto):
    # Genera una tabla en html
    tabla = """<table>
		 	<tr>
	 		<td>Tiempo </td>
	 		<td>Linea</td>
            <td>Movimiento </td> 
		 	</tr>"""
    
    elaboracion_temporal = salida_producto.lista_elaboracion_optima.inicio
    
    while elaboracion_temporal is not None:
        tabla += """<tr>
	 		<td>""" + str(elaboracion_temporal.tiempo) +"""</td>
	 		<td>""" + str(elaboracion_temporal.numero_linea) + """</td>
            <td>""" + str(elaboracion_temporal.accion) + """</td>
		 	</tr>"""
        elaboracion_temporal = elaboracion_temporal.siguiente

    tabla += "</table>"

    return tabla

def generar_reporte(salida_producto):
    
    head = """<head>
	<title>Reporte de Simulacion</title>
	<link rel=\"stylesheet\" type=\"text/css\" href=\"css/reporte.css\">
       </head>"""

    body = """"<body>
	<div id = principal>
		<header>
			<div id=\"titulo_principal\">
				<h1>"""+salida_producto.nombre +"""</h1>
			</div>
		</header>
		<hr>

		<section>
			<div class=\"grafica\">
				<div class=\"titulo\">
					<h1>Tabla de simulacion </h1>
				</div>\n""" + tabla_datos_html(salida_producto) +""" 
			</div>
		</section>

	</div>

"</body>"""

    html = "<!DOCTYPE html>\n<html>" + head + body + "</html>"
    return html


# Funciones de la aplicacion -----------------------------------------------
def cargar_archivo_maquina(ruta):
    tree = ET.parse(ruta)
    root = tree.getroot()
    
    for maquina in root:
        for linea_produccion in maquina.iter('CantidadLineasProduccion'):
            linea_produccioneas = (linea_produccion.text)
        
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
                nombre_producto = ""
                for nombre in productos.iter('nombre'):

                    nombre_temporal = str(nombre.text)
                    for i in nombre_temporal:
                        if re.search('\w', i):
                            nombre_producto += i

                    lista_productos_grafica.append(nombre_producto)
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

    actualizar_lista_grafo()

def cargar_archivo_simulacion(ruta):
    tree = ET.parse(ruta)
    root = tree.getroot()
    nombre_simulacion = ""
    nombre_producto = ""
    for simulacion in root:
        
        for nombre in simulacion.iter('Nombre'):
            nombre_simulacion = str(nombre.text)
            lista_simulaciones.crear_simulacion(nombre_simulacion)
        
        for Listado_productos in simulacion.iter('ListadoProductos'):
            simulaciono = lista_simulaciones.get_simulacion(nombre_simulacion)
            for producto in Listado_productos.iter('Producto'):
                nombre_producto = ""
                nombre_temporal = str(producto.text)
                for i in nombre_temporal:
                    if re.search('\w', i):
                        nombre_producto  += i
                simulaciono.listado_productos.ingresar_producto(nombre_producto)                
                lista_productos.append(nombre_producto)
    
    actualizar()

def procesar_producto():
    procesar_archivo(producto_spin.get())

def procesar_todos_producto():
    for producto in lista_productos:
        lista_lineas_ensamblaje.append(producto)
        procesar_archivo(producto)
        

def generar_grafica():
    generar_img_grafo(grafo_spin.get())

def generar_img_grafo(nombre_producto):

    producto = maquina_intelligence.lista_productos.get_producto(nombre_producto)
    graphviz = """digraph L{
    node[shape = box fillcolor = "yellow" style = filled]
    

    subgraph cluster_p{
        label = \""""+str(producto.nombre) +"""\"
        
        /*Aqui creamos las cabeceras de las filas */
        """ 
  
    

    columnas = ""
    producto_temporal = producto.elaboracion.inicio
    i = 1
    while producto_temporal is not None:
        columnas += "Columna"+ str(i) +"[label = \""+ str(producto_temporal.comando) + """\", group = """+str(i+1) +", fillcolor = yellow];\n"""
        producto_temporal = producto_temporal.siguiente
        i += 1

    producto_temporal = producto.elaboracion.inicio
    i = 1
    while producto_temporal is not None:
        if producto_temporal.siguiente is None:
            break
        columnas += "Columna"+ str(i) +"->Columna"+str(i+1)+";\n"
        producto_temporal = producto_temporal.siguiente
        i += 1
    
        
    graphviz += columnas
    graphviz += """}
    }""" 

    miArchivo = open('graphviz.dot', 'w')
    miArchivo.write(graphviz)
    miArchivo.close()
    system('dot -Tpng graphviz.dot -o graphviz'+producto.nombre+'.png')
    system('cd ./graphviz'+producto.nombre+'.png')
    startfile('graphviz'+producto.nombre+'.png')
    
#------------------------------------------------------------------------------ 



# Barra Menu
barra_menu = Menu(root)
root.config(menu=barra_menu)

# Creacion de la barra menu
archivo_menu = Menu(barra_menu, tearoff=0)

# Subelemento
archivo_menu.add_command(label="Cerrar", command=cerrar_documento)
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=salir_aplicacion)

# Creacion de la barra de carga de archivo
archivo_carga = Menu(barra_menu, tearoff = 0)

#Subelemento
archivo_carga.add_command(label="Archivo Maquina", command=abre_fichero_maquina)
archivo_carga.add_command(label="Archivo Simulación", command=abre_fichero_simulacion)

archivo_ayudas = Menu(barra_menu, tearoff=0)
#subelemnto
archivo_ayudas.add_command(label="Licencia", command=aviso_licencia)
archivo_ayudas.add_command(label="Acerca de...", command=info_adicional)

archivo_reportes = Menu(barra_menu, tearoff=0)
archivo_reportes.add_command(label="Ver Reportes")

barra_menu.add_cascade(label="Archivo", menu=archivo_menu) # le indicamos el texto del primer menu
barra_menu.add_cascade(label= "Cargar", menu=archivo_carga)
barra_menu.add_cascade(label="Reportes", menu=archivo_reportes)
barra_menu.add_cascade(label="Ayuda", menu=archivo_ayudas)




spin_producto = Spinbox(root, values=lista_productos, textvariable=producto_spin).place(x=5, y=5)
boton_producto = Button(root, text="Procesar Producto", command=procesar_producto,  bg="#009",fg="white").place(x=25, y=30)

boton_productos = Button(root, text="Procesar todos", command=procesar_todos_producto,  bg="#0F0",fg="white").place(x=150, y=5)

spin_grafo = Spinbox(root, values=lista_productos_grafica, textvariable=grafo_spin).place(x=250, y=5)
boton_grafo = Button(root, text="Graficar cola", command=generar_grafica,  bg="#009",fg="white").place(x=260, y=30)

boton_limpiar = Button(root, text="Limpiar", command=limpiar_text,  bg="#F00",fg="white").place(x=460, y=30)

etiqueta_tiempo = Label(root, text="Tiempo Total:", bg="#FF0").place(x=460, y=520)
imprimir = Label(root)
imprimir.place(x=460, y=560)

r = Text(root, width=65, height=25)
#scrollbar = Scrollbar(root, command=r.yview)
#scrollbar.pack(side=RIGHT, fill=Y)
r.place(x=20, y= 100)
r.insert(INSERT, "t(s)\tLinea\tMovimientos\n")

root.mainloop()