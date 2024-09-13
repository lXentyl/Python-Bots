import smtplib
import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Función para enviar correo
def send_email(subject, message, to_email):
    from_email = "arosabg1@gmail.com"
    password = "ooyj optu ojzy lxwl"  # Puedes necesitar una contraseña de aplicación de Gmail

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print(f"Recordatorio enviado a {to_email}")
        messagebox.showinfo("Éxito", f"Correo enviado a {to_email}")
    except Exception as e:
        messagebox.showerror("Error", f"Error enviando el correo: {e}")

# Función para programar el recordatorio
def schedule_reminder(time, subject, message, to_email):
    def job():
        send_email(subject, message, to_email)

    schedule.every().day.at(time).do(job)
    print(f"Recordatorio programado para las {time}")
    messagebox.showinfo("Programado", f"Recordatorio programado para las {time}")

# Función para iniciar el programador de recordatorios
def start_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Interfaz gráfica
def create_gui():
    root = ttk.Window(themename="darkly")  # Tema moderno oscuro
    root.title("Programar Recordatorios")
    root.geometry("500x400")

    # Colores principales azul y dorado
    entry_bg = '#003366'  # Azul oscuro
    text_fg = '#FFD700'  # Dorado

    # Título
    ttk.Label(root, text="Programar Recordatorio", font=("Helvetica", 16), bootstyle=INFO).pack(pady=10)

    # Campo de correo
    ttk.Label(root, text="Correo de destino", bootstyle="primary").pack(pady=5)
    to_email_entry = ttk.Entry(root, width=40, bootstyle="info")
    to_email_entry.pack(pady=5)

    # Campo de hora
    ttk.Label(root, text="Hora del recordatorio (HH:MM)", bootstyle="primary").pack(pady=5)
    time_entry = ttk.Entry(root, width=40, bootstyle="info")
    time_entry.pack(pady=5)

    # Campo de asunto
    ttk.Label(root, text="Asunto del correo", bootstyle="primary").pack(pady=5)
    subject_entry = ttk.Entry(root, width=40, bootstyle="info")
    subject_entry.pack(pady=5)

    # Campo de mensaje
    ttk.Label(root, text="Mensaje del correo", bootstyle="primary").pack(pady=5)
    message_entry = ttk.Text(root, height=5, width=40)
    message_entry.pack(pady=5)

    # Botón para programar recordatorio
    def on_schedule_click():
        to_email = to_email_entry.get()
        reminder_time = time_entry.get()
        subject = subject_entry.get()
        message = message_entry.get("1.0", tk.END)
        schedule_reminder(reminder_time, subject, message, to_email)

    schedule_button = ttk.Button(root, text="Programar Recordatorio", bootstyle="success", command=on_schedule_click)
    schedule_button.pack(pady=20)

    # Icono animado (puedes cargar un gif animado)
    # Cargar un gif usando Pillow (si es necesario) y agregar a la interfaz

    root.mainloop()

# Llamar a la interfaz gráfica
create_gui()
