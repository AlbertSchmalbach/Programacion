import tkinter as tk
from tkinter import ttk
import time

class VentanaReloj(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('400x250')
        self.resizable(0,0)
        self.title('Reloj')
        self.configure(bg='#164748')
        self.etiqueta = tk.Label(self, text='', font=('Arial', 60), fg='#F4ECF7', bg='#164748', padx=15, pady=15)
        self.etiqueta.place(x=25, y=54)
        self._actualizacion()

    def _actualizacion(self):
        hora = time.strftime('%H:%M:%S')
        self.etiqueta.configure(text=hora)
        self.after(1000, self._actualizacion)

if __name__ == '__main__':
    reloj = VentanaReloj()
    reloj.mainloop()