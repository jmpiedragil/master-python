# Tkinter
# Módulo para crear interfaces gráficas de usuario

from tkinter import *


# Crear la ventana raíz

ventana = Tk()

# Cambio en el tañamaño de la ventana

ventana.geometry("750x450")

# Bloquear el tamaño de la ventana

ventana.resizable(0, 1)

# Arrancar y mostrar la ventana hasta que se cierre.

ventana.mainloop()
