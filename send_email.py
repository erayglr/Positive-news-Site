import smtplib
import os
import ssl
def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "erayguler5767@gmail.com"
    password = os.getenv("GMAIL_PASSWORD")

    receiver = "erayguler5767@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
