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

encabezado.pack(anchor=tk.NW, side=tk.LEFT, fill=tk.X, expand=tk.YES)

ventana.mainloop()
