# Capturar excepciones y manejar errores en código
# susceptible a fallas / errores.

"""
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
"""
# Múltiples excepciones

"""
try:
  numero = int(input("Número para elevarlo al cuadarado: "))

  print("El cuadrado es " + str(numero * numero))
except TypeError:
  print("¡¡Debes convertir tus cadenas a enteros!!")
#except ValueError:
# print("¡¡Introduce un número correcto!!")
except Exception as e:
  print(type(e))
  print("Ha ocurrido un error:", type(e).__name__)
"""

# Excepciones "perwonalizadas" o lanzar excepción

try:
  nombre = input("introduce el nombre: ")
  edad = int(input("Introduce la edad: "))

  if edad < 5 or edad > 110:
    raise ValueError("La edad introducida no es real")
  elif len(nombre) <= 1:
    raise ValueError("El nombre no está completo")
  else:
    print(f"¡¡Bienvenido al Master en Python {nombre}!!")
except ValueError:
  print("Introduce los datos correctamente")
except Exception as e:
  print("Existe un error: ", e)
