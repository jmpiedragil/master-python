"""
Ejercicio 6

  - Mostrar todas la tablas de multiplicar del 1 al 10
  - Mostrando el título de la tabla y las multiplicaciones.

"""

for contador in range(1, 11):
  print(f"\n########## Tabla del {contador} ##########")

  for contador2 in range(1, 11):
    print(f"{contador} * {contador2} = {contador * contador2}")

print("Fin de las tablas de multiplicar")
