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

# Operadores lógicos
and Y
or  O
!   negación
not NO

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
continente = "Oceanía"
edad = 18
mayoria_edad = 18

if edad >= mayoria_edad:
  print(f"¡¡{nombre} es mayor de edad!!")

  if continente != "Europa":
    print("El usuario NO es europeo")
  else:
    print(f"Es europeo y de {ciudad}")
else:
  print(f"{nombre} No es mayor de edad")

# Ejemplo 4

print("\n########## EJEMPLO 4 ##########")

dia = int(input("Introduce el número del día de la semana: "))

"""
if dia == 1:
  print("Es lunes")
else:
  if dia == 2:
    print("Es martes")
  else:
    if dia == 3:
      print("Es miércoles")
    else:
      if dia == 4:
        print("Es jueves")
      else:
        if dia == 5:
          print("Es viernes")
        else:
          print("Es fin de semana")
"""

if dia == 1:
  print("Es lunes")
elif dia == 2:
  print("Es martes")
elif dia == 3:
  print("Es miércoles")
elif dia == 4:
  print("Es jueves")
elif dia == 5:
  print("Es viernes")
else:
  print("Es fin de semana")

# Ejemplo 5

print("\n########## EJEMPLO 5 ##########")

edad_minima = 18
edad_maxima = 65
edad_oficial = int(input("¿Tienes edad de trabajar? Introduce tu edad: "))

if edad_oficial >= edad_minima and edad_oficial <= edad_maxima:
  print("¡¡Está en edad de trabajar!!")
else:
  print("No está en edad de trabajar")

# Ejemplo 6

print("\n########## EJEMPLO 6 ##########")

pais = "Rusia"

if pais == "México" or pais == "España" or pais == "Colombia":
  print(f"¡¡{pais} es un país de habla hispana!!")
else:
  print(f"{pais} no es un país de habla hispana :C")

# Ejemplo 7

print("\n########## EJEMPLO 7 ##########")

pais = "España"

if not (pais == "México" or pais == "España" or pais == "Colombia"):
  print(f"{pais} no es un país de habla hispana :C")
else:
  print(f"¡¡{pais} es un país de habla hispana!!")
