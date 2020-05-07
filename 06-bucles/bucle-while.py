"""

# Bucle WHILE
Estructura de control que itera o repite la ejecución
de una serie de instrucciones tantas veces como sea necesario,
hasta que deje de cumplirse la condición.

while condición:
  bloque de instrucciones
  actualización del contador

"""
contador = 1

while contador <= 100:
  print(f"Estoy en el número: {contador}")
  contador += 1

print("------------------------------------------")

contador = 1
muestrame = str(0)

while contador <= 100:
  muestrame = muestrame + ", " + str(contador)
  contador += 1

print(muestrame)
