# Importar módulo

import sqlite3

productos = None

# Conexión

conexion = sqlite3.connect('pruebas.db')

# Crear cursor

cursor = conexion.cursor()

# Crear tabla

cursor.execute("CREATE TABLE IF NOT EXISTS producto (" +
               "id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, " +
               "titulo VARCHAR(255), " +
               "descripcion TEXT, " +
               "precio INT(10))"
               )

# Insertar datos

cursor.execute("INSERT INTO producto VALUES (" +
               "null, " +
               "'Primer producto', " +
               "'Descripción de mi producto', " +
               "550)"
               )

# Guardar cambios

conexion.commit()

# Listar datos

cursor.execute("SELECT * FROM producto;")
productos = cursor.fetchall()

print(productos)

# Cerrar conexión

conexion.close()
