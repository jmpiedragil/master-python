"""
Ejercicio 9

  - Hacer un programa que pida números al usuario indefinidamente hasta que
    se capture el número 111

"""
numero_correcto = False
numero = 0

while not numero_correcto:
  numero = int(input("Introduzca un número: "))

  if numero == 111:
    numero_correcto = True
  else:
    print(f"{numero} no es el número correcto.")

print(f"¡¡¡{numero} es el número correcto!!!")
