class Nodo: #clase nodo

    def __init__ (self,nombre, edad): #creacion de nodo
            self.nombre = nombre
            self.edad = edad
            self.siguiente = None

    def obtener(self): #obtener nombre 

        return self.nombre

    def obtener_edad(self): #obtener edad

        return self.edad

    def obtener_next(self): #siguiente nombre
        
        return self.siguiente_nombre

    def obtener_next_edad(self): #siguiente edad

        return self.siguiente_edad

    def asignar(self, nombre, edad): #asignar nombre y edad
            
            self.nombre = nombre

            self.edad = edad

    def asignar_next(self, siguiente_nombre, siguiente_edad): #asignar siguiente nombre y edad

            self.siguiente_nombre = siguiente_nombre
            self.siguiente_edad = siguiente_edad

class Lista: #clase listas

    def __init__(self):
        self.head = None #creacopm de cabezera de lista

    def estado(self):

        return self.head == None #estado de la lista 

    def agregar(self, nombre, edad): #agregar contenido a la lista
        asig = Nodo(nombre, edad)
        asig.asignar_next(self.head,self.head)
        self.head = asig

    def tamano(self): #tamaño de la lista
        actual = self.head
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.obtener_next()

        return contador

    def Mostrar(self): #mostrar contenido de la lista
        actual = self.head
        while actual != None:
            print('Nombre: '+actual.obtener() + ' ,edad:'+actual.obtener_edad())
            actual = actual.obtener_next()       

    def Eliminar(self,dato): #eliminar contenido de la lista
        actual = self.head
        anterior = None
        find = False
        while not find:
            if actual.obtener() == dato:
                find = True
            else:
                anterior = actual
                actual = actual.obtener_next()

        if anterior == None:
            self.head = actual.obtener_next()
        else:
            anterior.asignar_next(actual.obtener_next())