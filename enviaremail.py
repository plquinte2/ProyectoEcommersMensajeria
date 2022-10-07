from email.message import EmailMessage
import smtplib
def enviar_email(email_destino,codigo):
    remitente = "quinterolf@uninorte.edu.co"
    destinatario = email_destino
    mensaje = "Ingrese el siguiente codigo: "+codigo+" para activar su cuenta"
    email = EmailMessage()
    email["From"] = remitente
    email["To"] = destinatario
    email["Subject"] = "Codigo de activacion mensajeria Mintic Grupo 13 2022002132"
    email.set_content(mensaje)
    smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
    smtp.starttls()
    smtp.login(remitente, "Martin13")
    smtp.sendmail(remitente, destinatario, email.as_string())
    smtp.quit()