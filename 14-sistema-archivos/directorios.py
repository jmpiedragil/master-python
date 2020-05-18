import os, shutil

# Crear carpeta
if not os.path.isdir("./14-sistema-archivos/mi-carpeta"):
  os.mkdir("./14-sistema-archivos/mi-carpeta")
else:
  print("Ya existe el directorio")

# Eliminar
#os.rmdir("./14-sistema-archivos/mi-carpeta")

# Copiar
#ruta_original = "./14-sistema-archivos/mi-carpeta"
#ruta_nueva =  "./14-sistema-archivos/mi-carpeta_COPIADA"

#shutil.copytree(ruta_original, ruta_nueva)

# Eliminar
os.rmdir("./14-sistema-archivos/mi-carpeta_COPIADA")
