import tkinter as tk


ventana = tk.Tk()

ventana.geometry("700x400")
ventana.title("Formularios en Tkinter | Víctor Robles")

# Texto encabezado

encabezado = tk.Label(ventana, text="Formularios con Tkinter - Víctor Robles")
encabezado.config(
    fg="white",
    bg="darkgrey",
    font=("Open Sans", 18),
    padx=10,
    pady=10
)

encabezado.grid(row=0, column=0, columnspan=2, sticky=tk.W)

# Label para el campo

label = tk.Label(ventana, text="Nombre")
label.grid(row=1, column=0, padx=5, pady=5)

# Campo de texto

campo_texto = tk.Entry(ventana)
campo_texto.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

ventana.mainloop()
