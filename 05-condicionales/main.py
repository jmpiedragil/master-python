"""
# Condicional IF

SI se_cumple_esta_condición:
  Ejecutar grupo de instrucciones
SI NO:
  Se ejecutan otro grupo de instrucciones

if condicion:
  instrucciones
else:
  otras instrucciones

# Operadores de comparación

== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

"""

# Ejemplo 1

print("########## EJEMPLO 1 ##########")

color = input("Adivina cuál es mi color favorito: ")

if color == "rojo":
  print("¡¡Enhorabuena!!")
  print("El color es ROJO")
else:
  print("¡¡Color incorrecto!!")

# Ejemplo 2

print("\n########## EJEMPLO 2 ##########")

year = input("¿En qué año estamos?: ")

if int(year) >= 2021:
  print("Estamos de 2021 en adelante")
else:
  print("Es un año anterior a 2021")
