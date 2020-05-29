"""

Proyecto Python y MySQL:

- Abrir asistente
- Login o registro
- Si elegimos registro, crear usuario en la BD
- Si elegimos login, identifica al usuario y nos preguntará
- Creear nota, mostrar notas, borrarlas

"""

from usuario import acciones

ejecutar = acciones.Accion()

print("""
Acciones disponibles:
    - registro
    - login
""")

accion = input("Qué quieres hacer?: ")

if accion == "registro":

    ejecutar.registro()


elif accion == "login":

    ejecutar.login()
