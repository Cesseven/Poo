#metodo contructor 

class Persona:
    pass
    def __init__(self,nombre,edad): 
        self.nombre = nombre 
        self.edad = edad 
    def descripcion(self): 
        return f"{self.nombre} tiene {self.edad}, años de edad"
    
    def comentario(self, frase):
        return f"dice : {self.nombre}", frase 
    

doctor = Persona("Cesar", 24) 

#print(doctor.nombre)
#print(doctor.descripcion()) 
#print(doctor.comentario("Hola que tal ??"))  


# modificar un atributo 

class Email:
    def __init__(self):
        self.enviado = False 

    def enviar_correo(self):
        self.enviado = True 

mi_correo = Email()

print(mi_correo.enviado) 

mi_correo.enviar_correo()

print(mi_correo.enviado)