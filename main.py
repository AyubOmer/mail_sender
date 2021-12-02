import smtplib, os
from email.message import EmailMessage

email = "din_mail@gmail.com"
password = input("passord: ")

def send_email(to, subject, msg):
    message = EmailMessage()
    message["From"] = email
    message["To"] = to
    message["Subject"] = subject
    message.set_content(msg)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    print(f"email: {email} password: {password}")
    server.login(email, password)
    server.send_message(message, email, to)
    server.quit()

send_email("til_epost", "Ha", "Hi")
