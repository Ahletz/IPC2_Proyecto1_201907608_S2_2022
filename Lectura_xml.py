import xml.etree.ElementTree as ET


class Open:

    def Leer(self, direccion):

        

        tree = ET.parse(direccion)

        root = tree.getroot()

        i = 0

        for paciente in root.findall('paciente'):

            i+=1

            datos = paciente.find('datospersonales')
            nombre = datos.find('nombre').text
            edad = datos.find('edad').text
            print(i,nombre,edad)

        print('-------------------------------')



            

            


            



