import usuario.usuario as modelo


class Accion:

    def registro(self):

        print("\nOk, ¡¡Vamos a registrarte en el sistema!!!...")

        nombre = input("¿Cuál es tu nombre?: ")
        apellidos = input("¿Cuáles son tus apellidos?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)

        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre}, " +
                  f"te has registrado con el email {registro[1].email}")

        else:
            print("\nNo te has registrado correctamente")

    def login(self):

        print("\n¡¡Vale!! Identifícate en el sistema...")

        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")

            usuario = modelo.Usuario("", "", email, password)

            login = usuario.indentificar()

            if email == login[3]:
                print(f"\nBienvenido {login[1]}, te has registrado en el " +
                      f"sistema el {login[5]}")
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print("¡¡Login incorrecto!! Inténtalo más tarde")