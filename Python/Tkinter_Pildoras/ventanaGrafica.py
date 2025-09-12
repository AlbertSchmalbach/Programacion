import tkinter as tk  # Importa la biblioteca Tkinter para interfaces gráficas
import tkinter.font  # Importa el módulo de fuentes de Tkinter
from pathlib import Path  # Importa Path para manejar rutas de archivos

# Obtiene la carpeta actual donde se ejecuta el script
carpeta_actual = Path.cwd()

# Construye la ruta de la imagen a mostrar en la interfaz
ubicacion_img = Path(carpeta_actual, "Interfaces_Graficas", "desktop.png")


# Crea la ventana principal de la aplicación
root = tk.Tk()

# Configura el título de la ventana
root.title("Tkinter Python")
# Configura el color de fondo de la ventana
root.config(bg="#311F73")
# Establece el tamaño mínimo de la ventana
root.minsize(200, 200)
# Establece el tamaño inicial de la ventana
root.geometry("500x500")

# Crea dos fuentes personalizadas para los textos
cf1 = tkinter.font.Font(family="Arial", size=20, weight="bold")  # Fuente para el título
cf2 = tkinter.font.Font(family="Arial", size=16, weight="bold")  # Fuente para el subtítulo
# Crea y muestra la primera etiqueta (título)
tk.Label(root, text="Programa interfaces graficas", font=cf1, bg="#311F73", fg="white").pack(ipadx=10, ipady=10)
# Crea y muestra la segunda etiqueta (subtítulo)
tk.Label(root, text="Python Tkinter", font=cf2, bg="#311F73", fg="white").pack()

# Carga la imagen desde la ruta especificada
image = tk.PhotoImage(file=ubicacion_img)
# Crea y muestra una etiqueta con la imagen
tk.Label(root, image=image).pack()

# Inicia el bucle principal de la aplicación (ventana)
root.mainloop()