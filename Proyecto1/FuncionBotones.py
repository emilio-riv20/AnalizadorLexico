import tkinter 
from tkinter import ttk
from tkinter import filedialog, messagebox

class Funciones():

    def Analizar(self):
        pass

    def Abrir(self):
        archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")],title="Seleccionar archivo de texto")
        if archivo:
            try:
                with open(archivo, "r") as entrada:
                    contenido = entrada.read()
            except Exception as e:
                print(e)

    def GuardarComo(self):
        filedialog.askdirectory()

    def Guardar(self):
        filedialog.askdirectory()


funciones = Funciones()