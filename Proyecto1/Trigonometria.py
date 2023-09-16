from Abstracto.Abstract  import Expression 
import math
 
class Trigonometria(Expression): 
 
    def __init__(self, left, tipo, fila, columna): 
        self.left = left 
        self.tipo = tipo 
        super().__init__(fila, columna) 
 
    def operar(self, arbol): 
        leftValue = '' 
 
        if self.left != None: 
            leftValue = self.left.operar(arbol) 
 
        if self.tipo.operar(arbol) == 'Seno': 
            return math.sin(math.radians(leftValue)) 

        else: 
            return None 
 
    def getFila(self): 
        return super().getFila() 
 
    def getColumna(self): 
        return super().getColumna() 