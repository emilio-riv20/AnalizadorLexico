import tkinter 
from tkinter import Text, ttk
from FuncionBotones import funciones
from tkinter import filedialog, messagebox

class Ventana:
    def ventana(self):
        #Ventana principal
        ventana = tkinter.Tk()
        ventana.title("Menú")
        ventana.geometry("700x500") #Coloca las dimensiones de la ventana

        def seleccion(event):
            seleccion = combo.get()
            if seleccion == "ABRIR":
                funciones.Abrir()
            elif seleccion == "GUARDAR":
                funciones.Guardar()
            elif seleccion == "GUARDAR COMO":
                funciones.GuardarComo()
            elif seleccion == "SALIR":
                exit()

        #ComboBox
        combo = ttk.Combobox(ventana, state="readonly", values=["Seleccione una opción","ABRIR", "GUARDAR", "GUARDAR COMO", "SALIR"])
        combo.place(x=10,y=10)
        combo.current(0)
        combo.bind("<<ComboboxSelected>>", seleccion)
        
        #Boton de analizar
        analizar = tkinter.Button(ventana, text="ANALIZAR", command= funciones.Analizar())
        analizar.place(x=175, y=10)

        #Boton de errores
        errores = tkinter.Button(ventana, text="ERRORES")
        errores.place(x=275, y=10)

        #Boton de reporte
        reporte = tkinter.Button(ventana, text="REPORTE")
        reporte.place(x=375, y=10)

        #Area de texto
        Area = Text(ventana)
        Area.place(x=20, y=50)

        ventana.mainloop() #Lleva el registro de lo que pasa en la ventana

if __name__ == '__main__':
    inicio = Ventana()
    inicio.ventana()
