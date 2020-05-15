"""
Ejercicio 4

  Crear un script que tenga 4 variables, una lista, un string, un entero y
  un booleano y que imprima un mensaje según el tipo de dato de cada variable.
  Usar funciones

"""
def definirTipo(variable):

  return type(variable)

lista = [1, 2, 3, 4, 5]
cadena_caracteres = "Soy un string"
numero = 26
booleano = True

print(definirTipo(lista))
print(definirTipo(cadena_caracteres))
print(definirTipo(numero))
print(definirTipo(booleano))
