# herencia 1

class Pokemon: 
    pass
    def __init__(self, nombre, tipo):
        self.nombre = nombre 
        self.tipo = tipo 

    def descripcion(self): 
        return f"{self.nombre} es un pokemon de tipo : {self.tipo}"
    

class Pikachu(Pokemon):
    def ataque(self,tipoataque):
        return f"{self.nombre} Tiene tipo de ataque :",tipoataque 
    
class Charmander(Pokemon):
    def ataque(self,tipoataque):
        return f"{self.nombre} Tiene tipo de ataque :",tipoataque
    

nuevo_pokemon = Pikachu("MAX","ELECTRICO")

print(nuevo_pokemon.descripcion()) 
print(nuevo_pokemon.ataque(tipoataque= "BOLA ELECTRICA")) 
