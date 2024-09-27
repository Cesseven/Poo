class Persona: 
    def __init__(self, nombre, edad, ocupacion):
        self.nombre = nombre
        self.edad = edad 
        self.ocupacion = ocupacion

    def presentarse(self):
        return f"Mi nombre es {self.nombre} tengo {self.edad} años y soy {self.ocupacion}"

    def presentarse2(self): 
        return f"Mi nombre es {self.nombre} tengo {self.edad} años y soy el {self.ocupacion} de Cesar"
    





perosna1 = Persona("Cesar", 24,"Programador")
print(perosna1.presentarse())

persona2 = Persona("Mateo",5,"Hermano menor")
print(persona2.presentarse2())  
