from tkinter import *  # Importa todos los componentes de Tkinter
from tkinter import ttk  # Importa el módulo ttk para widgets mejorados
from tkinter import messagebox  # Importa el módulo para mostrar cuadros de mensaje

# Crea la ventana principal de la aplicación
vp = Tk()
# Establece el título de la ventana
vp.title("Interfaz Tkinter")
# Define el tamaño de la ventana principal
vp.geometry("450x430")

# Crea la barra de menú principal
menu = Menu(vp)
# Asocia la barra de menú a la ventana principal
vp.config(menu=menu)

# Crea un submenú llamado 'Archivos' dentro del menú principal
archivos = Menu(menu, tearoff=0)
# Agrega el submenú 'Archivos' a la barra de menú
menu.add_cascade(label="Archivos", menu=archivos)

# Agrega la opción 'Nuevo' al submenú, muestra mensaje al seleccionarla
archivos.add_command(label="Nuevo", command=lambda: messagebox.showinfo("Nuevo", "Nuevo archivo creado"))
# Agrega la opción 'Abrir' al submenú, muestra mensaje al seleccionarla
archivos.add_command(label="Abrir", command= lambda: messagebox.showinfo("Abrir", "Archivo abierto"))
# Agrega un separador visual en el submenú
archivos.add_separator()
# Agrega la opción 'Exit' para cerrar la aplicación
archivos.add_command(label="Exit", command= vp.destroy)

# Crea y coloca una etiqueta para el nombre completo
etq1 = Label(vp, text="Nombre Completo").grid(row=0,padx=8, pady=12, sticky="w")
# Crea y coloca un campo de entrada para el nombre completo
ent1 = Entry(vp, width=30).grid(row=0, column=1)

# Crea y coloca una etiqueta para el método de contacto
etq2 = Label(vp, text="¿Como nos comunicamos contigo?").grid(row=1, column=0, padx=8, pady=7)

# Variable para el checkbox de Email
var1 = IntVar()
# Crea y coloca un checkbox para Email
Checkbutton(vp, text="Email", variable=var1).grid(row=2, column=0, padx=8, sticky="w")

# Variable para el checkbox de WhatsApp
var2 = IntVar()
# Crea y coloca un checkbox para WhatsApp
Checkbutton(vp, text="WhastApp", variable=var2).grid(row=2, column=1, padx=8, sticky="w")

# Variable para los radiobuttons de sexo
v = IntVar()
# Crea y coloca una etiqueta para el sexo
etq3 = Label(vp, text="Sexo:").grid(row=4, column=0, padx=8, pady=7, sticky="w")
# Crea y coloca un radiobutton para 'Hombre'
Radiobutton(vp, text="Hombre", variable=v, value=1).grid(row=5, column=0, sticky="w", padx=8)
# Crea y coloca un radiobutton para 'Mujer'
Radiobutton(vp, text="Mujer", variable=v, value=2).grid(row=5, column=1, sticky="w", padx=8)

# Crea y coloca una etiqueta para lenguajes de programación
etq4 = Label(vp, text="Lenguajes de Programacion:").grid(row=6, column=0, padx=8, pady=7, sticky="w")
# Crea y coloca un combobox para seleccionar lenguaje de programación
cb = ttk.Combobox(vp, values=["Selecciona una opción", "Java", "Python", "JavaScript", "Otros"])
cb.current(0)  # Selecciona la opción por defecto
cb.grid(row=8, column=0, padx=8, pady=7)

# Crea y coloca una etiqueta para el área de texto
etq5 = Label(vp, text="Hablenos acerca de usted:").grid(row=9, column=0, padx=8, pady=7, sticky="w")
# Crea y coloca un área de texto para comentarios
text_area = Text(vp, width=25, height=5).grid(row=10, column=0, padx=8, pady=7, sticky="NS")

# Crea y coloca un botón para enviar el formulario
btn = Button(vp, text="Enviar", width=12, command=lambda: messagebox.showinfo("Envio", "Envio satisfatorio!!!")).grid(row=11, padx=8, pady=7, sticky="E")

# Inicia el bucle principal de la aplicación
vp.mainloop()
