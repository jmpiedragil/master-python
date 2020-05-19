# Capturar excepciones y manejar errores en código
# susceptible a fallas / errores.

try:
  nombre = input("¿Cuál es tu nombre: ")

  if len(nombre) > 1:
    nombre_usuario = "El nombre es " + nombre

  print(nombre_usuario)
except:
  print("Ha ocurrido un error, mete bien el nombre")
else:
  print("Todo ha funcionado correctamente")
finally:
  print("¡¡Fin de la iteración!!")
