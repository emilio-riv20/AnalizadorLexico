import tkinter 
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog, messagebox
from Analizador import *
from Analizador import ArchivoError, instruccion, operar_, limpiarLista, limpiarListaErrores


class Ventana:
    
    def __init__(self, ventana): 
        self.ventana = ventana 
        self.ventana.title("Editor de Texto") 
        self.ventana.geometry("700x500")
        self.ventana.resizable(0,0)
        self.ArchivoAbierto = None
        self.ejecutado = False #Detector de ejecucion de analisis

        self.botonA = tkinter.Button(ventana, text="Analizar", command=self.Analizar, background="lightblue")
        self.botonA.place(x=10, y=5)

        self.botonE = tkinter.Button(ventana, text="Errores", command=self.Errores, background="lightblue")
        self.botonE.place(x=80, y=5)

        self.botonG = tkinter.Button(ventana, text="Graficar", command=self.gh, background="lightblue")
        self.botonG.place(x=150, y=5)

        self.Texto = tkinter.Text(ventana, height=10, width=40, wrap=tkinter.WORD)
        barra = tkinter.Scrollbar(ventana, command=self.Texto.yview)
        self.Texto.config(yscrollcommand=barra.set)
        self.Texto.place(x=10, y=10)

        self.Texto.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=10, pady=40)
        barra.pack(side=tkinter.RIGHT, fill=tkinter.Y)
 
        self.menu_bar = tkinter.Menu(ventana) 
        self.ventana.config(menu=self.menu_bar) 

        self.file_menu = tkinter.Menu(self.menu_bar, tearoff=0, background="lightgray") 
        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu) 
        self.file_menu.add_command(label="Abrir", command=self.Abrir) 
        self.file_menu.add_command(label="Guardar", command=self.Guardar) 
        self.file_menu.add_command(label="Guardar Como", command=self.GuardarComo) 
        self.file_menu.add_separator() 
        self.file_menu.add_command(label="Salir", command=self.ventana.quit) 

        self.file_menu.entryconfigure("Abrir", background="lightgray", foreground="black")
        self.file_menu.entryconfigure("Guardar", background="lightgray", foreground="black")
        self.file_menu.entryconfigure("Guardar Como", background="lightgray", foreground="black")
        self.file_menu.entryconfigure("Salir", background="lightgray", foreground="black")

    def Analizar(self):
        try: 
            limpiarLista()
            limpiarListaErrores()
            instrucciones = instruccion(self.data) 
            respuestas_Operaciones = operar_() 
 
            Resultados = '' 
            Operacion = 1 
 
            configuracion = 1 
            salto = "\n" 
 
            for respuesta in respuestas_Operaciones: 
 
                if isinstance(respuesta.operar(None), int) or isinstance(respuesta.operar(None), float) == True: 
                    Resultados += str(f"operacion {Operacion} --> {respuesta.tipo.operar(None)} = {respuesta.operar(None)}\n")
                    print(respuesta.operar(None)) 
                    Operacion += 1 
                    self.ejecutado = True

            messagebox.showinfo("Analisis Exitoso", Resultados.lower()) 
        except: 
            messagebox.showinfo("Error", "No se ha ingresado ningun archivo") 

    def Errores(self):
        if self.ejecutado == False:
            messagebox.showerror("Error", "No se a ejecutado el analisis")
        else:
            try:
                ArchivoError()
                messagebox.showinfo("Éxito", "Archivo de errores generado con exito")
            except:
                messagebox.showerror("Error", "No se ha podido generar el archivo de errores")
                return

    def gh(self): 
        try: 
            operar_().clear() 
 
            intrucciones = instruccion(self.data) 
            operaciones = operar_() 
 
            contenido = "digraph G {\n\n"                           #CREAMOS NUESTRO ARCHIVO CON COMANDOS 
            r = open("Operaciones.dot", "w", encoding="utf-8") 
            contenido += str(self.Grafica(operaciones)) 
            contenido += '\n}' 

            r.write(contenido) 
            r.close() 
 
            print("...............................................................") 
            print("            ** COMANDOS DE GRAPHVIZ **               ") 
            print("") 
            print(contenido) 
            print("...............................................................") 
            print("") 
            print("FIN.....") 
            # ! dot -Tpng Operaciones.dot -o Operaciones.png 
            # ! Generar desde aquí la imagen 
 
        except Exception as e: 
            messagebox.showinfo("Se produjo un error: ",str(e)) 
            messagebox.showinfo("Mensaje", f"Error al generar el archivo de salida, Verificar el Archivo de entrada.") 
        else: 
            messagebox.showinfo("Mensaje", "Grafica generada con exito") 
            operaciones.clear() 
            intrucciones.clear() 

    def Grafica(Operaciones):
        Titulo = "" 
        colorNodo = "" 
        fuenteNodo = "" 
        formaNodo = ""
        try: 
            print('---------------------------------------------') 
            for respuesta in Operaciones: 
                if isinstance(respuesta.operar(None), int) or isinstance(respuesta.operar(None), float) == True: 
                    pass 
                else: 
                    temporal = str(respuesta.texto.operar(None)).lower() 
                    print(respuesta.texto.operar(None)) 
                    print(respuesta.ejecutarT()) 
                    if respuesta.ejecutarT() == "texto":  # Podemos recibir cualquier texto 
                        Titulo = str(respuesta.texto.operar(None)) 
                    if respuesta.ejecutarT() == "fondo":  # Vericar el color del nodo a asignar 
                        if temporal == ("amarillo" or "yellow"): 
                            temporal = "yellow" 
                            colorNodo = temporal 
                        elif temporal == ("verde" or "green"): 
                            temporal = "green" 
                            colorNodo = temporal 
                        elif temporal == ("azul" or "blue"): 
                            temporal = "blue" 
                            colorNodo = temporal 
                        elif temporal == ("rojo" or "red"): 
                            temporal = "red" 
                            colorNodo = temporal 
                        elif temporal == ("morado" or "purple"): 
                            temporal = "purple" 
                            colorNodo = temporal 
                        elif temporal == ("negro" or "black"): 
                            temporal = "black" 
                            colorNodo = temporal 


                    if respuesta.ejecutarT() == "fuente":  # Vericar la fuente del nodo a asignar 
 
                        if temporal == ("amarillo" or "yellow"): 
                            temporal = "yellow" 
                            fuenteNodo = temporal 
                        elif temporal == ("verde" or "green"): 
                            temporal = "green" 
                            fuenteNodo = temporal 
                        elif temporal == ("azul" or "blue"): 
                            temporal = "blue" 
                            fuenteNodo = temporal 
                        elif temporal == ("rojo" or "red"): 
                            temporal = "red" 
                            fuenteNodo = temporal 
                        elif temporal == ("morado" or "purple"): 
                            temporal = "purple" 
                            fuenteNodo = temporal 
                        elif temporal == ("negro" or "black"): 
                            temporal = "black" 
                            fuenteNodo = temporal 
 
                    if respuesta.ejecutarT() == "forma":  # Vericar el formato de nodo a asignar 
                        if temporal == ("circulo" or "circle"): 
                            temporal = "circle" 
                            formaNodo = temporal 
                        elif temporal == ("cuadrado" or "square"): 
                            temporal = "square" 
                            formaNodo = temporal 
                        elif temporal == ("triangulo" or "triangle"): 
                            temporal = "triangle" 
                            formaNodo = temporal 
                        elif temporal == ("rectangulo" or "box"): 
                            temporal = "box" 
                            formaNodo = temporal 
                        elif temporal == ("elipse" or "ellipse"): 
                            temporal = "ellipse" 
                            formaNodo = temporal 
 
            temporal = '' 
            CnumIzquierdo = 0 
            CnumDerecho = 0 
            Crespuesta = 0 
            Ctotal = 0 
 
            text = "" 
            text += f"\tnode [shape={formaNodo}]\n" 
            # text += f"\tnode [shape=box];\n" 
 
            text += f"\tnodo0 [label = \"{Titulo}\"]\n" 
            text += f"\tnodo0" + "[" + f"fontcolor = {fuenteNodo}" + "]\n" 
            # text += f"\tnodo0 [label = \"CambiarPorTexto\"]\n"    # ESTE DEJAR 
 
            for respuesta in Operaciones: 
                CnumIzquierdo += 1 
                CnumDerecho += 1 
                Crespuesta += 1 
                Ctotal += 1 
 
                if isinstance(respuesta.operar(None), int) or isinstance(respuesta.operar(None), float) == True: 
 
                    text += f"\tnodoRespuesta{Crespuesta}" + "[" + f"style = filled" + f",fillcolor = {colorNodo}" + f",fontcolor = {fuenteNodo}" + "]\n" 
                    text += f"\tnodoIzqu{CnumIzquierdo}" + "[" + f"style = filled" + f",fillcolor = {colorNodo}" + f",fontcolor = {fuenteNodo}" + "]\n" 
                    text += f"\tnodoDere{CnumDerecho}" + "[" + f"style = filled" + f",fillcolor = {colorNodo}" + f",fontcolor = {fuenteNodo}" + "]\n" 
                    text += f"\tnodoT{Ctotal}" + "[" + f"style = filled" + f",fillcolor = {colorNodo}" + f",fontcolor = {fuenteNodo}" + "]\n" 
 
                    text += f"\tnodoRespuesta{Crespuesta}" + f"[label = \"{str(respuesta.tipo.operar(None))}: " + "\"]\n" 
                    text += f"\tnodoIzqu{CnumIzquierdo}" + "[label = \"Valor1: " + f" {str(respuesta.left.operar(None))} " + "\"]\n" 
                    text += f"\tnodoDere{CnumDerecho}" + "[label = \"Valor2: " + f" {str(respuesta.right.operar(None))} " + "\"]\n" 
 
                    text += f"\tnodoRespuesta{Crespuesta} -> nodoIzqu{CnumIzquierdo}\n" 
                    text += f"\tnodoRespuesta{Crespuesta} -> nodoDere{CnumDerecho}\n" 
 
                    text += f"\tnodoT{Ctotal}" + f"[label = \"{respuesta.operar(None)}" + "\"]\n" 
                    text += f"\tnodoT{Ctotal} -> nodoRespuesta{Crespuesta}\n" 
 
                else: 
                    pass 
 
            return text 
        except Exception as e: 
            messagebox.showinfo("Se produjo un error: ",str(e)) 
            messagebox.showinfo("Mensaje", "Error en los comandos de Graphviz") 

    def Abrir(self):
        archivo = filedialog.askopenfilename(filetypes=[("Archivos Json", "*.json"),("Archivos de texto", "*.txt")],title="Seleccionar archivo de texto")
        if archivo:
                with open(archivo, "r") as entrada:
                    contenido = entrada.read()
                    self.Texto.delete(1.0, tkinter.END)
                    self.Texto.insert(tkinter.END, contenido)
                    self.ArchivoAbierto = archivo
        self.data = self.Texto.get(1.0, tkinter.END)

    def GuardarComo(self):
        archivo = filedialog.asksaveasfile(defaultextension=".txt",filetypes=[("Archivos Json", "*.json")],title="Guardar Como")
        texto = self.Texto.get(1.0, tkinter.END)
        if archivo:
            archivo.write(texto)
            archivo.close()

    def Guardar(self):
        texto = self.Texto.get(1.0, tkinter.END)
        if self.ArchivoAbierto:
                    try:
                        with open(self.ArchivoAbierto, 'w') as file:
                            file.write(self.Texto.get(1.0, tkinter.END))
                            messagebox.showinfo("Guardado", "Archivo guardado con exito")
                    except Exception as e:
                        messagebox.showerror("Error", f"Ocurrió un error al guardar el archivo: {str(e)}")
        else:
            self.GuardarComo()

if __name__ == '__main__':
    ventana = tkinter.Tk() 
    app = Ventana(ventana) 
    ventana.mainloop()
