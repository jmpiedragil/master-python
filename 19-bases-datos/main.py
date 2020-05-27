import mysql.connector

# Conexión

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="cynara020800",
    database="master_python"
)

# ¿La conexión ha sido correcta?

# print(database)

# Cursor

cursor = database.cursor()

# Crear base de datos
"""
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)
"""

# Crear tablas

cursor.execute("""
    CREATE TABLE IF NOT EXISTS vehiculo(
        id INT(10) AUTO_INCREMENT NOT NULL,
        marca VARCHAR(40) NOT NULL,
        modelo VARCHAR(40) NOT NULL,
        precio FLOAT(10, 2) NOT NULL,
        CONSTRAINT pk_vehiculo PRIMARY KEY(id)
    )
""")

cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)
