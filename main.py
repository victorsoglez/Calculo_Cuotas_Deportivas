from tkinter import *
from tkinter import ttk
from vistas.menu import Aplicacion

if __name__ == "__main__":
    ventana = Tk()
    ventana.geometry("700x300")
    app = Aplicacion(ventana)

    ventana.mainloop()