import tkinter as tk


ventana = tk.Tk()

mensaje = """
    Una imagen vale más que mil palabras, así que aquí hay 15K 
    de generadores de imágenes de marcador de posición para usar 
    en sus maquetas y diseños.
"""

lblMensaje = tk.Label(ventana, text=mensaje, justify="left", fg="#2F4F4F", bg="#FFFAF0", font=('helvetica', 12, 'bold')).pack()

ventana.mainloop()