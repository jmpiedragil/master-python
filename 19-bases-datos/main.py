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

cursor = database.cursor(buffered=True)

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

"""
cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)
"""

# cursor.execute("INSERT INTO vehiculo VALUES(null, 'Opel', 'Astra', 18500)")

coches = [
    ('Seat', 'Ibiza', 5000),
    ('Renault', 'Clio', 15000),
    ('Citroen', 'Saxo', 2000),
    ('Mercedes', 'Clase C', 35000),
]

# cursor.executemany("INSERT INTO vehiculo VALUES (null, %s, %s, %s)", coches)

database.commit()

cursor.execute("""
    SELECT *
   FROM vehiculo
   WHERE precio <= 5000 AND marca = 'Seat'
""")

resultado = cursor.fetchall()

print("----------- Todos mis coches -----------")

for coche in resultado:
    print(coche[1], coche[3])

cursor.execute("SELECT * FROM vehiculo")

coche = cursor.fetchone()
print(coche)

cursor.execute("DELETE FROM vehiculo WHERE marca = 'Renault'")
database.commit()
