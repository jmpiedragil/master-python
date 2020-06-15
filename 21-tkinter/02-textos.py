import tkinter as tk


ventana = tk.Tk()
ventana.geometry("700x500")

texto = tk.Label(ventana, text="Bienvenido a mi programa")
texto.config(fg="white", bg="#000000", padx=50, pady=20, font=("Consolas", 30))
texto.pack()

texto = tk.Label(ventana, text="Soy Javier M. Piedragil")
texto.config(height=3, bg="orange", font=("Arial", 18), padx=10, pady=20,
             cursor="spider")
texto.pack(anchor=tk.SE)

texto = tk.Label(ventana, text="Master en Python")
texto.config(height=3, bg="red", font=("Arial", 18), padx=10, pady=20,
             cursor="spider")
texto.pack(anchor=tk.NW)

ventana.mainloop()
