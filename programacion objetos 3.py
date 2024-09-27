# clase 3 metodos 

#  CLASS NOMBRE DE LA CLASE:
    #def NOMBRE DEL METODO (SELF):
#SELF.NOMBRE DE LA VARIABLE = ALGORITMO 
class Ropa: 
    def __init__(self,): 
        self.marca = "puma" 
        self.talla = "M" 
        self.color = " rojo"

camisa = Ropa() 
print(camisa.talla) 
print(camisa.color)   
print(camisa.marca)  

class Calculadora: 
    def __init__(self,n1,n2): 
        self.suma = n1 + n2 
        self.resta = n1 - n2 
        self.multiplicacion = n1 * n2 
        self.division = n2 / n2 

operacion = Calculadora(2,3)
print(operacion.multiplicacion) 