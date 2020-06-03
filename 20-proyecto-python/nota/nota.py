import usuario.conexion as conexion


connect = conexion.conectarBd()
database = connect[0]
cursor = connect[1]


class Nota:

    def __init__(self, id_usuario, titulo="", descripcion=""):

        self.id_usuario = id_usuario
        self.titulo = titulo
        self.descripcion = descripcion

    def guardar(self):

        sql = "INSERT INTO nota VALUES(null, %s, %s, %s, NOW())"

        nota = (self.id_usuario, self.titulo, self.descripcion)

        cursor.execute(sql, nota)
        database.commit()

        return [cursor.rowcount, self]

    def listar(self):

        sql = f"SELECT * FROM nota WHERE id_usuario =  {self.id_usuario}"
        cursor.execute(sql)
        result = cursor.fetchall()

        return result
