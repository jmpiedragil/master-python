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

if int(year) < 2021:
  print("Estamos antes de 2021")
else:
  print("Es un año igual o posterior a 2021")

# Ejemplo 3

print("\n########## EJEMPLO 3 ##########")

nombre = "Javier Piedragil"
ciudad = "Barcelona"
continente = "Europa"
edad = 17
mayoria_edad = 18

if edad >= mayoria_edad:
  print(f"¡¡{nombre} es mayor de edad!!")

  if continente != "Europa":
    print("El usuario NO es europeo")
  else:
    print(f"Es europeo y de {ciudad}")
else:
  print(f"{nombre} No es mayor de edad")
