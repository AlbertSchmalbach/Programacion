import tkinter as tk
from tkinter import ttk
from pathlib import Path

current_file = Path.cwd()
icono = current_file / 'icono.ico'

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Grid')
ventana.iconbitmap(icono)

# Definimos metodos
def evento1():
    boton1.config(text='Boton 1 Presionado')

def evento2():
    boton2.config(text='Boton 2 Presionado')

def evento4():
    boton4.config(text='Boton 4 Presionado', fg='blue', relief=tk.GROOVE, bg='cyan')

# Definimos 2 botones
boton1 = ttk.Button(ventana, text='Boton 1', command=evento1)
boton1.grid(row=0, column=0, sticky='NSWE', padx=20, pady=20, ipadx=10, ipady=10, columnspan=2, rowspan=2)
# boton2 = ttk.Button(ventana, text='Boton 2', command=evento2)
# boton2.grid(row=1, column=0, sticky='NSWE', padx=20, pady=20, ipadx=10, ipady=10)
# boton3 = ttk.Button(ventana, text='Boton 3')
# boton3.grid(row=0, column=1, sticky='NSWE', padx=20, pady=20, ipadx=10, ipady=10)
# boton4 = tk.Button(ventana, text='Boton 4', command=evento4)
# boton4.grid(row=1, column=1, sticky='NSWE', padx=20, pady=20, ipadx=10, ipady=10)
ventana.mainloop()