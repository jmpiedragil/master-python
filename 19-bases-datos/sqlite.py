# Importar módulo

import sqlite3

productos = None

# Conexión

conexion = sqlite3.connect('./19-bases-datos/pruebas.db')

# Crear cursor

cursor = conexion.cursor()

# Crear tabla

cursor.execute("""
               CREATE TABLE IF NOT EXISTS producto (
                   id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                   titulo VARCHAR(255),
                   descripcion TEXT,
                   precio INT(10)
               );
               """
               )

# Insertar datos
"""
cursor.execute("INSERT INTO producto VALUES (" +
               "null, " +
               "'Primer producto', " +
               "'Descripción de mi producto', " +
               "550)"
               )
"""

# Borrar datos

# cursor.execute("DELETE FROM producto")

# Insertar muchos registros de golpe

productos = [
    ("Ordenador portátil", "Buen PC", 700),
    ("Teléfono móvil", "Buen teléfono", 140),
    ("Placa base", "Buena placa", 80),
    ("Tablet 15", "Buena tablet", 300),
]

# cursor.executemany("INSERT INTO producto VALUES(null,?, ?, ?)", productos)

# Modificar datos

cursor.execute("UPDATE producto SET precio = 678 WHERE precio = 80")

# Guardar cambios

conexion.commit()

# Listar datos

cursor.execute("SELECT * FROM producto WHERE precio >= 100;")
productos = cursor.fetchall()

for producto in productos:
    print(f"ID: {producto[0]}")
    print(f"Título: {producto[1]}")
    print(f"Descripción: {producto[2]}")
    print(f"Precio: {producto[3]}")
    print("--------------------------------")

cursor.execute("SELECT titulo FROM producto;")

producto = cursor.fetchone()
print(producto)

# Cerrar conexión

conexion.close()
