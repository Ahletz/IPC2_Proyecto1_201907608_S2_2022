import xml.etree.ElementTree as ET
from Listas_Infor_pacientes import *
from Listas_info_celulas import *


class Open:

    def Leer(self, direccion):

        info = Lista()

        tree = ET.parse(direccion)

        root = tree.getroot()

        i = 0

        for paciente in root.findall('paciente'):

            i+=1

            datos = paciente.find('datospersonales')
            nombre = datos.find('nombre').text
            edad = datos.find('edad').text
            info.agregar(nombre, edad)
            print(i,nombre,edad)

        print('-------------------------------')

    def Leer_rejillas(self,direccion):

        info_rejilla = Lista_rejilla()

        tree = ET.parse(direccion)

        root = tree.getroot()

        for paciente in root.findall('paciente'):

            dato = paciente.find('datospersonales')
            
            m = int(paciente.find('m').text)

            nombre = dato.find('nombre').text

            if (m%10) == 0 and m < 10000:

                m+=1

                for i in range(m):

                    for j in range(m):

                        info_rejilla.agregar(nombre,'sana',str(i),str(j))

            else: 

                print('La rejilla celular del paciente '+dato.find('nombre').text+' no es una rejilla valida')

            
        info_rejilla.Mostrar()


            

            


            



