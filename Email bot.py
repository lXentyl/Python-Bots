import smtplib
import tkinter as tk
from tkinter import messagebox

# Función para enviar correo
def send_email():
    toaddrs = to_entry.get()
    fromaddrs = from_entry.get()
    message = message_entry.get("1.0", "end-1c")
    password = pass_entry.get()
    num_emails = int(num_emails_entry.get())  # Convertir a entero el número de correos

    # Convertimos el mensaje a UTF-8 para evitar problemas con caracteres especiales
    message = f"Subject: Mensaje\n\n{message}".encode('utf-8')

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtperver:
            smtperver.ehlo()
            smtperver.starttls()
            smtperver.ehlo()
            smtperver.login(fromaddrs, password)
            for i in range(num_emails):  # Utilizamos el número especificado
                smtperver.sendmail(fromaddrs, toaddrs, message)
                print(f"Correo {i+1} enviado")
        messagebox.showinfo("Éxito", f"Se enviaron {num_emails} correos correctamente")
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un error: {str(e)}")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Envío de Correos")
root.geometry("400x450")
root.configure(bg='#1a1a1a')  # Fondo negro

# Estilo moderno
entry_bg = '#2c2c2c'  # Fondo de las entradas en gris oscuro
text_fg = '#ffffff'   # Texto en blanco
button_bg = '#6a0dad' # Botones morados

# Etiquetas y entradas
tk.Label(root, text="Correo de destino", bg='#1a1a1a', fg=text_fg, font=("Helvetica", 10)).pack(pady=10)
to_entry = tk.Entry(root, width=40, bg=entry_bg, fg=text_fg, relief="flat", insertbackground='white')
to_entry.pack()

tk.Label(root, text="Correo de origen", bg='#1a1a1a', fg=text_fg, font=("Helvetica", 10)).pack(pady=10)
from_entry = tk.Entry(root, width=40, bg=entry_bg, fg=text_fg, relief="flat", insertbackground='white')
from_entry.pack()

tk.Label(root, text="Contraseña", bg='#1a1a1a', fg=text_fg, font=("Helvetica", 10)).pack(pady=10)
pass_entry = tk.Entry(root, width=40, bg=entry_bg, fg=text_fg, show="*", relief="flat", insertbackground='white')
pass_entry.pack()

tk.Label(root, text="Mensaje", bg='#1a1a1a', fg=text_fg, font=("Helvetica", 10)).pack(pady=10)
message_entry = tk.Text(root, height=5, width=40, bg=entry_bg, fg=text_fg, relief="flat", insertbackground='white')
message_entry.pack(pady=10)

# Entrada para el número de correos
tk.Label(root, text="Cantidad de correos a enviar", bg='#1a1a1a', fg=text_fg, font=("Helvetica", 10)).pack(pady=10)
num_emails_entry = tk.Entry(root, width=10, bg=entry_bg, fg=text_fg, relief="flat", insertbackground='white')
num_emails_entry.pack()

# Botón para enviar
send_button = tk.Button(root, text="Enviar", bg=button_bg, fg=text_fg, width=20, height=2, relief="flat", command=send_email)
send_button.pack(pady=20)

# Iniciar la interfaz gráfica
root.mainloop()
