# Tkinter
# Módulo para crear interfaces gráficas de usuario

import tkinter as tk
import os.path


class Programa:

    def __init__(self):

        self.title = "Master en Python Con Víctor Robles"
        self.icon = "./imagenes/computer_desktop.ico"
        self.icon_alt = "./21-tkinter/imagenes/computer_desktop.ico"
        self.size = "770x470"
        self.resizable = False

    def cargar(self):

        # Crear la ventana raíz

        ventana = tk.Tk()

        self.ventana = ventana

        # Título de la ventana

        ventana.title(self.title)

        # Comprobar si existe un archivo

        ruta_icono = os.path.abspath(self.icon)

        if not os.path.isfile(ruta_icono):

            ruta_icono = os.path.abspath(self.icon_alt)

        # Icono de la ventana

        ventana.iconbitmap(ruta_icono)

        # Mostrar texto en el programa

        texto = tk.Label(ventana, text=ruta_icono)

        texto.pack()

        # Cambio en el tamaño de la ventana

        ventana.geometry(self.size)

        # Bloquear el tamaño de la ventana

        if self.resizable:

            ventana.resizable(1, 1)

        else:

            ventana.resizable(0, 0)

    def addTexto(self, texto):

        texto = tk.Label(self.ventana, text=texto)
        texto.pack()

    def mostrar(self):

        # Arrancar y mostrar la ventana hasta que se cierre.

        self.ventana.mainloop()


# Instanciar  mi programa

programa = Programa()

programa.cargar()

programa.addTexto("Hola")
programa.addTexto("soy un texto")
programa.addTexto("Bienvenido al Master en Python")
programa.addTexto("Soy Víctor Robles")
programa.addTexto("Sígueme en YouTube")

programa.mostrar()
