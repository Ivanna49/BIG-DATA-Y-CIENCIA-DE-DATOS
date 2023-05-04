# Clases y Objetos
'''
class Persona:
    nombre = ""
    apellido = ""
    edad = 0
    dni = 0
    donante = True
    
    def saludar(self):
        print("hola, soy", self.nombre)

p1 = Persona() #Aqui creo el objeto "p1" (instancia)
p1.nombre = "Juan Carlos"
p1.apellido = "Gomez"
p1.edad = 40
p1.dni = 20345678
p1.donante = True

# print(p1.nombre)

p2 = Persona()
p2.nombre = "Julieta"
p2.apellido = "Perez"
p2.edad = 35
p2.donante = False

print(p2)

p1.saludar()
p2.saludar()
'''

class Perro:
    nombre = ""
    raza = ""
    edad = 0
    
    def ladrar(self):
        print(self.nombre, "te saludua: Guau!")
        
    def envejecer(self):
        print("Feliz cumple!")
        self.edad += 1
        
dog1 = Perro()
dog1.nombre = "Firulais"
dog1.raza = "Mestizo"
dog1.edad = 3

dog1.ladrar()

dog2 = Perro()
dog2.raza = "Caniche"
dog2.nombre = "Tomy"
dog2.edad = 5

print(dog2.edad)
dog2.envejecer()
dog2.envejecer()
dog2.envejecer()
print(dog2.edad)
