import datetime
import hashlib
import usuario.conexion as conexion


connect = conexion.conectarBd()
database = connect[0]
cursor = connect[1]


class Usuario:

    def __init__(self, nombre, apellidos, email, password):

        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):

        fecha = datetime.datetime.now()

        # Cifrar contraseña

        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        sql = "INSERT INTO usuario VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email,
                   cifrado.hexdigest(), fecha)

        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result

    # def indentificar(self):
