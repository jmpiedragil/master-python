"""

LISTAS (arrays)

  - Son colecciones o conjuntos de datos / valores, bajo un único nombre.
  - Para acceder a esos valores podemos usar un índice numérico.

"""

pelicula = "Batman"

# Definir Lista
peliculas = ["Batman", "Spiderman", "El señor de los anillos"]
cantantes = list(('2pac', 'Drake', 'Jennifer López'))
years = list(range(2020, 2050))
variada = ["Javier", 30, 4.4, True, "Texto"]

"""
print(peliculas)
print(cantantes)
print(years)
print(variada)
"""

# Índices
pelicula = "otra cosa"
peliculas[1] = "Gran Torino"
peliculas[2] = "El hobbit"

print(peliculas)

print(peliculas[1])
print(peliculas[-2])
print(cantantes[1:3])
print(peliculas[2:])
