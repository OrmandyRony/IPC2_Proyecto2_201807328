from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.iconbitmap("brazo_robot.ico")
root.title("Digital Intelligence")
root.geometry("800x500")

producto_spin = StringVar()

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

def abre_fichero():
    global ruta_archivo
    fichero = filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=( ("Ficheros de pxla", "*.pxla"), ("Ficheros de Texto", "*.txt"))) # especificar el inicio de la ruta
    ruta_archivo = fichero


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
archivo_carga.add_command(label="Archivo Maquina", command=abre_fichero)
archivo_carga.add_command(label="Archivo Simulación", command=abre_fichero)

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




spin_producto = Spinbox(root, textvariable=producto_spin).place(x=5, y=5)
boton_producto = Button(root, text="Producto",  bg="#009",fg="white").place(x=25, y=30)

r = Text(root, width=95, height=15)
r.place(x=20, y= 100)
r.insert(INSERT, "t(s)\tLinea1\t\tLinea2\t\tLinea3\n")

root.mainloop()