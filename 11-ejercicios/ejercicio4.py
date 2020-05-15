"""
Ejercicio 4

  Crear un script que tenga 4 variables, una lista, un string, un entero y
  un booleano y que imprima un mensaje según el tipo de dato de cada variable.
  Usar funciones

"""

def traducirTipo(tipo):

  resultado = ""

  if tipo == list:
    resultado = "lista"
  elif tipo == str:
    resultado = "cadena de texto"
  elif tipo == int:
    resultado = "entero"
  elif tipo == bool:
    resultado = "booleano"
  else:
    resultado = "desconocido"

  return resultado


def definirTipo(variable, tipo):

  resultado = ""

  if isinstance(variable, tipo):
    resultado = f"Esta variable es de tipo {traducirTipo(type(variable))}"
  else:
    resultado = f"Esta variable no es de tipo {traducirTipo(tipo)}, es {traducirTipo(type(variable))}"

  return resultado

lista = [1, 2, 3, 4, 5]
cadena_caracteres = "Soy un string"
numero = 26
booleano = True

print(definirTipo(lista, list))
print(definirTipo(cadena_caracteres, str))
print(definirTipo(numero, int))
print(definirTipo(booleano, bool))
