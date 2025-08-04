import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pathlib import Path

current_file = Path.cwd()
icono = current_file / 'user_icon.ico'

ventana = tk.Tk()
ventana.geometry('300x130')
ventana.title('Login')
ventana.iconbitmap(icono)
ventana.resizable(0,0)

# Configuracion del grid
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=3)

# Etiqueta usuario
etq_usuario = tk.Label(ventana, text='Usuario: ')
etq_usuario.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
# Etiqueta password
etq_passwd = tk.Label(ventana, text='Password: ')
etq_passwd.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)

# Cajillas de entrada de datos
# width aqui es la cantidad de caracteres
entrada_usuario = ttk.Entry(ventana, width=30) 
entrada_usuario.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)


entrada_passwd = ttk.Entry(ventana, width=30, show='*') 
entrada_passwd.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)


def logear():
    # Salida Login
    messagebox.showinfo('Datos Login', f'Usuario: {entrada_usuario.get()} - Password: {entrada_passwd.get()}')

# Creamos un boton 
btn = ttk.Button(ventana, text='Login', command=logear)
btn.grid(row=3, column=0, columnspan=2)
ventana.mainloop()