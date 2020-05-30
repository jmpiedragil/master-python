import mysql.connector
from mysql.connector import Error


def conectarBd():

    try:

        conexionDb = mysql.connector.connect(
                   host="localhost",
                   user="root",
                   passwd="cynara020800",
                   database="master_python",
                   port=3306
        )

        if conexionDb.is_connected():
            cursor = conexionDb.cursor(buffered=True)

    except Error as e:

        print("Error al conectarse a la base de datos.", e)
        conexionDb = None
        cursor = None

    return [conexionDb, cursor]
