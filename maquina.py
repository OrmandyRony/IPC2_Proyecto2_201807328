from lineas_ensamblaje import Lineas_ensamblaje
from lista_productos import Lista_productos
from lista_simulaciones import Lista_simulaciones
from lista_brazos import Lista_brazos
import re


class Maquina():

    def __init__(self) -> None:
        self.lineas_ensamblaje = Lineas_ensamblaje()
        self.lista_productos = Lista_productos()
        self.lista_simulaciones = Lista_simulaciones()
        self.lista_brazos = Lista_brazos()

    def procesar_archivo(self, nombre_producto):
        # 1. Se le da un producto a ensamblar
        producto = self.lista_productos.get_producto(nombre_producto)
        print("Entro")
        """2. Se le da un conjunto de intrucciones
                a. Indicando linea de produccion
                b. Componente que deber ser ensamblado"""

        elaboracion = producto.elaboracion
        comando = elaboracion.inicio
        linea_ensamblanje = self.lineas_ensamblaje.get_linea(comando.linea)
        

        tiempo = 1
        cantidad_lineas = self.lineas_ensamblaje.size
        cantidad_comandos = elaboracion.tamano

        # Crea los brazos roboticos a utilizar
        while comando is not None:
            if self.lista_brazos.brazo_existe(comando.linea):
                self.lista_brazos.crear_brazo(comando.linea)
            comando = comando.siguiente

        # Ingresar movimientos
        comando = elaboracion.inicio
        while comando is not None:
            brazo = self.lista_brazos.obtener_brazo(comando.linea)
            brazo.cola_movimientos.ingresar_movimiento(comando.posicion)
            comando = comando.siguiente

        comando = elaboracion.inicio
        
        brazo = self.lista_brazos.principio
        numero_linea = brazo.numero_linea
        listo = self.lista_brazos.producto_armado()
        tiempo_dezplazo = 1
        brazo_temporal = self.lista_brazos.principio
       
        prioridad = elaboracion.inicio

        while listo:
            bandera = True
            linea_ensamblanje = self.lineas_ensamblaje.get_linea(numero_linea)
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
                print("Tiempo\tLínea", numero_linea)
                print(tiempo, "s\tComponente",componente.posicion )

            #Brazo hacia atras
            elif componente.posicion > posicion and brazo.pausa:
                comando = comando.siguiente
                componente = componente.anterior
                linea_ensamblanje.mover_posicion(componente.posicion)
                print("Tiempo\tLínea", numero_linea)
                print(tiempo, "s\tComponente",componente.posicion )

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
                    brazo_temporal = self.lista_brazos.principio
                brazo = self.lista_brazos.principio
                
                
                print("Tiempo\tLínea", numero_linea)
                print(tiempo, "s\tEnsamblar Componente",componente.posicion )
                tiempo += tiempo_dezplazo 
                numero_linea = brazo.numero_linea
                comando = elaboracion.inicio
                bandera = False
                

            if prioridad is not None:
                if bandera:
                    if not (componente.posicion == prioridad.posicion and prioridad.linea == numero_linea):
                        # Simular una lista circular
                        
                        if brazo.siguiente is not None:
                            brazo = brazo.siguiente
                        else:
                            brazo = self.lista_brazos.principio
                            comando = elaboracion.inicio
                            tiempo += tiempo_dezplazo 
                        numero_linea = brazo.numero_linea
                
                
               
           
            listo = self.lista_brazos.producto_armado()
        
        print("Producto armado")


            



            




