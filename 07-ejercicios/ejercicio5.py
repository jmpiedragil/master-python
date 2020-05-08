"""
Ejercicio 5
  - Hacer un programa que muestre todos los números entre dos números que
    capture el usuario.
"""

numero1 = int(input("Por favor introduzca el primer número: "))
numero2 = int(input("Por favor introduzca el segundo número: "))

while numero2 <= numero1:
  numero2 = int(input("El segundo número debe ser mayoy al primero. Introduzca el segundo número: "))

contador = numero1
numero2 += 1

resultado = ""

for contador in range(numero1, numero2):
  resultado = resultado + " " + str(contador)

print(resultado)
