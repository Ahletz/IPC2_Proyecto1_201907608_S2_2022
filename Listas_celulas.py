from graphviz import Digraph

class Nodo: #clase nodo

    def __init__ (self,nombre, estado, fila, columna, periodo): #creacion de nodo
            self.nombre = nombre
            self.estado = estado
            self.fila = fila
            self.columna = columna
            self.periodo = periodo
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

    def obtener_periodo(self):

        return self.periodo

    #OBTENER SIGUIENTES

    def obtener_next(self): #siguiente nombre
        
        return self.siguiente_nombre

    def obtener_next_estado(self): #siguiente edad

        return self.siguiente_estado

    def obtener_next_fila(self):

        return self.siguiente_fila
    
    def obtener_next_columna(self):

        return self.siguiente_columna

    def obtener_next_periodo(self):

        return self.siguiente_periodo

    #ASIGNAR

    def asignar(self, nombre, estado, fila, columna, periodo): #asignar nombre y edad
            
            self.nombre = nombre

            self.estado = estado

            self.fila = fila

            self.columna = columna

            self.periodo = periodo

    def asignar_next(self, siguiente_nombre, siguiente_estado, siguiente_fila, siguiente_columna, siguiente_periodo): #asignar siguiente nombre y edad

            self.siguiente_nombre = siguiente_nombre
            self.siguiente_estado = siguiente_estado
            self.siguiente_fila = siguiente_fila
            self.siguiente_columna = siguiente_columna
            self.siguiente_periodo = siguiente_periodo


