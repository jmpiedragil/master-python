import tkinter as tk


ventana = tk.Tk()

ventana.title("Marcos | Master en Python")
ventana.geometry("700x400")

marco = tk.Frame(ventana, width=250, height=250)

marco.config(bg="red", bd=12, relief="solid")
marco.pack()


ventana.mainloop()
