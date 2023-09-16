import tkinter 
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog, messagebox
from Analizador import *

class Ventana:

    def __init__(self, root): 
        self.root = root 
        self.root.title("Editor de Texto") 
 
        self.line_number_bar = tkinter.Text(root, width=4, padx=4, takefocus=0, border=0, background='lightgrey', state='disabled') 
        self.line_number_bar.pack(side=tkinter.LEFT, fill=tkinter.Y) 
 
        self.text_widget = ScrolledText(self.root, wrap=tkinter.WORD) 
        self.text_widget.pack(expand=True, fill='both') 
 
        self.text_widget.bind('<Key>', self.ActualizarLineas) 
        self.text_widget.bind('<MouseWheel>', self.ActualizarLineas) 
 
        self.current_line = 1 
 
        self.menu_bar = tkinter.Menu(root) 
        self.root.config(menu=self.menu_bar) 
 
        self.file_menu = tkinter.Menu(self.menu_bar, tearoff=0) 
        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu) 
        self.file_menu.add_command(label="Abrir", command=self.Abrir) 
        self.file_menu.add_command(label="Guardar", command=self.Guardar) 
        self.file_menu.add_command(label="Guardar Como", command=self.GuardarComo) 
        self.file_menu.add_separator() 
        self.file_menu.add_command(label="Salir", command=self.root.quit) 
        self.menu_bar.add_command(label="Analizar", command=self.Analizar) 
        self.menu_bar.add_command(label="Errores", command=self.Errores) 
 
    def ActualizarLineas(self, event=None): 
        line_count = self.text_widget.get('1.0', tkinter.END).count('\n') 
        if line_count != self.current_line: 
            self.line_number_bar.config(state=tkinter.NORMAL) 
            self.line_number_bar.delete(1.0, tkinter.END) 
            for line in range(1, line_count + 1): 
                self.line_number_bar.insert(tkinter.END, f"{line}\n") 
            self.line_number_bar.config(state=tkinter.DISABLED) 
            self.current_line = line_count 

    def Analizar(self):
        try: 
            instrucciones = instruccion(self.data) 
            respuestas_Operaciones = operar_() 
 
            Resultados = '' 
            Operacion = 1 
 
            configuracion = 1 
            salto = "\n" 
 
            for respuesta in respuestas_Operaciones: 
 
                if isinstance(respuesta.operar(None), int) or isinstance(respuesta.operar(None), float) == True: 
                    Resultados += str(f"Operacion {Operacion} --> {respuesta.tipo.operar(None)} = {respuesta.operar(None)}\n") 
                    print(respuesta.operar(None)) 
                    Operacion += 1 
 
 
 
            messagebox.showinfo("Analisis Exitoso", Resultados) 
        except: 
            messagebox.showinfo("Error", "No se ha ingresado ningun archivo") 

    def Errores(self):
        lista_errores = getErrores() 
        for error in lista_errores: 
            cont = 1 
            er = error.operar(cont) 
            cont += 1 
            print(er) 

    def Abrir(self):
        archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")],title="Seleccionar archivo de texto")
        if archivo:
                with open(archivo, "r") as entrada:
                    contenido = entrada.read()
                    self.text_widget.delete(1.0, tkinter.END)
                    self.text_widget.insert(tkinter.END, contenido)
                self.ActualizarLineas()
        self.data = self.text_widget.get(1.0, tkinter.END)

    def GuardarComo(self):
        filedialog.asksaveasfile()

    def Guardar(self):
        filedialog.askdirectory()

if __name__ == '__main__':
    root = tkinter.Tk() 
    app = Ventana(root) 
    root.mainloop()
