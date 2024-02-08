"""
Inicio da criação da tela de Loading.
"""

from tkinter import *
from tkinter import ttk
from tkinter import font

root = Tk()

class App():
    def __init__(self):
        self.root = root
        self.Loanding_window()
        root.mainloop()
        
        # self.lista_arquivos = len(lista_arquivos)
        
        
    def Loanding_window(self):
        self.root.title("FilOr")
        self.root.geometry('400x150')
        self.root.resizable(False,False)
        
        fnt = font.Font(size=16)
        # self.texto = str(texto)
        self.label = Label(root, text='Organizando arquivos...',font=fnt)
        self.label1 = Label(root, text='|_______________________|',font=fnt) # Barra de loading
        self.label.place(x=50,y=40)
        self.label1.place(x=50,y=65)
        
    


App()