from tkinter import *

raiz = Tk()

miFrame = Frame(raiz)
miFrame.pack()

# -------------------- Pantalla ---------------------------------------------------
numeroPantalla = StringVar()
pantalla = Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#7FFF00", justify="right")

# -------------------- Pulsaciones teclado ---------------------------------------------------
def numeroPulsado(num):
    numeroPantalla.set(numeroPantalla.get() + num)
# -------------------- fila 1 ---------------------------------------------------
buton7 = Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
buton7.grid(row=2, column=1)
buton8 = Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
buton8.grid(row=2, column=2)
buton9 = Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
buton9.grid(row=2, column=3)
butonDiv = Button(miFrame, text="/", width=3)
butonDiv.grid(row=2, column=4)

# -------------------- fila 2 ---------------------------------------------------
buton4 = Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
buton4.grid(row=3, column=1)
buton5 = Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
buton5.grid(row=3, column=2)
buton6 = Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
buton6.grid(row=3, column=3)
butonMult = Button(miFrame, text="X", width=3)
butonMult.grid(row=3, column=4)

# -------------------- fila 3 ---------------------------------------------------
buton1 = Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
buton1.grid(row=4, column=1)
buton2 = Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
buton2.grid(row=4, column=2)
buton3 = Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
buton3.grid(row=4, column=3)
butonMenos = Button(miFrame, text="-", width=3)
butonMenos.grid(row=4, column=4)

# -------------------- fila 4 ---------------------------------------------------
butonGato = Button(miFrame, text="#", width=3)
butonGato.grid(row=5, column=1)
buton0 = Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
buton0.grid(row=5, column=2)
butonComa = Button(miFrame, text=",", width=3, command=lambda:numeroPulsado(","))
butonComa.grid(row=5, column=3)
butonIgual = Button(miFrame, text="=", width=3)
butonIgual.grid(row=5, column=4)

raiz.mainloop()