import tkinter as tk
from PIL import Image, ImageTk


ventana = tk.Tk()

ventana.geometry("700x500")

tk.Label(ventana, text="Hola soy Javier M. Piedragil Gálvez").pack(anchor=tk.W)

imagen = Image.open(
         './21-tkinter/imagenes/marc-olivier-jodoin-tauPAnOIGvE-unsplash.jpg')

render = ImageTk.PhotoImage(imagen)

tk.Label(ventana, image=render).pack(anchor=tk.E)

ventana.mainloop()
