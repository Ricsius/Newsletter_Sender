import smtplib
import ssl
import os

def send(message):
    host = "smtp.gmail.com"
    port = 465

    username = os.getenv("MY_MAIL")
    password = os.getenv("PEMAIL_PASSWORD")

    reciver = os.getenv("MY_MAIL")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciver, message)