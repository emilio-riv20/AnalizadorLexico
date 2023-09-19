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
 
        if self.tipo.operar(arbol) == 'seno' or self.tipo.operar(arbol) == 'Seno': 
            res = math.sin(math.radians(leftValue))
            res = round(res, 4)
            return res
        elif self.tipo.operar(arbol) == 'coseno' or self.tipo.operar(arbol) == 'Coseno': 
            res = math.cos(math.radians(leftValue))
            res = round(res, 4)
            return res
        elif self.tipo.operar(arbol) == 'tangente' or self.tipo.operar(arbol) == 'Tangente': 
            res= math.tan(math.radians(leftValue))
            res = round(res, 4)
            return res

        else: 
            return None 
 
    def getFila(self): 
        return super().getFila() 
 
    def getColumna(self): 
        return super().getColumna() 