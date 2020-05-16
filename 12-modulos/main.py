"""

Módulos: Son funcionalidades ya hechas para reutilizar.

En Python hay muchos módulos, que los puedes consultar aquí:
https://docs.python.org/3/py-modindex.html

Podemos conseguir módulos que ya vienen en el lenguaje, módulos en internet y
también podemos crear nuestros módulos.

"""
#from mimodulo import holaMundo
from mimodulo import *
import datetime


# print(mimodulo.holaMundo("Javier Piedragil Gálvez"))

# print(mimodulo.calculadora(3, 5, True))

print(holaMundo("Javier Piedragil Gálvez"))

print(calculadora(3, 5, True))

# Módulo de fechas

print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d%m%y, %H:%M:%S")
print("Mi fecha personalizada", fecha_personalizada)

print(datetime.datetime.now().timestamp())
