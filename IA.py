class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre}.")

class Estudiante(Persona):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)
        self.curso = curso

    def estudiar(self):
        print(f"{self.nombre} está estudiando en el curso {self.curso}.")

# Crear un objeto de la clase Estudiante
estudiante1 = Estudiante(nombre="Juan", edad=20, curso="Matemáticas")

# Llamar a los métodos heredados de Persona
estudiante1.saludar()

# Llamar al método propio de Estudiante
estudiante1.estudiar()
