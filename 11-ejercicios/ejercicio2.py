"""

Ejercicio 2

  Escribir un programa que añada valores a una lista mientras que su
  longitud sea menor a 120 y luego mostrar la lista.
  Plus: Usar while y for.

"""

valores = []
valor = 0

print("############# Usando while #############")

while len(valores) < 120:
  valores.append(valor)
  valor += 1

for elemento in valores:
  print(f"Elemento {valores.index(elemento)}: {elemento}")
