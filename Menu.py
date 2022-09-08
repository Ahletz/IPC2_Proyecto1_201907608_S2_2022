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
            print('|| 4. Generar salida.')
            print('|| 5. Salir.')

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

                    pass

            elif opcion == 3:
                        
                        self.Menu1()

            elif opcion == 4:

                        exit = False #cerrar el ciclo del menu

           # except:

                #print('USTED NO SELECCIONO UNA OPCION VALIDA.')
            
    def Menu1(self):

        ciclo = True 

        while ciclo == True:

            print('|| seleccione una opcion:            ||')
            print('|| 1. Graficar primera rejilla.      ||')
            print('|| 2. Graficar un periodo.           ||')
            print('|| 3. Salir.                         ||')

            opcion = input()

            if opcion == '1':

                pass
            
            elif opcion == '2':

                pass
        

            elif opcion == '3':

                ciclo = False

            else: 

                print('NO INGRESO UNA OPCION VALIDA')


        


            
        