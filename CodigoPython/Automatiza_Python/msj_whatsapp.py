import pywhatkit
import datetime

print("*** Enviar Mensaje por WhatsApp ***")

# envio de mensaje a una persona

# num_cel = input('Ingresa el numero de celular del destinatario: ')

# pywhatkit.sendwhatmsg(num_cel, "Hola otra vez", 10,46)


# envio mensaje a un grupo

# grupo_id = input("Ingrese ID del grupo: ")

id_grupo = "ElEObzrBaus1HMAtlUAKJ6"

# Verifica si hoy es día 10 del mes
hoy = datetime.datetime.now()
if hoy.day == 5:
    try:
        # Envía el mensaje al grupo
        mensaje = "Recordatorio => Se acerca la fecha limite de entrega del informe. Por favor, envienlo por el formulario."

        print(f"Enviando mensaje al grupo 4 con ID: {id_grupo}")
        print(f"Mensaje: {mensaje}")
        print("Presiona Ctrl+C para abortar antes de enviar el mensaje...")

        # Envía el mensaje a las 13:30 (1:30 PM) con un margen de 5 segundos
        pywhatkit.sendwhatmsg_to_group(id_grupo, mensaje, 13, 30, 5)

        print("Mensaje enviado al grupo.")

    except KeyboardInterrupt:
        # Manejo de la excepción KeyboardInterrupt
        # Esto se ejecutará si el usuario presiona Ctrl+C antes de enviar el mensaje
        print("\nTarea abortada por el usuario antes de enviar el mensaje.")
else:
    print("Hoy no es día de envío de informe.")

