from tkinter import *
from tkinter import Tk

root = Tk()

# criar um função para fazer a troca de cores de acordo com o tema.

# Classe Mãe para a criação de janelas
class App():
    def __init__(self) -> None:
        self.root = root
        self.window_base()
        root.mainloop()
    
    # Função de criação de janela base
    def window_base(self) -> None:
        self.root.title('FilOr')
        self.root.geometry('300x500')
        self.root.configure(background='#131f38')
        self.root.resizable(False,False)
        
    

App()
