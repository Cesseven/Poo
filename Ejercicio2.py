class Persona:
    def __init__(self, nombre, edad, ocupacion):
        self.nombre = nombre 
        self.__edad = edad 
        self.ocupacion = ocupacion 

    def presentarse(self):
        print(f"Mi Nombre es {self.nombre}, y tengo: {self.edad} años de edad , Ocupacion {self.ocupacion}") 

    def mostrar_edad(self): 
        return self.__edad 
    



persona1 = Persona(nombre="Cesar", edad ="24", ocupacion = "Estudiante")


print(f"La edad de {persona1.nombre} es {persona1.mostrar_edad()} años")


