from unicodedata import name
import xml.etree.ElementTree as ET
from Listas_Infor_pacientes import *
from Listas_info_celulas import *

class Open:

    def Leer(self, direccion):

        self.info = Lista() #clase lida

        tree = ET.parse(direccion) #leer elemntTree 

        root = tree.getroot() #obtener xml 

        i = 0

        for paciente in root.findall('paciente'): #ciclo pacientes

            i+=1

            datos = paciente.find('datospersonales') #obtener datos de la etiqueta datos
            nombre = datos.find('nombre').text #obtener el nombre 
            edad = datos.find('edad').text #obtener edad
            self.info.agregar(nombre, edad) # agregar a lista
            
        print('-------------------------------')

    def mostrar(self):

        self.info.Mostrar()

        #-------------------------------------------------------------------------------------------------------------------

    def Leer_rejillas(self,direccion):

        self.info_rejilla = Lista_rejilla()

        tree = ET.parse(direccion)

        root = tree.getroot()

        for paciente in root.findall('paciente'):

            dato = paciente.find('datospersonales')

            rejilla = paciente.find('rejilla')
            
            m = int(paciente.find('m').text)

            self.periodos = m

            nombre = dato.find('nombre').text

            estado = rejilla.find('celda')

            if (m%10) == 0 and m < 10000:

                m+=1

                for i in range(1, m): #ciclo para crear filas

                    for j in range(1, m): #ciclo para crear columnas

                        for x in rejilla.findall('celda'): #ciclo para contagiar celulas

                            estado_fila = x.attrib.get('f') #obtener fila de la celula contagiada

                            estado_columna = x.attrib.get('c') #obtener columna de la celula contagiada
                            
                            if estado_fila == str(i) and estado_columna == str(j): #comprobacion de fila

                                celula = 'contagiada' #contagiar celda
                                break #terminar ciclo para no descontagiar
                                
                            else:
                                celula = 'sana' #celula sana
                                
                                

                        
                        self.info_rejilla.agregar(nombre,celula,str(i),str(j)) #agregar informacion a listas

            else: 

                print('La rejilla celular del paciente '+dato.find('nombre').text+' no es una rejilla valida') #si la rejilla no es m%10 ==0

            
    def mostrar_rejilla(self, nombre):

        #self.info_rejilla.Mostrar(nombre) 

        self.info_rejilla.Periodos(self.periodos,nombre)

        self.info_rejilla.Mostrar_periodos()

    def graficar_rejillas_entrada(self):

        self.mostrar()

        print()
        print('INGRESE EL NOMBRE PARA VER SU REJILLA INICIAL: ')

        nombre = input()

        self.info_rejilla.Graficar(nombre)





        


            

            


            



