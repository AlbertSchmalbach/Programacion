import tkinter as tk
from tkinter import messagebox

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x450')
        self.resizable(0,0)
        self.title('Calculadora')
        self.iconbitmap('calculadora.ico')
        # Atributos de clase
        self.expresion = ''
        # Caja de texto (input)
        self.entrada = None
        # StringVar para obtener el valor del input
        self.entrada_texto = tk.StringVar()
        # cramos componentes
        self._creacion_componentes()

    # METODOS DE CLASE
    # 1. Metodo para crear los componentes
    def _creacion_componentes(self):
        # Creamos un frame para la caja de texto
        entrada_frame = tk.Frame(self, width=400, height=50, bg='grey')
        entrada_frame.pack(side=tk.TOP)
        # Entrada texto
        entrada = tk.Entry(entrada_frame, font=('arial', 18, 'bold'),
                           textvariable=self.entrada_texto, width=30,
                           justify=tk.RIGHT
                        )
        entrada.grid(row=0, column=0, ipady=10)

        # Creamos otro frame para la parte inferior
        botones_frame = tk.Frame(self, width=400, height=450, bg='grey')
        botones_frame.pack()

        # Primer renglon
        # Boton limpiar
        boton_limpiar = tk.Button(botones_frame, text='Limpiar', width=30, height=3, bd=0, bg='#eee', cursor='hand2', command=self._evento_limpiar)
        boton_limpiar.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
        # Boton dividir
        boton_dividir = tk.Button(botones_frame, text='/', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command=lambda: self._evento_click('/'))
        boton_dividir.grid(row=0, column=3, padx=1, pady=1)

    def _evento_limpiar(self):
        self.expresion = ''
        self.entrada_texto.set(self.expresion)

    def _evento_click(self, elemento):
        # Concatenamos el nuevo elemento a la expresion ya existente
        self.expresion = f'{self.expresion}{elemento}'
        self.entrada_texto.set(self.expresion)






if __name__ == '__main__':
    mi_calculadora = Calculadora()
    mi_calculadora.mainloop()