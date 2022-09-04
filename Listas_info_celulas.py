class Nodo: #clase nodo

    def __init__ (self,nombre, estado, fila, columna): #creacion de nodo
            self.nombre = nombre
            self.estado = estado
            self.fila = fila
            self.columna = columna
            self.siguiente = None

    #OBTENER DATOS
    def obtener(self): #obtener nombre 

        return self.nombre

    def obtener_estado(self): #obtener estado

        return self.estado
    
    def obtener_fila(self):

        return self.fila
    
    def obtener_columna(self):

        return self.columna

    #OBTENER SIGUIENTES

    def obtener_next(self): #siguiente nombre
        
        return self.siguiente_nombre

    def obtener_next_estado(self): #siguiente edad

        return self.siguiente_estado

    def obtener_next_fila(self):

        return self.siguiente_fila
    
    def obtener_next_columna(self):

        return self.siguiente_columna

    #ASIGNAR

    def asignar(self, nombre, estado, fila, columna): #asignar nombre y edad
            
            self.nombre = nombre

            self.estado = estado

            self.fila = fila

            self.columna = columna

    def asignar_next(self, siguiente_nombre, siguiente_estado, siguiente_fila, Siguiente_columna): #asignar siguiente nombre y edad

            self.siguiente_nombre = siguiente_nombre
            self.siguiente_estado = siguiente_estado
            self.siguiente_fila = siguiente_fila
            self.siguiente_columna = Siguiente_columna

class Lista_rejilla: #clase listas

    def __init__(self):
        self.head = None #creacopm de cabezera de lista

    def estado(self):

        return self.head == None #estado de la lista 

    def agregar(self, nombre, estado, fila, columna): #agregar contenido a la lista
        asig = Nodo(nombre, estado, fila, columna)
        asig.asignar_next(self.head,self.head, self.head, self.head)
        self.head = asig

    def tamano(self): #tamaño de la lista
        actual = self.head
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.obtener_next()

        return contador

    def Mostrar(self,): #mostrar contenido de la lista
        actual = self.head
        while actual != None:

            print('['+actual.obtener_fila()+'x'+actual.obtener_columna()+', '+actual.obtener_estado()+']', end='')

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