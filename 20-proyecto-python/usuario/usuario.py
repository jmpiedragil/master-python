import mysql.connector

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

    # def registrar(self):

    # def indentificar(self):
