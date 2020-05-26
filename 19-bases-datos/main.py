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

cursor = database.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)
