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

                    print('|| pacientes cargados en el sistema: ')
                    self.lectura.mostrar()

                    print()
                    print('|| ¿Desea ver la rejilla inicial de un paciente?')
                    print('|| 1. SI  2. NO')

                    opcion = input()

                    if opcion == '1':

                        print('|| Ingrese el nombre de un paciente: ')

                        self.lectura.mostrar()

                        print()

                        nombre = input()

                        self.lectura.mostrar_rejilla(nombre)




            elif opcion == 3:
                        
                        self.Menu1()

            elif opcion == 4:
                        
                        self.lectura.Xml()

            elif opcion == 5:

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

                self.lectura.graficar_rejillas_entrada()
            
            elif opcion == '2':

                print('INGRESE EL PERIODO QUE DESEA GRAFICAR')

                periodo = input()

                self.lectura.graficar_periodo(periodo)
        

            elif opcion == '3':

                ciclo = False

            else: 

                print('NO INGRESO UNA OPCION VALIDA')


        


            
        