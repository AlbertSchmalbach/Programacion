"""
Ventana de inicio de sesión para la panadería YULIPAN MAGANGUE
"""
import tkinter as tk
from tkinter import messagebox

class VentanaLogin:
    def __init__(self, master):
        self.master = master
        self.master.title("Login - Panadería YULIPAN MAGANGUE")
        self.master.geometry("300x200")
        
        self.label_usuario = tk.Label(master, text="Usuario:")
        self.label_usuario.pack(pady=5)
        self.entry_usuario = tk.Entry(master)
        self.entry_usuario.pack(pady=5)
        
        self.label_contrasena = tk.Label(master, text="Contraseña:")
        self.label_contrasena.pack(pady=5)
        self.entry_contrasena = tk.Entry(master, show="*")
        self.entry_contrasena.pack(pady=5)
        
        self.boton_login = tk.Button(master, text="Iniciar sesión", command=self.iniciar_sesion)
        self.boton_login.pack(pady=10)

    def iniciar_sesion(self):
        usuario = self.entry_usuario.get()
        contrasena = self.entry_contrasena.get()
        # Aquí se debe validar el usuario y contraseña con la base de datos
        if usuario == "admin" and contrasena == "admin":
            messagebox.showinfo("Login exitoso", "¡Bienvenido, administrador!")
            # Aquí se puede abrir la ventana principal del sistema
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
