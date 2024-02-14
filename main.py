from tkinter import *
from tkinter import Tk

root = Tk()


class App():
    def __init__(self) -> None:
        self.root = root
        self.window()
        self.frames()
        self.widgets_Lframe()
        root.mainloop()
    
    def window(self):
        self.root.title('FilOr')
        self.root.geometry('800x500')
        self.root.configure(background='#131f38')
        self.root.maxsize(950,650)
        self.root.minsize(650,350)
    
    def frames(self):
        self.Lframe = Frame(self.root, bd=4, bg='#dfe3ee',
                            highlightbackground='#759de6', highlightthickness=1.8)
        self.Lframe.place(relx=0.01,rely=0.01,relwidth=0.4,relheight=0.98)
        
        self.Rframe = Frame(self.root, bd=4, bg='#dfe3ee',
                            highlightbackground='#759de6', highlightthickness=1.8)
        self.Rframe.place(relx=0.414,rely=0.01,relwidth=0.576,relheight=0.98)
    
    def widgets_Lframe(self): ...





App()
