from tkinter import *
from tkinter import ttk
from vistas.cuota import FrameCuota

class Aplicacion(ttk.Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        self.mi_ventana = ventana
        self.mi_frame = LabelFrame(self.mi_ventana, text = "MENU", width="400", height="400", bg = "lightblue", bd = 5)
        self.mi_frame.config(fon = ("arial black", 10))
        self.mi_frame.pack()
   
        
        def carfarFrameCouta():
            self.cuota = FrameCuota(self)
        #Boton
        self.btn_cuota = Button(self.mi_frame, text = "CALCULADORA DE CUOTAS", command = carfarFrameCouta)
        self.btn_cuota.config(width = 30, height = 5, fon=("arial black", 10))
        self.btn_cuota.grid(row = 1, column = 1, padx = 10, pady = 10)

        self.btn_cuota2 = Button(self.mi_frame, text = "asdasdasdas")
        self.btn_cuota2.config(width = 30, height = 5, fon=("arial black", 10))
        self.btn_cuota2.grid(row = 1, column = 2, padx = 10, pady = 10)


        self.pack()