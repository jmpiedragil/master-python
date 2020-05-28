"""

Proyecto Python y MySQL:

- Abrir asistente
- Login o registro
- Si elegimos registro, crear usuario en la BD
- Si elegimos login, identifica al usuario y nos preguntará
- Creear nota, mostrar notas, borrarlas

"""

print("""
Acciones disponibles:
    - registro
    - login
""")

accion = input("Qué quieres hacer?: ")

if accion == "registro":
    print("Ok, ¡¡Vamos a registrarte en el sistema!!!...")
elif accion == "login":
    print("¡¡Vale!! Identifícate en el sistema...")
