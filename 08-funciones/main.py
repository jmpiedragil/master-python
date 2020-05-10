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

# Ejemplo 3
print("##### EJEMPLO 3 #####")

def tabla(numero):
  print(f"Tabla de multiplicar del número: {numero}")

  for contador in range(11):
    operacion = numero * contador
    print(f"{numero} * {contador} = {operacion}")

  print("\n")

tabla(3)
tabla(7)
tabla(12)

# Ejemplo 3.1

print("---------------------------------------------")

for numero_tabla in range(1, 11):
  tabla(numero_tabla)

# Ejemplo 4
print("##### EJEMPLO 4 #####")

# Parámetros opcionales

def getEmpleado(nombre, dni = None):
  print("EMPLEADO")
  print(f"Nombre: {nombre}")

  if dni != None:
    print(f"DNI: {dni}")

getEmpleado("Javier Piedragil")
