"""

Ejercicio 8

  - Cuánto es el x por ciento de X número
    Ejemplo: ¿Cuánto es el 20% de 150.

"""

porcentaje_a_calcular = int(input("¿Cuál es el porcentaje que se quiere obtener?:  "))
numero = int(input("¿De qué número?: "))

print(f"El {porcentaje_a_calcular}% de {numero} es {(porcentaje_a_calcular * numero) / 100}")
