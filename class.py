class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre 
        self.edad = edad 

    def mostrar_informacion(self):
        print(f"Nombre:{self.nombre}, Edad: {self.edad}")


cantidad =int(input("cuantos usuarioas desea ingrear : "))
for i in range(cantidad):
    nombre = input("ingrese su nombre : ")
    edad = int(input("ingrese su edad"))



#crear una instancia de tipo de persona   
persona1 = Persona(nombre, edad)
persona1.mostrar_informacion  


