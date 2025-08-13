import tkinter as tk

raiz = tk.Tk()

miFrame = tk.Frame(raiz, width=500, height=300)
miFrame.pack()

userLabel = tk.Label(miFrame, text="Usuario: ")
userLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

userNombre = tk.Entry(miFrame, justify="center")
userNombre.grid(row=0, column=1, padx=10, pady=10)

passLabel = tk.Label(miFrame, text="Contraseña: ")
passLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

cuadroPass = tk.Entry(miFrame, justify="center")
cuadroPass.grid(row=1, column=1, padx=10, pady=10)
cuadroPass.config(show="*")


raiz.mainloop()