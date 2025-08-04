import tkinter as tk

ventana = tk.Tk()

logo = tk.PhotoImage(file="ventanas/coffee.png")

lblMensaje = tk.Label(ventana, text="texto sobre imagen", compound="center", image=logo).pack()

ventana.mainloop()