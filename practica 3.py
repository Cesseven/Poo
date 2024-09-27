# Ejercicio 3 Herencia 

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Mi nombre es {self.nombre} y tengo {self.edad} años."

class Estudiante(Persona):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)
        self.curso = curso

    def estudiar(self):
        return f"El estudiante {self.nombre} tiene {self.edad} años de edad y está en el curso de  {self.curso}."

# Crear un objeto de la clase Estudiante
persona1 = Estudiante(nombre= "Cesar",edad= 24,curso= "Programación")

# Llamar al método estudiar

print(persona1.presentarse())

# Llamar al método estudiar

print(persona1.estudiar())

