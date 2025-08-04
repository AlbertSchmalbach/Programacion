from tkinter import Frame, Tk

ventana = Tk()
ventana.title("Primera ventana")
# ventana.geometry("500x300")
ventana.iconbitmap("Interfaces_Graficas/icon.ico")
# ventana.config(bg="turquoise4")
miFrame = Frame()
# miFrame.pack(fill="both", expand=1)
miFrame.pack()
miFrame.config(width="500", height="300", bg="SteelBlue4")
miFrame.config(bd=12, relief="ridge")
miFrame.config(cursor="arrow")
ventana.mainloop()