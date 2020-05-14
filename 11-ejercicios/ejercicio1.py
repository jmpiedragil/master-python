"""

Ejercicio 1

  Hacer un programa que tenga una lista de 8 número enteros y haga lo siguiente:
  - Recorrer la lista y mostrarla
  - Hacer una función que recorra la lista de números y devuelva un string.
  - Ordenarla y mostrarla
  - Mostrar su longitud
  - Buscar algún elemento que el usuario pida por teclado

"""

numeros = [34, 56, 2, 143, 104, 0, 10, 17]
numero_a_buscar = 0

for numero in numeros:
  print(numero)

numeros.sort()

print(numeros)

print(f"La longitud de la lista es: {len(numeros)}")

numero_a_buscar = int(input("Introduzca el número a buscar: "))

if numero_a_buscar in numeros:
  print(f"¡El número {numero_a_buscar} existe en la lista!")
else:
  print(f"El número {numero_a_buscar} no existe en la lista")
