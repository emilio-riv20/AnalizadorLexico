from Abstracto.Abstract  import Expression 
 
class Aritmetica(Expression): 
 
    def __init__(self, left, right, tipo, fila, columna): 
        self.left = left 
        self.right = right 
        self.tipo = tipo 
        super().__init__(fila, columna) 
 
    def operar(self, arbol): 
        leftValue = '' 
        rightValue = '' 
 
        if self.left != None: 
            leftValue = self.left.operar(arbol) 
        if self.right != None: 
            rightValue = self.right.operar(arbol) 
 
        if self.tipo.operar(arbol) == 'suma': 
            return leftValue + rightValue 
        elif self.tipo.operar(arbol) == 'resta': 
            return leftValue - rightValue 
        elif self.tipo.operar(arbol) == 'multiplicacion':
            return leftValue * rightValue
        elif self.tipo.operar(arbol) == 'division':
            return leftValue / rightValue
        elif self.tipo.operar(arbol) == 'potencia':
            return leftValue ** rightValue
        elif self.tipo.operar(arbol) == 'mod':
            return leftValue % rightValue
        else: 
            return None 
        
    def getFila(self): 
        return super().getFila() 
 
    def getColumna(self): 
        return super().getColumna() 