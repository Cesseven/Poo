class Persona:
    def __init__(self, nombre, edad, ocupacion):
        self.nombre = nombre 
        self.edad = edad 
        self.ocupacion = ocupacion 
    
    def presentarse(self):
        print(f"Mi Nombre es {self.nombre}, y tengo: {self.edad} años de edad , Ocupacion {self.ocupacion}")


class Estuduiante(Persona):
    def __init__(self, nombre, edad,ocupacion, curso):
        super().__init__(nombre, edad, ocupacion)
        self.curso = curso 

    def estudiar(self): 
        print(f"{self.nombre} esta estudiando el curso de {self.curso}")

estudiante1 = Estuduiante(nombre = "Nicol",edad = 21, ocupacion = "Trabajadora social", curso = "Metodologia")

estudiante1.presentarse()
estudiante1.estudiar()
