import tkinter as tk

# ventana grafica
ventana = tk.Tk()

def mostrar():

    mensaje = 'Producto agregado: '

    if(intCheck1.get() == 1):
        mensaje = mensaje + ' Piña'
    
    if(intCheck2.get() == 1):
        mensaje = mensaje + ' Sandia'
    else:
        mensaje = mensaje + ' Sin agregar'

    lbMensaje.config(text=mensaje)


# Estado check
intCheck1 = tk.IntVar()
intCheck2 = tk.IntVar()

# Label
lbMensaje = tk.Label(ventana)
lbMensaje.pack()

# Checkbox
check1 = tk.Checkbutton(ventana, text='Piña', variable=intCheck1).pack()
check2 = tk.Checkbutton(ventana, text='Sandia', variable=intCheck2).pack()

# boton
btnClick = tk.Button(ventana, text='Agregar al carrito', command=mostrar).pack()

ventana.mainloop()







