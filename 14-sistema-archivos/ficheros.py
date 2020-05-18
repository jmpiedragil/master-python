from io import open
import pathlib
import shutil

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
  print("- " + renglon.center(100))

# Copiar
#ruta_original = str(pathlib.Path().absolute()) + "\\14-sistema-archivos\\fichero_texto.txt"
#ruta_nueva = str(pathlib.Path().absolute()) + "\\14-sistema-archivos\\fichero_copiado.txt"
#ruta_alternativa = str(pathlib.Path().absolute()) + "/07-ejercicios/fichero_copiado77.txt"

#shutil.copyfile(ruta_original, ruta_alternativa)

# Mover
ruta_original = str(pathlib.Path().absolute()) + "\\14-sistema-archivos\\fichero_copiado.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "\\14-sistema-archivos\\fichero_copiado_NUEVO.txt"

shutil.move(ruta_original, ruta_nueva)
