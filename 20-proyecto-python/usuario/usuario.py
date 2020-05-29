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

    def registrar(self):

        fecha = "2020-01-29"
        sql = "INSERT INTO usuario VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, self.password,
                   fecha)

        cursor.execute(sql, usuario)
        database.commit()

        return [cursor.rowcount, self]

    # def indentificar(self):
