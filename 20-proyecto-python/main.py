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
    print("\nOk, ¡¡Vamos a registrarte en el sistema!!!...")

    nombre = input("¿Cuál es tu nombre?: ")
    apellidos = input("¿Cuáles son tus apellidos?: ")
    email = input("Introduce tu email: ")
    password = input("Introduce tu contraseña: ")

elif accion == "login":
    print("¡¡Vale!! Identifícate en el sistema...")

    email = input("Introduce tu email: ")
    password = input("Introduce tu contraseña: ")
