from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

def info():
    MessageBox.showinfo("Informacion", "Hola mundo") # título, mensaje
    
def alert():
    MessageBox.showwarning("Alerta", "Sección sólo para administradores.")
    
def err():
    MessageBox.showerror("Error", "Ha ocurrido un error inesperado")
    
def question():
    resultado = MessageBox.askquestion("Salir", 
    "¿Está seguro que desea salir sin guardar?")

    if resultado == "yes":
        root.destroy()  # Destruir, alternativa a quit
        
def questionOkCancel():
    resultado = MessageBox.askokcancel("Salir", 
    "¿Sobreescribir fichero actual?")

    if resultado == True:
        pass
    
def reintentar():
    resultado = MessageBox.askretrycancel("Reintentar",
    "No se puede conectar")

    if resultado == True:
        pass
    
def selectColor():
    color = ColorChooser.askcolor(title="Elige un color")
    print(color)
    
def selectDirectory():
    directory = FileDialog.askdirectory(title="Abrir Directorio")
    print(directory)
    
def openFile():
    fichero = FileDialog.askopenfilename(title="Abrir un fichero")
    print(fichero)

root = Tk()
root.title('Mi ventana')
root.geometry("200x100")

Button(root, text = "Clícame", command=selectDirectory).pack()

root.mainloop()