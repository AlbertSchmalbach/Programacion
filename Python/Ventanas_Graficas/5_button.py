import tkinter as tk

ventana = tk.Tk()

texto = tk.StringVar()
texto.set('Saludar a mi chica')

def changeText():
    texto.set('Hola Luz Saray, te amo')


lb_etiqueta = tk.Label(ventana, textvariable=texto, font='Arial 20').pack()
btn_boton = tk.Button(ventana, text='Saluda', font='Arial 20', command=changeText).pack()

ventana.mainloop()