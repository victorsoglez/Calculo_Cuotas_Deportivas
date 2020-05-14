from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class FrameCuota(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #Metodo para calcular porcentaje de victorias/derrotas
        #Y para calcular las cuotas de ambos
        def calcular():

            if (len(self.entry_cantidad.get()) <= 0 or len(self.entry_local.get()) <= 0 or len(self.entry_visitante.get()) <= 0):
                messagebox.showwarning("ATENCION", "FAVOR DE NO DEJAR CAMPOS VACIOS.")
                self.cuotaF.destroy()

            else:

                #Obtenemos los valores de cada ENTRY
                cantidad_muestra = int(self.entry_cantidad.get())
                win_local = int(self.entry_local.get())
                win_visita = int(self.entry_visitante.get())
                #Calculamos el porcentaje de victoria
                porcientoWinLocal = int((win_local / cantidad_muestra) * 100)
                porcientoWinVisita = int((win_visita / cantidad_muestra) * 100)
                #Pasamos el resultado a los respectivos ENTRY´s
                self.resultado_local['text'] = StringVar(self.resultados_frame, value = porcientoWinLocal)
                self.resultado_visitante['text'] = StringVar(self.resultados_frame, value = porcientoWinVisita)
                #Calculamos las respectivas cuotas
                cuotaWinLocal = 100 / porcientoWinLocal
                cuotaWinVisita = 100 / porcientoWinVisita
                #Pasamos las cuotas a cada ENTRY
                self.cuota_local['text'] = StringVar(self.resultados_frame, value = "{:.3f}".format(cuotaWinLocal))
                self.cuota_visita['text'] = StringVar(self.resultados_frame, value = "{:.3f}".format(cuotaWinVisita))



        #ventana cuotas
        self.cuotaF = Toplevel()
        self.cuotaF.title("CUOTAS")
        self.cuotaF.geometry("650x400")
        #Frame labelframe
        self.cuota_frame = LabelFrame(self.cuotaF, text = "CALCULADORA DE COUTAS", fon = ("arial black", 10))
        self.cuota_frame.config(bg = "lightblue", bd = 5, )
        self.cuota_frame.pack()
        #label muestra de partidos
        self.label_cantidad = Label(self.cuota_frame, text = "MUESTRA DE PARTIDOS(CANTIDAD):", fon = ("arial black", 10))
        self.label_cantidad.grid(row = 0, column = 0, padx = 0, pady = 10)
        #entry cantidad de la muestra
        self.entry_cantidad = Entry(self.cuota_frame, justify = CENTER)
        self.entry_cantidad.grid(row = 0, column = 1, padx = 0, pady = 10)

        self.label_local = Label(self.cuota_frame, text = "VICTORIAS LOCAL(CANTIDAD):", fon = ("arial black", 10))
        self.label_local.grid(row = 1, column = 0, padx = 10, pady = 10)

        self.entry_local = Entry(self.cuota_frame, justify = CENTER)
        self.entry_local.grid(row = 2, column = 0, padx = 10, pady = 10)

        self.label_visitante = Label(self.cuota_frame, text = "VICTORIAS VISITANTE(CANTIDAD):", fon = ("arial black", 10))
        self.label_visitante.grid(row = 1, column = 1, padx = 10, pady = 10)

        self.entry_visitante = Entry(self.cuota_frame, justify = CENTER)
        self.entry_visitante.grid(row = 2, column = 1, padx = 10, pady = 10)

        self.btn_calcular = Button(self.cuotaF, text = "CALCULAR", fon = ("arial black", 10), bg = "DodgerBlue2", command = calcular)
        self.btn_calcular.pack()
        self.btn_calcular.config(width = 25)
        
        #Labelframe resultados
        self.resultados_frame = LabelFrame(self.cuotaF, text = "RESULTADOS", fon = ("arial black", 10))
        self.resultados_frame.config(bg = "lightblue", bd = 5, )
        self.resultados_frame.pack()

        self.label_resultado_local = Label(self.resultados_frame, text = "PORCENTAJE DE VICTORIAS LOCAL:", fon = ("arial black", 10))
        self.label_resultado_local.grid(row = 4, column = 0, padx = 10, pady = 10)

        self.resultado_local = Entry(self.resultados_frame)
        self.resultado_local.config(state = "readonly", justify = CENTER)
        self.resultado_local.grid(row = 4, column = 1, padx = 10, pady = 10)

        self.label_resultado_visita = Label(self.resultados_frame, text = "PORCENTAJE DE VICTORIAS VISITANTE:", fon = ("arial black", 10))
        self.label_resultado_visita.grid(row = 5, column = 0, padx = 10, pady = 10)

        self.resultado_visitante = Entry(self.resultados_frame)
        self.resultado_visitante.config(state = "readonly", justify = CENTER)
        self.resultado_visitante.grid(row = 5, column = 1, padx = 10, pady = 10)

        self.label_cuotas = Label(self.resultados_frame, text = "CUOTAS:", fon = ("arial black", 10))
        self.label_cuotas.grid(row = 3, column =2, padx = 10, pady = 10)

        self.cuota_local = Entry(self.resultados_frame)
        self.cuota_local.config(state = "readonly", justify = CENTER)
        self.cuota_local.grid(row = 4, column = 2, padx = 10, pady = 10)

        self.cuota_visita = Entry(self.resultados_frame)
        self.cuota_visita.config(state = "readonly", justify = CENTER)
        self.cuota_visita.grid(row = 5, column = 2, padx = 10, pady = 10)