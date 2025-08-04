import tkinter as tk
from tkinter import ttk


# función que convierte la temperatura ingresada en la caja de texto
def convertir_temp():
    temp_celsius = float(caja_temp_celsius.get())
    temp_kelvin = temp_celsius + 273.15
    temp_fahrenheit = temp_celsius*1.8 + 32
    etiqueta_temp_kelvin.config(text=f"Temperatura en K: {temp_kelvin}")
    etiqueta_temp_fahrenheit.config(
        text=f"Temperatura en ºF: {temp_fahrenheit}")

# Creando ventana principal
ventana = tk.Tk()

# título y un tamaño a la ventana
ventana.title("Conversor de temperatura")
ventana.config(width=400, height=300)

# etiqueta que indique al usuario que debe ingresar la temperatura en grados Celsius
etiqueta_temp_celsius = ttk.Label(text="Temperatura en ºC:")
etiqueta_temp_celsius.config(font=('Verdana', 10))
# ubicarla en algún lugar de la ventana
etiqueta_temp_celsius.place(x=20, y=20)

# caja de texto para introducir la temperatura
caja_temp_celsius = ttk.Entry()
# ubicarla en algún lugar de la ventana y un ancho fijo
caja_temp_celsius.place(x=200, y=20, width=60)

# Estilos del boton
s = ttk.Style()
s.configure(
    "MyButton.TButton",
    foreground="#000",
    background="cadet blue",
    padding=10,
    font=("Verdana", 10),
    
)

# botón para realizar la conversión
boton_convertir = ttk.Button(text="Convertir", command=convertir_temp, style='MyButton.TButton')
# ubicarla en algún lugar de la ventana y un ancho fijo
boton_convertir.place(x=20, y=60)

# etiqueta resultado de la conversión en kelvin
etiqueta_temp_kelvin = ttk.Label(text="Temperatura en K: n/a")
etiqueta_temp_kelvin.config(font=('Verdana', 10))
etiqueta_temp_kelvin.place(x=20, y=120)

# etiqueta resultado de la conversión en Fahrenheit
etiqueta_temp_fahrenheit = ttk.Label(text="Temperatura en ºF: n/a")
etiqueta_temp_fahrenheit.config(font=('Verdana', 10))
etiqueta_temp_fahrenheit.place(x=20, y=160)

# bucle principal del programa
ventana.mainloop()




