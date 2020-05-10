nombre = "Javier Piedragil Gálvez"

# Funciones generales
print(type(nombre))

# Detectar el tipado
comprobar = isinstance(nombre, int)

if comprobar:
  print("Esa variable es un string")
else:
  print("No es una cadena")

if not isinstance(nombre, float):
  print("La variable no es un número con decimales")

# Limpiar espacios
frase = "    mi contenido   "
print(frase)
print(frase.strip())

# Limpiar variables
year = 2022
print(year)
