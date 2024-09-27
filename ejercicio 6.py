# Herencia parte 2


class Caculadora: 
    def __init__(self, numero): 
        self.n = numero 
        self.datos = [0 for i in range(numero)]

    def ingresar_dato (self):
        self.datos =[int (input("Ingresar datos" +str(i+1) + "= "))for i in range(self.n)] 
