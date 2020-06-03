import nota.nota as modelo


class Accion:

    def crear(self, usuario):

        print(f"\n¡¡Ok {usuario[1]} Vamos a crear una nueva nota...")

        titulo = input("Introduce el título de tu nota: ")
        descripcion = input("Introduce el contenido de tu nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nPerfecto, has guardado la nota: {nota.titulo}")
        else:
            print(f"\nNo se ha guardado la nota, lo siento {usuario[1]}")

    def mostrar(self, usuario):

        print(f"\n¡¡Vale {usuario[1]}!! Aquí tienes tus notas: ")

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        for nota in notas:

            print("\n********************************************************")
            print(nota[2])
            print(nota[3])
            print("\n********************************************************")
