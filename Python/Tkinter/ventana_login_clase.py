import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pathlib import Path

class VentanaLogin(tk.Tk):
    def __init__(self):
        super().__init__()

        current_file = Path.cwd()
        icono = current_file / 'user_icon.ico'

        # Creamos ventana
        self.geometry('300x130')
        self.title('Login')
        self.iconbitmap(icono)
        self.resizable(0,0)

        # Configuracion del grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        # Creamos los componentes
        self._crear_componentes()

    def _crear_componentes(self):
        # Etiqueta usuario
        etq_usuario = tk.Label(self, text='Usuario: ')
        etq_usuario.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        # Etiqueta password
        etq_passwd = tk.Label(self, text='Password: ')
        etq_passwd.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)

        # Cajillas de entrada de datos
        # width aqui es la cantidad de caracteres
        self.entrada_usuario = ttk.Entry(self, width=30) 
        self.entrada_usuario.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        self.entrada_passwd = ttk.Entry(self, width=30, show='*') 
        self.entrada_passwd.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        # Creamos un boton 
        btn = ttk.Button(self, text='Login', command=self._logear)
        btn.grid(row=3, column=0, columnspan=2)

    def _logear(self):
        # Salida Login
        messagebox.showinfo('Datos Login', f'Usuario: {self.entrada_usuario.get()} - Password: {self.entrada_passwd.get()}')

    
if __name__ == '__main__':
    ventana_login = VentanaLogin()
    ventana_login.mainloop()