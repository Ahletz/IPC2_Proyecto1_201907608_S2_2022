from opcode import opname
from Abrir_Archivo import *
from Lectura_xml import *


class Menu:

    def __init__(self):

        print('||---------------BIENVENIDO!---------------||')

    def Opciones(self):

        abrir = Abrir() #importar clase para abrir un archivo 

        exit = True #salida del programa

        self.lectura = Open()

        while exit == True:

            print('|| SELECCIONE UNA DE LAS SIGUIENTES OPCIONES: ||')

            print('|| 1. Cargar Archivo.')
            print('|| 2. Analizar paciente.')
            print('|| 3. Generar Graficas.')
            print('|| 4. Salir.')

            #try: #capturador try exeption de errores al momento de ingresar una opcion no valida
                    
            opcion = int(input()) #ingreso de la opcion a elegir 

            if opcion == 1: #cargar archivo

                print('abriendo...')

                direccion = abrir.AbrirArchivo() #direccion del documento cargado 

                print(direccion) #direccion del archivo

                self.lectura.Leer(direccion) #Lectura del xml

                print('--------------------------------------------------------------------')

                self.lectura.Leer_rejillas(direccion)

            elif opcion == 2:

                    self.lectura.mostrar()    
                    print('INGRESE EL NOMBRE DEL PACIENTE PARA GENERAR SU DIAGNOSTICO: ')

                    nombre = input()

                    self.lectura.mostrar_rejilla(nombre)

                    print('¿DESEA REVISAR UN PERIODO EN ESPECIFICO?')
                    print('1.Si 2.No')

                    des = int(input())
                    ciclo = True

                    while ciclo == True:
                    
                        try:

                            if des == 1:
                                
                                self.lectura.mostrar_rejilla(nombre)
                                
                                ciclo = False

                            elif des == 2:

                                ciclo = False

                        except:

                            print('NO INGRESO UNA OPCION VALIDA')

            elif opcion == 3:
                        
                        self.lectura.graficar_rejillas_entrada()

            elif opcion == 4:

                        exit = False #cerrar el ciclo del menu

           # except:

                #print('USTED NO SELECCIONO UNA OPCION VALIDA.')

    def Graficar(self):

        pass

    def Generar_salida(self):

        pass
            

            
        