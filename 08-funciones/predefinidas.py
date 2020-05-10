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

del year
# print(year)

# Comprobar variable vacía
texto = " ff  "

if len(texto) < 0:
  print("La variable está vacía")
else:
  print("La variable tiene contenido: ", len(texto))

# Encontrar caracteres
frase = "La vida es bella"
print(frase.find("vida"))

# Reemplazar pálabras en un string
nueva_frase = frase.replace("vida", "moto")
print(nueva_frase)

# Mayúsculas y minúsculas
print(nombre)
print(nombre.lower())
print(nombre.upper())
