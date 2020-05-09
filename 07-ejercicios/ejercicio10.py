"""

Ejercicio 10

  - El programa tiene que pedir la nota de 15 alumnos y sacar por pantalla
    cuántos han aprobado y cuántos ghan suspendido.

"""
aprobados = 0
suspendidos = 0
calificacion = 0

for contador in range(1, 16):
  calificacion = int(input(f"Favor de introducir la nota del alumno {contador}: "))

  if calificacion >= 6:
    aprobados += 1
  else:
    suspendidos += 1

print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos suspendidos: {suspendidos}")
