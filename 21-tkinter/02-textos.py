import tkinter as tk


ventana = tk.Tk()
ventana.geometry("500x500")

texto = tk.Label(ventana, text="Bienvenido a mi programa")
texto.config(fg="white", bg="black")
texto.pack()

texto = tk.Label(ventana, text="Soy Javier M. Piedragil")
texto.pack()

ventana.mainloop()
