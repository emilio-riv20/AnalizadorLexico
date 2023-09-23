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

        if self.tipo.operar(arbol) == 'suma' or self.tipo.operar(arbol) == 'Suma': 
            return leftValue + rightValue 
        
        elif self.tipo.operar(arbol) == 'resta' or self.tipo.operar(arbol) == 'Resta': 
            return leftValue - rightValue 
        
        elif self.tipo.operar(arbol) == 'multiplicacion' or self.tipo.operar(arbol) == 'Multiplicacion':
            return leftValue * rightValue
        
        elif self.tipo.operar(arbol) == 'division' or self.tipo.operar(arbol) == 'Division':
            return leftValue / rightValue
        
        elif self.tipo.operar(arbol) == 'potencia' or self.tipo.operar(arbol) == 'Potencia':
            return leftValue ** rightValue
        
        elif self.tipo.operar(arbol) == 'mod' or self.tipo.operar(arbol) == 'Mod':
            return leftValue % rightValue
        
        elif self.tipo.operar(arbol) == 'raiz' or self.tipo.operar(arbol) == 'Raiz':
            return leftValue ** (1/rightValue)
        
        elif self.tipo.operar(arbol) == 'inverso' or self.tipo.operar(arbol) == 'Inverso':
            return 1/leftValue
        
        else: 
            return None 
        
    def getFila(self): 
        return super().getFila() 
 
    def getColumna(self): 
        return super().getColumna() 