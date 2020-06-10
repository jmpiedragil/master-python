# Tkinter
# Módulo para crear interfaces gráficas de usuario

from tkinter import *


# Crear la ventana raíz

ventana = Tk()

# Título de la ventana

ventana.title("Interfaz gráfica con Python y Javier Piedragil")

# Icono de la ventana

ventana.iconbitmap("./21-tkinter/imagenes/computer_desktop.ico")

# Cambio en el tañamaño de la ventana

ventana.geometry("750x450")

# Bloquear el tamaño de la ventana

ventana.resizable(0, 1)

# Arrancar y mostrar la ventana hasta que se cierre.

ventana.mainloop()
