"""

Funciones:

Una función es un conjunto de instrucciones agrupadas bajo un nombre
concreto que pueden reutilizarse invocando a la función tantas veces
como sea necesario.

def nombreDeMiFuncion(parámetros):
  # Bloque / conjunto de instrucciones

nombreDeMiFuncion(mi_parametro)

"""
# Ejemplo 1

print("##### EJEMPLO 1 #####")

# Definir función
def muestraNombre():
  print("Víctor")
  print("Paco")
  print("Juan")
  print("Francisco")
  print("Aitor")
  print("Néstor")
  print("\n")

# Invocar función
muestraNombre()
muestraNombre()
muestraNombre()

# Ejemplo 2: parámetros
print("##### EJEMPLO 2 #####")

def mostrarTuNombre(nombre, edad):
  print(f"Tu nombre es: {nombre}")

  if edad >= 18:
    print("Y eres mayor de edad.")

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))

mostrarTuNombre(nombre, edad)
