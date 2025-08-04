"""
Archivo principal para iniciar la aplicación de la panadería YULIPAN MAGANGUE
"""
from interfaz.ventana_login import VentanaLogin
from interfaz.ventana_ventas import VentanaVentas


import tkinter as tk


if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaLogin(root)
    # ventana = VentanaVentas(root)
    root.mainloop()
