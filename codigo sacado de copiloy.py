class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def imprimirdatos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Grado: {self.grado}")

class Trabajador(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def imprimirdatos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Sueldo: ${self.sueldo:.2f}")

# Crear un objeto de la clase Trabajador
trabajador1 = Trabajador(nombre="Pedro", edad=35, sueldo=45000.0)

# Mostrar los datos del trabajador
print("\nDatos del trabajador:")
trabajador1.imprimirdatos()
