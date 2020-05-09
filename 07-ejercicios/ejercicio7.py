"""

Ejercicio 7

  - Hacer un programa que muestre todos los números impares entre dos números que
    desida el usuario.

"""
primer_numero = int(input("Introduzca el primer número: "))
segundo_numero = int(input("Introduzca el segundo número: "))

resultado = str(primer_numero)

while primer_numero >= segundo_numero:
  print("El segundo número debe ser mayor al primero.")
  segundo_numero = int(input("Introduzca el segundo número: "))
else:
  for contador in range(primer_numero + 1, segundo_numero):
    if contador % 2 != 0:
      resultado = resultado + " " + str(contador)

print(resultado + " " + str(segundo_numero))
