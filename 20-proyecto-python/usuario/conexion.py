import mysql.connector


def conectarBd():

    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="cynara020800",
        database="master_python",
        port=3306
    )

    cursor = database.cursor(buffered=True)

    return [database, cursor]
