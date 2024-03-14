from tkinter import *
from tkinter import Tk

from Funcs.file_organizer import fileOrganizer
from Funcs.config import configs
from Funcs.directory_creator import structures

root = Tk()

# criar um função para fazer a troca de cores de acordo com o tema.
class Themes:
  ...
  
# Classe Mãe.
class App:
  def __init__(self) -> None:
    self.root = root
    self.window_base()
    self.buttons()
    root.mainloop()

  # Função de criação de janela base
  def window_base(self) -> None:
    self.root.title('FilOr')
    self.root.geometry('300x500')
    self.root.configure(background='#131f38')
    self.root.resizable(False,False)

  def buttons(self):
    # Botão para a função de organizar arquivos.
    self.organize = Button(self.root, text='Organizar', font=('26'),
                            command=fileOrganizer)
    self.organize.place(x=50,y=75, width=200, height=50)

    # Botão para a função de criar estrutura de diretórios.
    self.organize = Button(self.root, text='Gerar estruturas', font=('26'),
                            command=structures)
    self.organize.place(x=50,y=225, width=200, height=50)

    # Botão para a janela de configurações.
    self.organize = Button(self.root, text='Configurações', font=('26'),
                            command=configs)
    self.organize.place(x=50,y=375, width=200, height=50)

App()