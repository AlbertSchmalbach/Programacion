import cv2
from pyzbar.pyzbar import decode

def decifrar_wifi_qr(ruta_imagen):
    # Carga la imagen del QR
    imagen = cv2.imread(ruta_imagen)
    # Decodifica el QR
    datos = decode(imagen)
    for obj in datos:
        contenido = obj.data.decode('utf-8')
        # El formato estándar es: WIFI:T:WPA;S:SSID;P:contraseña;;
        if contenido.startswith('WIFI:'):
            partes = contenido.split(';')
            for parte in partes:
                if parte.startswith('P:'):
                    return parte[2:]
    return None

# Ejemplo de uso
ruta = r'C:\Users\KHAdmin\Desktop\qr_wifi_salon.jpg'  # Cambia por la ruta de tu imagen
contrasena = decifrar_wifi_qr(ruta)
if contrasena:
    print(f'La contraseña es: {contrasena}')
else:
    print('No se encontró una contraseña WiFi en el QR.')