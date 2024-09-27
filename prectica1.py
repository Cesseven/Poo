class Perro: 
    # Atributo de la clase 
    especie = 'Mamifero'
    
     #El método __init__ es llamado al crear el objeto
    def __init__(self, nombre, raza): 
        print(f"creando perro {nombre}, {raza}")

        # atributos de instancia 
        self.nombre = nombre
        self.raza = raza 
    def ladra(self):
        print("Guau")

    def camina(self, pasos): 
        print(f"Caminando {pasos} pasos ") 



mi_perro = Perro ("Jumper", "Border collie")
mi_perro.ladra()
mi_perro.camina(10) 


