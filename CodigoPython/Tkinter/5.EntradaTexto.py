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

# insert -> agrega un texto
# entrada1.insert(0,'Introduce un texto')
# entrada1.insert(tk.END, '.')
# entrada1.config(state='readonly')

def enviar():
    # print(entrada1.get())
    # messagebox.showinfo('Texto Enviado', entrada1.get())
    # Eliminar entrada
    # entrada1.delete(0, tk.END)
    # Seleccionar el texto de la caja
    # entrada1.select_range(0, tk.END)
    # Hacer efectiva la seleccion del texto
    # entrada1.focus()

    # 2. Recuperamos la entrada a partir de la variable asociada
    # btn.config(text=entrada_var1.get())
    messagebox.showinfo('Mensaje', entrada_var1.get())
    # Modificamos contenido de variable con set()
    entrada_var1.set('Cambiando texto de entrada')
    # Recuperamos la info
    print(entrada_var1.get())
    print(entrada1.get())

# Creamos un boton 
btn = ttk.Button(ventana, text='Enviar', command=enviar)
btn.grid(row=0, column=1)
ventana.mainloop()