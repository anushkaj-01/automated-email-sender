import os
from email.message import EmailMessage as Emailmsg
import ssl
import smtplib
import csv
import tkinter as tk
from tkinter import filedialog

def send_emails():
    email_sender = sender_entry.get()
    email_password = password_entry.get()
    subject = subject_entry.get()
    body = body_entry.get('1.0', tk.END)

    with open(csv_file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            text = f'Congratulations {line[1]}, you are selected.'
            email_receiver = line[0]

            em = Emailmsg()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['Subject'] = subject
            em.set_content(text)
            #em.add_alternative(body, subtype='html')

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())

def select_csv_file():
    global csv_file_path
    csv_file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    csv_file_label.config(text=csv_file_path)
root = tk.Tk()
root.title("Email Sender")
sender_label = tk.Label(root, text="Sender Email:")
sender_label.pack()
sender_entry = tk.Entry(root)
sender_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

subject_label = tk.Label(root, text="Subject:")
subject_label.pack()
subject_entry = tk.Entry(root)
subject_entry.pack()

body_label = tk.Label(root, text="Body:")
body_label.pack()
body_entry = tk.Text(root, height=5, width=30)
body_entry.pack()

csv_file_label = tk.Label(root, text="Select CSV File:")
csv_file_label.pack()
csv_file_button = tk.Button(root, text="Browse", command=select_csv_file)
csv_file_button.pack()

send_button = tk.Button(root, text="Send Emails", command=send_emails)
send_button.pack()

root.mainloop()
