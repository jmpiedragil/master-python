# Importar módulo

import sqlite3

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

# Guardar cambios

conexion.commit()

# Cerrar conexión

conexion.close()
