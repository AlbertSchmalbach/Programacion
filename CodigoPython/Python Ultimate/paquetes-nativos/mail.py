from email.message import EmailMessage
import ssl
import smtplib

email_emisor = "beto21048@gmail.com"
email_contrasena = "dcjs ochi wcvr ceys"

email_receptor = "albert2550@hotmail.com"

asunto = "Mensaje de prueba con Python"
cuerpo = """Cuerpo del mensaje generado desde python"""

correo = EmailMessage()
correo["From"] = email_emisor
correo["To"] = email_receptor
correo["Subject"] = asunto
correo.set_content(cuerpo)

contexto = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
    smtp.login(email_emisor, email_contrasena)
    smtp.send_message(email_emisor, email_receptor, correo.as_string())