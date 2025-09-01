import tkinter as tk

ventana = tk.Tk()

miTexto = "Mensaje escrito en Python. Me da gusto programar con interfaces graficas."

# 1 ejemplo
# msgMensagge = tk.Message(ventana, text=miTexto).pack()

# 2 ejemplo
# msgMensagge = tk.Message(ventana, text=miTexto, width=300).pack()

# 3 ejemplo
msgMensagge = tk.Message(ventana, text=miTexto)
msgMensagge.config(bg='SteelBlue', fg='white', font='time 24 bold',padx=12,  pady=12)
msgMensagge.pack()


ventana.mainloop()