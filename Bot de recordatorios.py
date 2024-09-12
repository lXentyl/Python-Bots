import smtplib
import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuración del correo electrónico
def send_email(subject, message, to_email):
    # Detalles de tu cuenta de Gmail
    from_email = "arosabg1@gmail.com"
    password = "ooyj optu ojzy lxwl"  # Puede que necesites una contraseña de aplicaciones de Gmail

    # Crear el mensaje
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Configuración del servidor SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Iniciar la encriptación TLS
        server.login(from_email, password)  # Iniciar sesión
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)  # Enviar el correo
        server.quit()
        print(f"Recordatorio enviado a {to_email}")
    except Exception as e:
        print(f"Error enviando el correo: {e}")

# Función para programar un recordatorio
def schedule_reminder(time, subject, message, to_email):
    def job():
        send_email(subject, message, to_email)

    schedule.every().day.at(time).do(job)
    print(f"Recordatorio programado para las {time}")

# Ejemplo de programación de recordatorios
if __name__ == "__main__":
    # Datos del recordatorio
    reminder_time = "13:16"  # Hora en formato 24h (HH:MM)
    email_subject = "Recordatorio Diario"
    email_message = "¡No olvides revisar tu agenda hoy!"
    recipient_email = "armanymmg@gmail.com"  # Cambia al correo de quien recibirá el recordatorio

    # Programar el recordatorio
    schedule_reminder(reminder_time, email_subject, email_message, recipient_email)

    # Mantener el script corriendo para enviar los recordatorios
    while True:
        schedule.run_pending()
        time.sleep(1)
