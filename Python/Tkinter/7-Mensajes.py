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


# width aqui es la cantidad de caracteres
entrada1 = ttk.Entry(ventana, width=30) # (show='*', state=tk.DISABLED, justify=tk.CENTER, state=tk.NORMAL)
entrada1.grid(row=0, column=0)

# Etiqueta(label)
etq1 = tk.Label(ventana, text='Contenido de caja de texto')
etq1.grid(row=1, column=0, columnspan=2)


def enviar():
    # Modificamos el texto del label
    etq1.config(text=entrada1.get())
    # Messagebox(Mensajes)
    # 1. Mensaje informativo
    # messagebox.showinfo('Mensaje Informativo',entrada1.get())
    # 2. Mensaje de Error
    # messagebox.showerror('Mensaje de Error', entrada1.get())
    # 3. Mensaje de alerta
    messagebox.showwarning('Alerta del sistema', entrada1.get())


# Creamos un boton 
btn = ttk.Button(ventana, text='Enviar', command=enviar)
btn.grid(row=0, column=1)

ventana.mainloop()