import mysql.connector
import datetime
import hashlib


database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="cynara020800",
    database="master_python",
    port=3306
)

cursor = database.cursor(buffered=True)


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
