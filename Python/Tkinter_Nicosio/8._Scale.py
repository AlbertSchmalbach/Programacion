import tkinter as tk


def sumar(n):
    res = vertical.get() + horizontal.get()
    lb_mensaje.config(text=str(res)+' --- ' + str(n))


ventana = tk.Tk()

vertical = tk.IntVar()

sliderv = tk.Scale(ventana, from_=0, to=50, variable=vertical, command=sumar).pack()

vertical.set(25)

horizontal = tk.IntVar()
sliderh = tk.Scale(ventana, from_=0, to=100, orient=tk.HORIZONTAL, variable=horizontal, command=sumar).pack()

lb_mensaje = tk.Label(ventana)
lb_mensaje.pack()


ventana.mainloop()

