import tkinter as tk
from tkinter import messagebox
from twilio.rest import Client

# Twilio Credentials (replace with your own)
account_sid = 'PN82b3d5a7e84d0b46ca59699cc3b266a4'
auth_token = 'your_auth_token'
twilio_number = 'whatsapp:+your_twilio_number'

# Initialize Twilio Client
client = Client(account_sid, auth_token)

# Function to send WhatsApp message
def send_reminder():
    phone_number = phone_entry.get()
    message_text = message_entry.get()

    if phone_number and message_text:
        try:
            message = client.messages.create(
                body=message_text,
                from_=twilio_number,
                to=f'whatsapp:{phone_number}'
            )
            messagebox.showinfo("Success", "Reminder sent successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send message: {e}")
    else:
        messagebox.showerror("Error", "Please enter both phone number and message.")

# Create the main application window
root = tk.Tk()
root.title("WhatsApp Reminder Bot")
root.geometry("400x300")
root.config(bg='black')

# Style settings
label_font = ("Arial", 12)
entry_font = ("Arial", 10)

# Phone number label and entry
phone_label = tk.Label(root, text="Phone Number (WhatsApp):", bg='black', fg='white', font=label_font)
phone_label.pack(pady=10)
phone_entry = tk.Entry(root, font=entry_font, width=30)
phone_entry.pack()

# Message label and entry
message_label = tk.Label(root, text="Message:", bg='black', fg='white', font=label_font)
message_label.pack(pady=10)
message_entry = tk.Entry(root, font=entry_font, width=30)
message_entry.pack()

# Send Button
send_button = tk.Button(root, text="Send Reminder", command=send_reminder, bg='white', fg='black', font=label_font)
send_button.pack(pady=20)

# Run the application
root.mainloop()
