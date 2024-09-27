# ejercicio de herencia y uso de SUPER
# Crear un sistema para una escuela con 2 clases principales PERSONA y ESTUDIANTE
# Persona: nombre, edad
# Estudiante : grado (ademas de un metodo que imprime el grado del estudiante)
# Se debera usar el Metodo INIT para reutilizar el codigo de la clase padre PERSONA en la clase ESTUDIANTE
# Crear una instancia de la clase Persona e imprimir sus atributos utilizando los metodos.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad




class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def imprimirdatos(self):
        print(self.nombre)
        print(self.edad)
        print(self.grado) 

class Trabajadores(Persona):
     def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

estudiantes = []

for i in range(3): 
    nombre = input("ingrese su nombre : ")
    edad = int(input("ingrese su edad : ")) 
    grado = input("ingrese su grado :") 

estudiante = Estudiante(nombre, edad, grado) 
estudiantes.append(estudiante) 


print("\nDATOS DEL ESTUDIANTE:")
for estudiante in estudiantes: 
    estudiante.imprimirdatos()
    print("-" * 20 )
