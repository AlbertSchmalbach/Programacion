import tkinter as tk 
from tkinter import ttk, messagebox, scrolledtext
from pathlib import Path
from time import sleep

current_file = Path.cwd()
icono = current_file / 'icono.ico'
image = current_file / 'python-logo.png'

ventana = tk.Tk()
ventana.geometry('600x400+400+200')
ventana.title('Componentes')
ventana.iconbitmap(icono)

def crear_componentes_tab1(tabulador):
     # Agregar un a etiqueta y componente de entrada
    etiqueta1 = ttk.Label(tabulador, text='Nombre: ')
    etiqueta1.grid(row=0, column=0, sticky=tk.E)
    entrada1 = ttk.Entry(tabulador, width=30)
    entrada1.grid(row=0, column=1, padx=5, pady=5)
    # Agregamos un boton
    def enviar():
        messagebox.showinfo('Mensaje', f'Nombre: {entrada1.get()}')

    btn1 = ttk.Button(tabulador, text='Enviar', command=enviar)
    btn1.grid(row=1, column=0, columnspan=2)

def crear_componentes_tab2(tabulador):
    contenido = 'Este es el contenido de mi tabulador'
    # Creamos Scroll
    scroll = scrolledtext.ScrolledText(tabulador, width=50, height = 10, wrap = tk.WORD)
    scroll.insert(tk.INSERT, contenido)
    # Mostramos el componente
    scroll.grid(row=0, column=0)

def crear_componentes_tab3(tabulador):
    # Creamos una lista usando un list comprehensions
    datos = [x+1 for x in range(10)]
    combobox = ttk.Combobox(tabulador, width=15, values=datos)
    combobox.grid(row=0, column=0, padx=10, pady=10)
    # Seleccionamos un elemneto por default a mostrar.
    combobox.current(6)
    # Definimos metodo mostrar_valor
    def mostrar_valor():
        messagebox.showinfo('Valor Seleccionado', f'El valor seleccionado es: {combobox.get()}')
    # Agregar un boton para saber que selecciono un usuario.
    btn1 = ttk.Button(tabulador, text='Mostrar valor seleccionado', command=mostrar_valor)
    btn1.grid(row=0, column=1)

def crear_componentes_tab4(tabulador):
    imagen = tk.PhotoImage(file='python-logo.png')
    # Definimos metodo para mostrar informacion de imagen
    def mostrar_titulo():
        messagebox.showinfo('Mas Info', f'Nombre Imagen: {imagen.cget("file")}')
    btn_imagen = ttk.Button(tabulador, image=imagen, command=mostrar_titulo)
    btn_imagen.grid(row=0, column=0)

def crear_componentes_tab5(tabulador):
    # Creamos componente de barra de progreso.
    barra_progreso = ttk.Progressbar(tabulador, orient='horizontal', length=550)
    barra_progreso.grid(row=0, column=0, padx=10, pady=10, columnspan=4)
    # Metodos para controlar los eventos de la barra de progreso.
    def ejecutar_barra():
        barra_progreso['maximum'] = 100
        for valor in range(101):
            # Mandamos a esperar un poco antes de ejecutar
            sleep(0.09)
            # Incrementamos nuestra barra de progreso.
            barra_progreso['value'] = valor
            # Actualizamos barra de progreso.
            barra_progreso.update()
        barra_progreso['value'] = 0


    def ejecutar_ciclo():
        barra_progreso.start()

    def detener():
        barra_progreso.stop()

    def detener_despues():
        esperar_ms = 1000
        ventana.after(esperar_ms, barra_progreso.stop())

    # Botones para controlar los eventos de una barra de progreso
    boton_inicio = ttk.Button(tabulador, text='Ejecutar barra de progreso', command=ejecutar_barra)
    boton_inicio.grid(row=1, column=0)
    boton_ciclo = ttk.Button(tabulador, text='Ejecutar ciclo', command=ejecutar_ciclo)
    boton_ciclo.grid(row=1, column=1)
    boton_detener = ttk.Button(tabulador, text='Detener Ejecucion', command=detener)
    boton_detener.grid(row=1, column=2)
    boton_despues = ttk.Button(tabulador, text='Detener Ejecucion despues', command=detener_despues)
    boton_despues.grid(row=1, column=3)

def crear_tabs():
    # Creamos un tab controlador, para ello usamos la clase Notebook
    control_tabulador = ttk.Notebook(ventana)

    # Agregamos un Frame para agregar dentro del tab y organizar elementos
    tabulador1 = ttk.Frame(control_tabulador)
    # Agregamos el tabulador al control tabulador
    control_tabulador.add(tabulador1, text='Tabulador 1')
    # Mostramos el tabulador
    control_tabulador.pack(fill='both')

    crear_componentes_tab1(tabulador1)

    # Creamos un segundo tabulador
    tabulador2 = ttk.LabelFrame(control_tabulador, text='Contenido')
    control_tabulador.add(tabulador2, text='Tabulador 2')
    
    # Creamos los componentes del segundo tabulador
    crear_componentes_tab2(tabulador2)

    # Creamos un tercer tabulador
    tabulador3 = ttk.Frame(control_tabulador)
    control_tabulador.add(tabulador3, text='Tabulador 3')

    # Creamos componentes del tercer tabulador
    crear_componentes_tab3(tabulador3)

    # Creamos un cuarto tabulador
    tabulador4 = ttk.LabelFrame(control_tabulador, text='Imagen')
    control_tabulador.add(tabulador4, text='Tabulador 4')

    # Creamos componentes del tercer tabulador
    crear_componentes_tab4(tabulador4)

    # Creamos un quinto tabulador
    tabulador5 = ttk.LabelFrame(control_tabulador, text='Progress Bar')
    control_tabulador.add(tabulador5, text='Tabulador 5')

    # Creamos componentes del quinto tabulador
    crear_componentes_tab5(tabulador5)

crear_tabs()

ventana.mainloop()