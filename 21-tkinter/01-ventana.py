# Tkinter
# Módulo para crear interfaces gráficas de usuario

from tkinter import *
import os.path


# Crear la ventana raíz

ventana = Tk()

# Título de la ventana

ventana.title("Interfaz gráfica con Python y Javier Piedragil")

# Comprobar si existe un archivo

ruta_icono = os.path.abspath('./imagenes/computer_desktop.ico')

if not os.path.isfile(ruta_icono):

    ruta_icono = os.path.abspath('./21-tkinter/imagenes/computer_desktop.ico')

# Icono de la ventana

ventana.iconbitmap(ruta_icono)

# Mostrar texto en el programa

texto = Label(ventana, text=ruta_icono)

texto.pack()

# Cambio en el tañamaño de la ventana

ventana.geometry("750x450")

# Bloquear el tamaño de la ventana

ventana.resizable(0, 1)

# Arrancar y mostrar la ventana hasta que se cierre.

ventana.mainloop()
