from io import open
import pathlib

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "\\14-sistema-archivos\\fichero_texto.txt"
print(ruta)

archivo_lectura = open(ruta, "r")

# Leer contenido
#contenido = archivo_lectura.read()

#print(contenido)

# Leer contenido y guardarlo en una lista
lista = archivo_lectura.readlines()

# Cerrar archivo
archivo_lectura.close()

for renglon in lista:
  lista_renglon = renglon.split()
  print(lista_renglon)
