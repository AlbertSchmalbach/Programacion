import sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, Menu
from pathlib import Path

current_file = Path.cwd()
icono = current_file / 'icono.ico'

ventana = tk.Tk()
ventana.geometry('400x300')
ventana.title('Entrada Texto')
ventana.iconbitmap(icono)


# width aqui es la cantidad de caracteres
entrada1 = ttk.Entry(ventana, width=30) 
entrada1.grid(row=0, column=0)

# Etiqueta(label)
etq1 = tk.Label(ventana, text='Contenido de caja de texto')
etq1.grid(row=1, column=0, columnspan=2)


def enviar():
    # Modificamos el texto del label
    etq1.config(text=entrada1.get())    
    # 1. Mensaje informativo
    messagebox.showinfo('Mensaje Informativo',entrada1.get())

def salir():
    opcion = messagebox.askquestion('Salir', '¿Esta seguro que desea salir?')
    
    if opcion == 'yes':
        ventana.quit()
        ventana.destroy()
        sys.exit()

def crear_menu():
    # Configuramos menu principal
    menu_principal = Menu(ventana)
    # Mostrar menu en la ventana principal
    ventana.config(menu=menu_principal)

    # SUBMENU ARCHIVO
    # tearoff = False o 0 => evitar que se separe menu de la interface
    submenu_archivo = Menu(menu_principal, tearoff=0)
    # Agregamos opcion al submenu archivo
    submenu_archivo.add_command(label='Nuevo')
    # Añadimos separador
    submenu_archivo.add_separator()
    # Agregamos la opcion de salir
    submenu_archivo.add_command(label='Salir', command=salir)
    # Agregamos submenu archivo a menu principal
    menu_principal.add_cascade(menu=submenu_archivo, label='Archivo')

    # SUBMENU AYUDA
    submenu_ayuda = Menu(menu_principal, tearoff=0)
    # Agregamos opcion de ayuda al submenu
    submenu_ayuda.add_command(label='Acerca De')
    # Agregamos submenu ayuda a menu principal
    menu_principal.add_cascade(menu=submenu_ayuda, label='Ayuda')
    
# Creamos un boton 
btn = ttk.Button(ventana, text='Enviar', command=enviar)
btn.grid(row=0, column=1)

crear_menu()


ventana.mainloop()