# PRIMERA FORMA =>

# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# your_email = 'beto21048@gmail.com'
# your_psswd = 'doxa jdfv bebj bvxn'

# recept_email = input('Para: ')

# msg = MIMEMultipart()
# msg['From'] = your_email
# msg['To'] = recept_email
# msg['Subject'] = input('Asunto: ')

# body = input('Contenido: ')

# msg.attach(MIMEText(body, 'plain'))

# smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
# smtp_server.starttls()
# smtp_server.login(your_email, your_psswd)

# smtp_server.sendmail(your_email, recept_email, msg.as_string())
# smtp_server.quit()
# print('mensaje enviado con exito!!!')

# SEGUNDA FORMA =>

import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = "beto21048@gmail.com"
EMAIL_PASSWORD = "doxa jdfv bebj bvxn"
email = EmailMessage()
email["Subject"] = input(str("Asunto: "))
email["From"] = input(str("Nombre: "))
email["To"] = input(str("Para: "))
print('Contenido: ')
email.set_content(input(""))
print('Enviando...')
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
server.send_message(email)
server.quit()
print("emails enviados con exito!!!!😎")


