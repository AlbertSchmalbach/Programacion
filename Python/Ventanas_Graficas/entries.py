import tkinter as tk
from tkinter import messagebox

raiz = tk.Tk()

def validarUser():
    user = userEntry.get().lower()
    passwd = passEntry.get()

    if user == "albert" and passwd == "As_21048":
        messagebox.showinfo(message="Usuario validado!!!", title='User')
    else:
        messagebox.showinfo(message="Usuario no registrado", title='user')

miFrame = tk.Frame(raiz, width=500, height=300, padx=14, pady=12)
miFrame.pack()

userLabel = tk.Label(miFrame, text="Usuario: ", font="Arial 12")
userLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

userEntry = tk.Entry(miFrame, justify="center", width=40, font="Arial 12")
userEntry.grid(row=0, column=1, padx=10, pady=10, ipady=8)

# dirLabel = tk.Label(miFrame, text="Direccion: ", font="Arial 12")
# dirLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

# dirEntry = tk.Entry(miFrame, justify="center", width=40, font="Arial 12")
# dirEntry.grid(row=1, column=1, padx=10, pady=10, ipady=8)

passLabel = tk.Label(miFrame, text="Contraseña: ", font="Arial 12")
passLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

passEntry = tk.Entry(miFrame, justify="center", width=40, font="Arial 12")
passEntry.grid(row=2, column=1, padx=10, pady=10, ipady=8)
passEntry.config(show="*")

# comLabel = tk.Label(miFrame, text="Comentarios: ", font="Arial 12")
# comLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

# textComentarios = tk.Text(miFrame, width=40, height=12, font="Arial 12")
# textComentarios.grid(row=4, column=1, sticky="e", padx=10, pady=10)

# scrollVert = tk.Scrollbar(miFrame, command=textComentarios.yview)
# scrollVert.grid(row=4, column=2, sticky="nsew")

# textComentarios.config(yscrollcommand=scrollVert.set)

btnEnviar = tk.Button(raiz, text="Enviar", command=validarUser, width=16, height=2, font="Helvetica 16 bold", bg="Grey54").pack(padx=12, pady=12)

raiz.mainloop()