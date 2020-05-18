from io import open
import pathlib

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "\\14-sistema-archivos\\fichero_texto.txt"
print(ruta)

archivo_lectura = open(ruta, "r")

# Leer contenido
contenido = archivo_lectura.read()

print(contenido)

# Cerrar archivo
archivo_lectura.close()