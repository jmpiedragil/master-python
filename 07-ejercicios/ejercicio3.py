"""
Ejercicio 3
  - Escribir un programa que muestre un cuadrados (un número multiplicado
  por sí mismo) de los primeros 60 números naturales.
  - Resolverlo con las estructuras for y while.

"""

# While
contador = 0

while contador <= 60:
  print(f"El cuadrado de {contador} es {contador * contador}")
  contador += 1

print("Lista terminada")

# for
for contador in range(0, 61):
  print(f"El cuadrado de {contador} es {contador * contador}")

print("Lista terminada")
