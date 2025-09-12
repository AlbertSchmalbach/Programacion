import cv2
from pyzbar.pyzbar import decode
import tkinter as tk
from tkinter import filedialog, messagebox
import os


def decifrar_wifi_qr(ruta_imagen):
    """Lee una imagen desde ruta y devuelve una tupla (ssid, password) si contiene datos WIFI,
    o None si no contiene información de tipo WIFI. También puede devolver contenido crudo si no sigue
    el formato estándar.
    """
    if ruta_imagen is None or not os.path.isfile(ruta_imagen):
        return None

    imagen = cv2.imread(ruta_imagen)
    if imagen is None:
        return None

    datos = decode(imagen)
    resultados = []
    for obj in datos:
        contenido = obj.data.decode('utf-8')
        # Formato estándar: WIFI:T:WPA;S:SSID;P:contraseña;;
        if contenido.startswith('WIFI:'):
            # separar por ';' y extraer S: y P:
            partes = contenido.split(';')
            ssid = None
            pwd = None
            for parte in partes:
                if parte.startswith('S:'):
                    ssid = parte[2:]
                if parte.startswith('P:'):
                    pwd = parte[2:]
            resultados.append(('WIFI', ssid, pwd))
        else:
            resultados.append(('RAW', contenido))

    return resultados if resultados else None


def decodificar_ruta(ruta):
    res = decifrar_wifi_qr(ruta)
    if not res:
        return 'No se encontró información QR válida.'

    salida_lines = []
    for item in res:
        if item[0] == 'WIFI':
            _, ssid, pwd = item
            salida_lines.append(f'SSID: {ssid or "(desconocido)"}')
            salida_lines.append(f'Password: {pwd or "(vacía)"}')
        else:
            _, contenido = item
            salida_lines.append(f'Contenido: {contenido}')

    return '\n'.join(salida_lines)


def scan_from_camera():
    """Abre la cámara y busca un QR hasta que encuentre uno o el usuario presione 'q'.
    Retorna la lista de contenidos decodificados o None.
    """
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return None

    found = None
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            datos = decode(frame)
            if datos:
                # tomamos el primer QR detectado
                obj = datos[0]
                contenido = obj.data.decode('utf-8')
                # liberamos y retornamos resultados en el mismo formato
                if contenido.startswith('WIFI:'):
                    partes = contenido.split(';')
                    ssid = None
                    pwd = None
                    for parte in partes:
                        if parte.startswith('S:'):
                            ssid = parte[2:]
                        if parte.startswith('P:'):
                            pwd = parte[2:]
                    found = [('WIFI', ssid, pwd)]
                else:
                    found = [('RAW', contenido)]
                break

            cv2.imshow('Escanear QR - presiona q para salir', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

    return found


def build_gui():
    root = tk.Tk()
    root.title('Decifrar contraseña WiFi - QR')
    root.geometry('600x300')

    ruta_var = tk.StringVar()
    resultado_var = tk.StringVar()

    def seleccionar_imagen():
        ruta = filedialog.askopenfilename(title='Seleccionar imagen QR',
                                          filetypes=[('Imágenes', '*.png;*.jpg;*.jpeg;*.bmp;*.gif'), ('Todos', '*.*')])
        if ruta:
            ruta_var.set(ruta)
            resultado_var.set('')

    def decodificar():
        ruta = ruta_var.get()
        if not ruta:
            messagebox.showwarning('Aviso', 'Selecciona primero una imagen.')
            return
        salida = decodificar_ruta(ruta)
        resultado_var.set(salida)

    def escanear():
        messagebox.showinfo('Info', 'Se abrirá la cámara. Presiona q para detener el escaneo.')
        res = scan_from_camera()
        if not res:
            resultado_var.set('No se detectó ningún QR o la cámara no está disponible.')
            return
        # formatear resultado
        lines = []
        for item in res:
            if item[0] == 'WIFI':
                _, ssid, pwd = item
                lines.append(f'SSID: {ssid or "(desconocido)"}')
                lines.append(f'Password: {pwd or "(vacía)"}')
            else:
                _, contenido = item
                lines.append(f'Contenido: {contenido}')
        resultado_var.set('\n'.join(lines))

    # Widgets
    frm_top = tk.Frame(root)
    frm_top.pack(fill='x', padx=10, pady=10)

    tk.Label(frm_top, text='Imagen:').pack(side='left')
    tk.Entry(frm_top, textvariable=ruta_var, width=60).pack(side='left', padx=5)
    tk.Button(frm_top, text='Seleccionar', command=seleccionar_imagen).pack(side='left')

    frm_mid = tk.Frame(root)
    frm_mid.pack(fill='x', padx=10, pady=5)
    tk.Button(frm_mid, text='Decodificar', command=decodificar).pack(side='left', padx=5)
    tk.Button(frm_mid, text='Escanear cámara', command=escanear).pack(side='left', padx=5)
    tk.Button(frm_mid, text='Salir', command=root.destroy).pack(side='right')

    frm_bot = tk.Frame(root)
    frm_bot.pack(fill='both', expand=True, padx=10, pady=10)
    tk.Label(frm_bot, text='Resultado:').pack(anchor='nw')
    txt = tk.Text(frm_bot, wrap='word')
    txt.pack(fill='both', expand=True)

    # actualizar el text cuando resultado_var cambie
    def actualizar_text(*args):
        txt.delete('1.0', tk.END)
        txt.insert('1.0', resultado_var.get())

    resultado_var.trace_add('write', actualizar_text)

    root.mainloop()


if __name__ == '__main__':
    build_gui()

# Dependencias: opencv-python, pyzbar
# Instalación: pip install opencv-python pyzbar