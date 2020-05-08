"""
Ejercicio 2

  - Escribir un script que nos muestre por pantalla
    todos lo números pares del 1 al 100

 """

for contador in range(1, 121):
  if contador % 2 == 0:
    print(f"{contador} es par")
  else:
    print(f"{contador} es impar")
print("Lista de números pares terminada.")
