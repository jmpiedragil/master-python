import os

# Crear carpeta
if not os.path.isdir("./14-sistema-archivos/mi-carpeta"):
  os.mkdir("./14-sistema-archivos/mi-carpeta")
else:
  print("Ya existe el directorio")

# Eliminar
os.rmdir("./14-sistema-archivos/mi-carpeta")
