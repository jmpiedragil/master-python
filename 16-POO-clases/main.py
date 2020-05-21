# Programación orientada a objetos (POO u OOP)

# Definir una clase (molde para crear objetos de ese tipo (Coche) con
# características similares.)

class Coche:

  # Atributos o propiedades (variables)
  # Características del coche
  color = "Rojo"
  marca = "Ferrari"
  modelo = "Aventador"
  velocidad = 300
  caballaje = 500
  plazas = 2

  # Métodos, son acciones que hace el objeto (Coche) (funciones)

  def setColor(self, color):
    self.color = color

  def getColor(self):
    return self.color

  def setModelo(self, modelo):
    self.modelo = modelo

  def getModelo(self):
    return self.modelo

  def acelerar(self):
    self.velocidad += 1

  def frenar(self):
    self.velocidad -= 1

  def getVelocidad(self):
    return self.velocidad

  # Fin definición de clase

print("COCHE 1: ")

coche = Coche()

coche.setColor("amarillo")
coche.setModelo("Murciélago")

print(coche.marca, coche.getModelo(), coche.getColor())

print("Velocidad actual: ", coche.velocidad)

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()

print("Velocidad nueva: ", coche.velocidad)

print("-------------------------------------------------")

# Crear más objetos

print("COCHE 2: ")

coche2 = Coche()

print(coche2.getColor())
