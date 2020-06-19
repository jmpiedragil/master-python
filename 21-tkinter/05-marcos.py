import tkinter as tk


ventana = tk.Tk()

ventana.title("Marcos | Master en Python")
ventana.geometry("700x700")

marco_padre = tk.Frame(ventana, width=250, height=250)

marco_padre.pack(side=tk.BOTTOM, anchor=tk.S, fill=tk.X, expand=tk.YES)

marco = tk.Frame(marco_padre, width=250, height=250)

marco.config(bg="red", bd=5, relief=tk.RAISED)
marco.pack(side=tk.LEFT, anchor=tk.SW)
marco.pack_propagate(False)

texto = tk.Label(marco, text="Primer marco")
texto.config(
    bg="red",
    fg="white",
    font=("Arial", 20),
    bd=3,
    relief=tk.SOLID
)
texto.pack(anchor=tk.CENTER, fill=tk.Y, expand=tk.YES)

marco = tk.Frame(marco_padre, width=250, height=250)

marco.config(bg="green", bd=5, relief=tk.RAISED)
marco.pack(side=tk.RIGHT, anchor=tk.SE)

marco_padre = tk.Frame(ventana, width=250, height=250)

marco_padre.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=tk.YES)

marco = tk.Frame(marco_padre, width=250, height=250)

marco.config(bg="blue", bd=5, relief=tk.RAISED)
marco.pack(side=tk.LEFT)

marco = tk.Frame(marco_padre, width=250, height=250)

marco.config(bg="orange", bd=5, relief=tk.RAISED)
marco.pack(side=tk.RIGHT)

ventana.mainloop()
