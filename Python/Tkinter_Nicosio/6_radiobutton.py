import tkinter as tk

def mostrarOpcion():
    if seleccion.get() == 1:
        mensaje = "Haz seleccionado Python"
    if seleccion.get() == 2:
        mensaje = "Haz seleccionado C++"
    if seleccion.get() == 3:
        mensaje = "Haz seleccionado Java"
    
    lbMensaje.config(text=mensaje)

ventana = tk.Tk()
seleccion = tk.IntVar()

rbtnPython = tk.Radiobutton(ventana, text='Python', variable=seleccion, value=1, command=mostrarOpcion).pack(anchor=tk.W)

rbtnCplus = tk.Radiobutton(ventana, text='C++', variable=seleccion, value=2, command=mostrarOpcion).pack(anchor=tk.W)

rbtnJava = tk.Radiobutton(ventana, text='Java', variable=seleccion, value=3, command=mostrarOpcion).pack(anchor=tk.W)

lbMensaje = tk.Label(ventana)
lbMensaje.pack()


ventana.mainloop()
