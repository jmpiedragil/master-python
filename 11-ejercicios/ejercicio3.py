"""
Ejercicio 3

  Programa que compruebe si una variable está vacía y si lo está, rellenarla
  con tecto en minúsculas y mostrarlo en mayúsculas.

"""

variable_a_probar = None

if variable_a_probar == None:
  variable_a_probar = "esta variable está vacía"
  print(variable_a_probar.upper())
else:
  print(f"La variable tiene contenido: {variable_a_probar}")
