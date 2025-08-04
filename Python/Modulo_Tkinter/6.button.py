from tkinter import *

def sumar():
    r.set( int(n1.get()) + int(n2.get()) )
    borrar()

def resta():
    r.set( int(n1.get()) - int(n2.get()) )
    borrar()

def producto():
    r.set( int(n1.get()) * int(n2.get()) )
    borrar()

def borrar():
    n1.set("")
    n2.set("")

# Configuración de la raíz
root = Tk()
root.title('Operadora')
root.geometry("220x200")
root.config(bd=15)

n1 = StringVar()
n2 = StringVar()
r = StringVar()

Label(root, text="Número 1").pack()
Entry(root, justify="center", textvariable=n1).pack()

Label(root, text="Número 2").pack()
Entry(root, justify="center", textvariable=n2).pack()

Label(root, text="Resultado").pack()
Entry(root, justify="center", textvariable=r, state="disabled").pack()

Label(root, text="").pack()  # Separador

Button(root, text="Sumar", command=sumar, padx=10).pack(side="left")
Button(root, text="Resta", command=resta, padx=10).pack(side="left")
Button(root, text="Producto", command=producto, padx=10).pack(side="left")

# Finalmente bucle de la aplicación
root.mainloop()