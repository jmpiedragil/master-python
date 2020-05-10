nombre = "Javier Piedragil Gálvez"

# Funciones generales
print(type(nombre))

# Detectar el tipado
comprobar = isinstance(nombre, str)

if comprobar:
  print("Esa variable es un string")
else:
  print("No es una cadena")
