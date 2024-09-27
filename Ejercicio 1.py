class Persona:
    def __init__(self, nombre, edad, ocupacion):
        self.nombre = nombre 
        self.edad = edad 
        self.ocupacion = ocupacion 

    def presentarse(self):
        print(f"Mi Nombre :{self.nombre}, y Edad: {self.edad}, Ocupacion {self.ocupacion}") 



persona1 = Persona(nombre="Cesar", edad ="24", ocupacion = "Estudiante")
persona2 = Persona(nombre="Mateo", edad ="5", ocupacion = "Estudiante") 

persona1.presentarse()
persona2.presentarse()




    