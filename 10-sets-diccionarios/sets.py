"""
SET es un toipo de dato para tener una coleccoón de valores, pero no tiene ni índice ni orden.
"""

personas = {
  "Víctor",
  "Manolo",
  "Francisco"
}

personas.add("Paco")
personas.remove("Francisco")

print(type(personas))
print(personas)
