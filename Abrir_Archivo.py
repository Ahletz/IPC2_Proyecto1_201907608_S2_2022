from tkinter import filedialog
from tkinter import *

class Abrir:



    def AbrirArchivo(self):

       archivo = filedialog.askopenfilename(title="Abrir",initialdir="C:/") #filedialog para abrir y buscar un archivo con tkinter

       

       return archivo
       # print(self.Contenido)
