import tkinter as tk


ventana = tk.Tk()
ventana.geometry("700x500")

texto = tk.Label(ventana, text="Bienvenido a mi programa")
texto.config(fg="white", bg="#000000", padx=50, pady=20, font=("Consolas", 30))
texto.pack()

texto = tk.Label(ventana, text="Soy Javier M. Piedragil")
texto.config(width=400, height=400, bg="orange")
texto.pack(anchor=tk.SE)

ventana.mainloop()
