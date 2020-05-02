"""
# Condicional IF

SI se_cumple_esta_condición:
  Ejecutar grupo de instrucciones
SI NO:
  Se ejecutan otro grupo de instrcciones

if condicion:
  instrucciones
else:
  otras instrucciones

"""

# Ejemplo 1

print("########## EJEMPLO 1 ##########")

color = input("Adivina cuál es mi color favorito: ")

if color == "rojo":
  print("¡¡Enhorabuena!!")
  print("El color es ROJO")
else:
  print("¡¡Color incorrecto!!")