class Lista_rejilla_celular: #clase listas

    def __init__(self):
        self.head = None #creacopm de cabezera de lista

    def estado(self):

        return self.head == None #estado de la lista 

    def agregar(self, nombre, estado, fila, columna, periodo): #agregar contenido a la lista
        asig = Nodo(nombre, estado, fila, columna, periodo)
        asig.asignar_next(self.head,self.head, self.head, self.head, self.head)
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
        
        print('INGRESE EL PERIODO QUE DESEA REVISAR: ') #periodo que desea visualizar
        periodo = input()

        while actual != None:

            if  periodo == actual.obtener_periodo():

                print('['+actual.obtener_fila()+'x'+actual.obtener_columna()+', '+actual.obtener_estado()+']', end='')

            actual = actual.obtener_next()   
        print()    

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

            

    
    def Infectar(self, periodos): #crear periodos

        actual = self.head

        periodos = int(periodos)+1 #cantidad de periodos

        for i in range(2,periodos): # ciclo para crear periodos

            while actual != None:

                infectados = 0

                if actual.obtener_fila() == str(periodos) and actual.obtener_columna() == str(periodos): #revision esquina inferior

                    #esquina inferior derecha datos

                     Arriba_fila = str(int(actual.obtener_fila())-1)
                     Arriba_columna = actual.obtener_columna() 

                     izquierda_fila = actual.obtener_fila()
                     izquierda_columna = str(int(actual.obtener_columna())-1)

                     ezquina_ar_fila = str(int(actual.obtener_fila())-1)
                     ezquina_ar_columna = str(int(actual.obtener_columna())-1)

                     actual1 = self.head

                     while actual1 != None:

                        if actual1.obtener_fila() == Arriba_fila and actual1.obtener_columna() == Arriba_columna and actual1.obtener_estado() == 'contagiada':

                            infectados+=1

                        if actual1.obtener_fila() == izquierda_fila and actual1.obtener_columna() == izquierda_columna and actual1.obtener_estado() == 'contagiada':

                            infectados+=1

                        if actual1.obtener_fila() == ezquina_ar_fila and actual1.obtener_columna() == ezquina_ar_columna and actual1.obtener_estado() == 'contagiada':

                            infectados+=1

                        actual1 = actual1.obtener_next()
                
                elif actual.obtener_fila() == str(periodos) and actual.obtener_columna() == '1': #revision esquina inferior izquierda

                    #esquina inferior izquierda datos

                    Arriba_fila = str(int(actual.obtener_fila())-1)
                    Arriba_columna = '1'

                    derecha_fila = actual.obtener_fila()
                    derecha_columna = str(int(actual.obtener_columna())+1)

                    ezquina_d_fila = str(int(actual.obtener_fila())-1)
                    ezquina_d_columna = str(int(actual.obtener_columna())+1)

                    actual2 = self.head

                    while actual2 != None:

                        if actual2.obtener_fila() == Arriba_fila and actual2.obtener_columna() == Arriba_columna and actual2.obtener_estado() == 'contagiada':

                            infectados+=1

                        if actual2.obtener_fila() == derecha_fila and actual2.obtener_columna() == derecha_columna and actual2.obtener_estado() == 'contagiada':

                            infectados+=1

                        if actual2.obtener_fila() == ezquina_d_fila and actual2.obtener_columna() == ezquina_d_columna and actual2.obtener_estado() == 'contagiada':

                            infectados+=1

                        actual2 = actual2.obtener_next()

                
                elif actual.obtener_fila() == '1' and actual.obtener_columna() == str(periodos): #estado esquina superior derecha

                    #esquina superior derechar datos

                     Abajo_fila = str(int(actual.obtener_fila())+1)
                     Abajo_columna = actual.obtener_columna() 

                     izquierda_fila = actual.obtener_fila()
                     izquierda_columna = str(int(actual.obtener_columna())-1)

                     ezquina_fila = str(int(actual.obtener_fila())+1)
                     ezquina_columna = str(int(actual.obtener_columna())-1)

                     actual3 = self.head

                     while actual3 != None:

                        if actual3.obtener_fila() == Abajo_fila and actual3.obtener_columna() == Abajo_columna and actual3.obtener_estado() == 'contagiada':

                            infectados+=1

                        if actual3.obtener_fila() == izquierda_fila and actual3.obtener_columna() == izquierda_columna and actual3.obtener_estado() == 'contagiada':

                            infectados+=1

                        if actual3.obtener_fila() == ezquina_fila and actual3.obtener_columna() == ezquina_columna and actual3.obtener_estado() == 'contagiada':

                            infectados+=1

                        actual3 = actual3.obtener_next()


                elif actual.obtener_fila() == '1' and actual.obtener_columna() == '1': #estado esquina superior izquierda

                    #esquina superior izquierda datos

                    Abajo_fila = str(int(actual.obtener_fila())+1)
                    Abajo_columna = actual.obtener_columna() 

                    derecha_fila = actual.obtener_fila()
                    derecha_columna = str(int(actual.obtener_columna())+1)

                    ezquina_fila = str(int(actual.obtener_fila())+1)
                    ezquina_columna = str(int(actual.obtener_columna())+1)

                    actual4 = self.head

                    while actual4 != None:

                        if actual4.obtener_fila() == Abajo_fila and actual4.obtener_columna() == Abajo_columna and actual4.obtener_estado() == 'contagiada':

                            infectados+=1

                        if actual4.obtener_fila() == derecha_fila and actual4.obtener_columna() == derecha_columna and actual4.obtener_estado() == 'contagiada':

                            infectados+=1

                        if actual4.obtener_fila() == ezquina_fila and actual4.obtener_columna() == ezquina_columna and actual4.obtener_estado() == 'contagiada':

                            infectados+=1

                        actual4 = actual4.obtener_next()

                elif actual.obtener_fila() == '1' and actual.obtener_columna() != '1'and actual.obtener_columna() != '5': #estado primera fila

                    #datos primera linea

                    Abajo_fila = str(int(actual.obtener_fila())+1)
                    Abajo_columna = actual.obtener_columna()

                    izquierda_fila = actual.obtener_fila()
                    izquierda_columna = str(int(actual.obtener_columna())-1)

                    derecha_fila = actual.obtener_fila()
                    derecha_columna = str(int(actual.obtener_columna())+1)

                    esquinaI_fila = str(int(actual.obtener_fila())+1)
                    esquinaI_columna = str(int(actual.obtener_columna())-1)

                    esquinaD_fila = str(int(actual.obtener_fila())+1)
                    esquinaD_columna = str(int(actual.obtener_columna())+1)

                    actual5 = self.head

                    while actual5 != None:

                        if actual5.obtener_fila() == Abajo_fila and actual5.obtener_columna() == Abajo_columna and actual5.obtener_estado() == 'contagiada':

                            infectados+=1

                        if actual5.obtener_fila() == derecha_fila and actual5.obtener_columna() == derecha_columna and actual5.obtener_estado() == 'contagiada':

                            infectados+=1

                        if actual5.obtener_fila() == izquierda_fila and actual5.obtener_columna() == izquierda_columna and actual5.obtener_estado() == 'contagiada':

                            infectados+=1

                        if actual5.obtener_fila() == esquinaI_fila and actual5.obtener_columna() == esquinaI_columna and actual5.obtener_estado() == 'contagiada':

                            infectados+=1

                        if actual5.obtener_fila() == esquinaD_fila and actual5.obtener_columna() == esquinaD_columna and actual5.obtener_estado() == 'contagiada':

                            infectados+=1

                        actual5 = actual5.obtener_next()

                
                elif actual.obtener_fila() == '1' and actual.obtener_columna() != '1'and actual.obtener_columna() != '5': #estado ultima fila fila

                    #datos ultima linea

                    Arriba_fila = str(int(actual.obtener_fila())+1)
                    Arriba_columna = actual.obtener_columna()

                    izquierda_fila = actual.obtener_fila()
                    izquierda_columna = str(int(actual.obtener_columna())-1)

                    derecha_fila = actual.obtener_fila()
                    derecha_columna = str(int(actual.obtener_columna())+1)

                    esquinaI_fila = str(int(actual.obtener_fila())-1)
                    esquinaI_columna = str(int(actual.obtener_columna())-1)

                    esquinaD_fila = str(int(actual.obtener_fila())-1)
                    esquinaD_columna = str(int(actual.obtener_columna())+1)

                    actual6 = self.head

                    while actual6 != None:

                        if actual6.obtener_fila() == Abajo_fila and actual6.obtener_columna() == Abajo_columna and actual6.obtener_estado() == 'contagiada':

                            infectados+=1

                        if actual6.obtener_fila() == derecha_fila and actual6.obtener_columna() == derecha_columna and actual6.obtener_estado() == 'contagiada':

                            infectados+=1

                        if actual6.obtener_fila() == izquierda_fila and actual6.obtener_columna() == izquierda_columna and actual6.obtener_estado() == 'contagiada':

                            infectados+=1

                        if actual6.obtener_fila() == esquinaI_fila and actual6.obtener_columna() == esquinaI_columna and actual6.obtener_estado() == 'contagiada':

                            infectados+=1

                        if actual6.obtener_fila() == esquinaD_fila and actual6.obtener_columna() == esquinaD_columna and actual6.obtener_estado() == 'contagiada':

                            infectados+=1

                        actual6 = actual6.obtener_next()

                elif actual.obtener_columna() == '1' and actual.obtener_fila() != '1'and actual.obtener_fila() != '5': #estado primera columna

                     #datos primera columna

                    Arriba_fila = str(int(actual.obtener_fila())-1)
                    Arriba_columna = actual.obtener_columna()

                    Abajo_fila = str(int(actual.obtener_fila())+1)
                    Abajo_columna = actual.obtener_columna()

                    derecha_fila = actual.obtener_fila()
                    derecha_columna = str(int(actual.obtener_columna())+1)

                    esquinaA_fila = str(int(actual.obtener_fila())-1)
                    esquinaA_columna = str(int(actual.obtener_columna())+1)

                    esquinaB_fila = str(int(actual.obtener_fila())+1)
                    esquinaB_columna = str(int(actual.obtener_columna())+1)

                    actual7 = self.head

                    while actual7 != None:

                        if actual7.obtener_fila() == Abajo_fila and actual7.obtener_columna() == Abajo_columna and actual7.obtener_estado() == 'contagiada':

                            infectados+=1

                        if actual7.obtener_fila() == derecha_fila and actual7.obtener_columna() == derecha_columna and actual7.obtener_estado() == 'contagiada':

                            infectados+=1

                        if actual7.obtener_fila() == Arriba_fila and actual7.obtener_columna() == Arriba_columna and actual7.obtener_estado() == 'contagiada':

                            infectados+=1

                        if actual7.obtener_fila() == esquinaA_fila and actual7.obtener_columna() == esquinaA_columna and actual7.obtener_estado() == 'contagiada':

                            infectados+=1

                        if actual7.obtener_fila() == esquinaB_fila and actual7.obtener_columna() == esquinaB_columna and actual7.obtener_estado() == 'contagiada':

                            infectados+=1

                        actual7 = actual7.obtener_next()


                elif actual.obtener_columna() == '5' and actual.obtener_fila() != '1'and actual.obtener_fila() != '5': #estado ultima columna

                     #datos ultima columna

                    Arriba_fila = str(int(actual.obtener_fila())-1)
                    Arriba_columna = actual.obtener_columna()

                    Abajo_fila = str(int(actual.obtener_fila())+1)
                    Abajo_columna = actual.obtener_columna()

                    izquierda_fila = actual.obtener_fila()
                    izquierda_columna = str(int(actual.obtener_columna())-1)

                    esquinaA_fila = str(int(actual.obtener_fila())-1)
                    esquinaA_columna = str(int(actual.obtener_columna())-1)

                    esquinaB_fila = str(int(actual.obtener_fila())+1)
                    esquinaB_columna = str(int(actual.obtener_columna())-1)

                    actual8 = self.head

                    while actual8 != None:

                        if actual8.obtener_fila() == Abajo_fila and actual8.obtener_columna() == Abajo_columna and actual8.obtener_estado() == 'contagiada':

                            infectados+=1

                        if actual8.obtener_fila() == izquierda_fila and actual8.obtener_columna() == izquierda_columna and actual8.obtener_estado() == 'contagiada':

                            infectados+=1

                        if actual8.obtener_fila() == Arriba_fila and actual8.obtener_columna() == Arriba_columna and actual8.obtener_estado() == 'contagiada':

                            infectados+=1

                        if actual8.obtener_fila() == esquinaA_fila and actual8.obtener_columna() == esquinaA_columna and actual8.obtener_estado() == 'contagiada':

                            infectados+=1

                        if actual8.obtener_fila() == esquinaB_fila and actual8.obtener_columna() == esquinaB_columna and actual8.obtener_estado() == 'contagiada':

                            infectados+=1

                        actual8 = actual8.obtener_next()    


                else:
                    
                    Arriba_fila = str(int(actual.obtener_fila())-1)
                    Arriba_columna = actual.obtener_columna()

                    Abajo_fila = str(int(actual.obtener_fila())+1)
                    Abajo_columna = actual.obtener_columna()

                    izquierda_fila = actual.obtener_fila()
                    izquierda_columna = str(int(actual.obtener_columna())-1)

                    derecha_fila = actual.obtener_fila()
                    derecha_columna = str(int(actual.obtener_columna())-1)

                    esquinaAI_fila = str(int(actual.obtener_fila())-1)
                    esquinaAI_columna = str(int(actual.obtener_columna())-1)

                    esquinaBI_fila = str(int(actual.obtener_fila())+1)
                    esquinaBI_columna = str(int(actual.obtener_columna())-1)

                    esquinaAD_fila = str(int(actual.obtener_fila())-1)
                    esquinaAD_columna = str(int(actual.obtener_columna())-1)

                    esquinaBD_fila = str(int(actual.obtener_fila())+1)
                    esquinaBD_columna = str(int(actual.obtener_columna())-1)

                    actual9 = self.head

                    while actual9 != None:

                        if actual9.obtener_fila() == Abajo_fila and actual9.obtener_columna() == Abajo_columna and actual9.obtener_estado() == 'contagiada':

                            infectados+=1
                        
                        if actual9.obtener_fila() == Arriba_fila and actual9.obtener_columna() == Arriba_columna and actual9.obtener_estado() == 'contagiada':

                            infectados+=1
                        
                        if actual9.obtener_fila() == izquierda_fila and actual9.obtener_columna() == izquierda_columna and actual9.obtener_estado() == 'contagiada':

                            infectados+=1

                        if actual9.obtener_fila() == derecha_fila and actual9.obtener_columna() == derecha_columna and actual9.obtener_estado() == 'contagiada':

                            infectados+=1

                        if actual9.obtener_fila() == esquinaAI_fila and actual9.obtener_columna() == esquinaAI_columna and actual9.obtener_estado() == 'contagiada':

                            infectados+=1

                        if actual9.obtener_fila() == esquinaBI_fila and actual9.obtener_columna() == esquinaBI_columna and actual9.obtener_estado() == 'contagiada':

                            infectados+=1
                        
                        if actual9.obtener_fila() == esquinaAD_fila and actual9.obtener_columna() == esquinaAD_columna and actual9.obtener_estado() == 'contagiada':

                            infectados+=1

                        if actual9.obtener_fila() == esquinaBD_fila and actual9.obtener_columna() == esquinaBD_columna and actual9.obtener_estado() == 'contagiada':

                            infectados+=1

                        

                        actual9 = actual9.obtener_next() 

                
                if infectados >= 3: #estado y agregacion a celulas repeticion #tal

                    self.agregar(actual.obtener(),'contagiada',actual.obtener_fila(),actual.obtener_columna(),str(i))

                    

                else:

                    self.agregar(actual.obtener(),actual.obtener_estado(),actual.obtener_fila(),actual.obtener_columna(),str(i))

                
                actual = actual.obtener_next()

    
    def Graficar_rejilla(self, periodo):

        dot = Digraph('Rejilla', filename='Archivo_graficas.dot',engine='dot', format='svg')
        dot.attr(rankdir='LR')
        dot.node_attr.update(shape='box')
        dot.node_attr['style'] = 'filled'

        actual = self.head

        periodo = periodo

        while actual != None:

            if periodo == actual.obtener():

                estado = actual.obtener_periodo()

                if actual.obtener_estado == 'contagiada':

                    dot.node(estado, fillcolor = 'green')

                else:

                    dot.node(estado)


            actual = actual.obtener_next()   

        dot.view()






