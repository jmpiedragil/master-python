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

  def acelerar(self):
    self.velocidad += 1

  def frenar(self):
    self.velocidad -= 1

  def getVelocidad(self):
    return self.velocidad

  # Fin definición de clase

coche = Coche

print(coche)
