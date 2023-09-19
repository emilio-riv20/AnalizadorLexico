from Abstracto.Lexema import * 
from Abstracto.Numero import * 
from Instrucciones.Aritmetica import *
from Instrucciones.Texto import * 
from Instrucciones.Trigonometria import *
from Error import * 

Reservados = {
    'ROPERACIONES'      : 'operaciones', 
    'ROPERACION'        : 'operacion', 
    'RVALOR1'           : 'valor1', 
    'RVALOR2'           : 'valor2', 
    'RSUMA'             : 'suma', 
    'RRESTA'            : 'resta',
    'RMULTIPLICACION'   : 'multiplicacion',
    'RDIVISON'          : 'division',
    'RMOD'              : 'mod',
    'RPOTENCIA'         : 'potencia',
    'RSENO'             : 'seno',
    'RCOSENO'           : 'coseno',
    'RTANGENTE'         : 'tangente',
    'RRAIZ'             : 'raiz',
    'RINVERSO'          : 'inverso',
    'COMA'              : ',', 
    'PUNTO'             : '.', 
    'DPUNTOS'           : ':', 
    'CORI'              : '[', 
    'CORD'              : ']', 
    'LLAVEI'            : '{', 
    'LLAVED'            : '}', 
}

lexemas = list(Reservados.values())

global n_linea 
global n_columna 
global instrucciones 
global lista_lexemas 

n_linea = 1 
n_columna = 1 
lista_lexemas = [] 
instrucciones = [] 
lista_errores = [] 

def instruccion(cadena): 
    global n_linea 
    global n_columna 
    global lista_lexemas 
    lexema = '' 
    puntero = 0 
 
    while cadena: 
        char = cadena[puntero] 
        puntero += 1 
 
        if char == '"':       #! leemos nuestra cadena y al encontrar " que habre empieza a crear el token 
            lexema, cadena = armar_lexema(cadena[puntero:])
            if lexema and cadena: 
                n_columna += 1 
                #Armar lexema como clase 
                l = Lexema(lexema, n_linea, n_columna) 
 
                lista_lexemas.append(l)  #! Agregamos los lexemas a la lista_lexema 
                n_columna += len(lexema) + 1 
                puntero = 0 
 
        elif char.isdigit(): 
            token, cadena = armar_numero(cadena) 
            if token and cadena: 
                n_columna += 1 
                #! Armamos lexema como clase 
                n = Numero(token, n_linea, n_columna) 
 
                lista_lexemas.append(n) 
                n_columna += len(str(token)) + 1 
                puntero = 0 
 
        elif char == '[' or char == ']': 
            #! Armamos lexema como clase 
            c = Lexema(char, n_linea, n_columna) 
 
            lista_lexemas.append(c) 
            cadena = cadena[1:] 
            puntero = 0 
            n_columna += 1 
 
        elif char =="\t": 
            n_columna += 4 
            cadena = cadena[4:] 
            puntero = 0 
        elif char == "\n": 
            cadena = cadena[1:] 
            puntero = 0 
            n_linea += 1 
            n_columna = 1 
        elif char == ' ' or char == '\r' or char == '{' or char == '}' or char == ',' or char == '.' or char == ':': 
            n_columna += 1 
            cadena = cadena[1:] 
            puntero = 0 
        else: 
            lista_errores.append(Errores(char, n_linea, n_columna)) 
            cadena = cadena[1:] 
            puntero = 0 
            n_columna += 1 
 
 
    return lista_lexemas 

def armar_lexema(cadena): 
    global n_linea 
    global n_columna 
    global lista_lexemas 
    lexema = '' 
    puntero = '' 
 
    for char in cadena: 
        puntero += char 
        if char == '\"': 
            return lexema, cadena[len(puntero):]    #! si encuentra una  " termino de leer el token 
        else: 
            lexema += char   #! creamos nuestros Token 
    return None, None 
 
def armar_numero(cadena): 
    numero = '' 
    puntero = '' 
    is_decimal =  False 
 
    for char in cadena: 
        puntero += char 
        if char == '.': 
            is_decimal = True 
 
        if char == '"' or char == ' ' or char == '\n' or char == '\t': 
            if is_decimal: 
                return float(numero), cadena[len(puntero)-1:] 
            else: 
                return int(numero), cadena[len(puntero)-1:] 
        else: 
            if char != ',': #! si no es una coma lo agregamos al numero 
                numero += char 
    return None, None 

def operar(): 
    global lista_lexemas 
    global instrucciones 
    operacion = ''
    n1 = '' 
    n2 = '' 
 
    while lista_lexemas: 
        lexema = lista_lexemas.pop(0) 
        if lexema.operar(None) == 'operacion' or lexema.operar(None) == 'Operacion': 
            operacion = lista_lexemas.pop(0)
        elif lexema.operar(None) == 'valor1' or lexema.operar(None) == 'Valor1': 
            n1 = lista_lexemas.pop(0)
            if n1.operar(None) == '[': 
                n1 = operar()
        elif lexema.operar(None) ==  'valor2' or lexema.operar(None) ==  'Valor2': 
            n2 = lista_lexemas.pop(0) 
            if n2.operar(None) == '[': 
                n2 = operar() 
 
        if operacion and n1 and n2: 
            return Aritmetica(n1, n2, operacion, f'Inicio: {operacion.getFila()}: {operacion.getColumna()}', f'Fin: {n2.getFila()}: {n2.getColumna()}') 
        elif operacion and n1 and (operacion.operar(None) == 'seno' or operacion.operar(None) == 'coseno' or operacion.operar(None) == 'tangente'):
            return Trigonometria(n1, operacion, f'Inicio: {operacion.getFila()}: {operacion.getColumna()}', f'Fin: {n1.getFila()}:{n1.getColumna()}')
    return None 
 
def operar_(): 
    global instrucciones 
    while True: 
        operacion = operar() 
        if operacion: 
            instrucciones.append(operacion) 
        else: 
            break 
 
    return instrucciones 
 
def getErrores(): 
    global lista_errores 
    formatoErrores = '{\n'

    for i in range(len(lista_errores)):
        error = lista_errores[i]
        formatoErrores += error.operar(i+1)
        if i != len(lista_errores)-1:
            formatoErrores += ',\n'
        else:
            formatoErrores += '\n'

    formatoErrores += '}'
    return lista_errores

def ArchivoError():
    nombre = "ListaErrores"+".txt"
    with open(nombre, 'w') as f:
        f.write(getErrores())