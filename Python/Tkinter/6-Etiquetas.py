import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pathlib import Path

current_file = Path.cwd()
icono = current_file / 'icono.ico'

ventana = tk.Tk()
ventana.geometry('320x200')
ventana.title('Entrada Texto')
ventana.iconbitmap(icono)

# Definimos una variable que podremos modificar con (set) y leer con (get)
entrada_var1 = tk.StringVar(value='Valor por defecto')
# width aqui es la cantidad de caracteres
entrada1 = ttk.Entry(ventana, width=30, textvariable=entrada_var1) # (show='*', state=tk.DISABLED, justify=tk.CENTER, state=tk.NORMAL)
entrada1.grid(row=0, column=0)

# Etiqueta(label)
etq1 = tk.Label(ventana, text='Contenido de caja de texto')
etq1.grid(row=1, column=0, columnspan=2)


def enviar():
    # Modificamos el texto del label
    etq1.config(text=entrada_var1.get())

# Creamos un boton 
btn = ttk.Button(ventana, text='Enviar', command=enviar)
btn.grid(row=0, column=1)
ventana.mainloop()