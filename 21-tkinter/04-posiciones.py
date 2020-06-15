import tkinter as tk


ventana = tk.Tk()
# ventana.geometry("700x500")

texto = tk.Label(ventana, text="Bienvenido a mi programa")
texto.config(fg="white", bg="#000000", padx=50, pady=20, font=("Consolas", 30))
texto.pack(side=tk.TOP)

texto = tk.Label(ventana, text="Soy Javier M. Piedragil")
texto.config(height=3, bg="orange", font=("Arial", 18), padx=10, pady=20,
             cursor="spider")
texto.pack(side=tk.TOP, fill=tk.X, expand=tk.YES)

texto = tk.Label(ventana, text="Básico 1")

texto.config(height=3, bg="green", font=("Arial", 18), padx=10, pady=20,
             cursor="spider")
texto.pack(anchor=tk.NW)

texto = tk.Label(ventana, text="Básico 2")

texto.config(height=3, bg="red", font=("Arial", 18), padx=10, pady=20,
             cursor="spider")
texto.pack(anchor=tk.NW)

texto = tk.Label(ventana, text="Básico 3")

texto.config(height=3, bg="orange", font=("Arial", 18), padx=10, pady=20,
             cursor="spider")
texto.pack(anchor=tk.NW)

ventana.mainloop()
