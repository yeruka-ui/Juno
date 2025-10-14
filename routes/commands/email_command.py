from .command_helper import newJson
import smtplib
import os
from os import getenv


def send_email(command, confidence, content):

    #sender
    sender_email = getenv("GMAIL")
    sender_pass = getenv("GMAIL_PASS")

    #Receiver and message
    receiver = content['receiver']
    subject = content['subject']
    body = f"Subject: {subject}\n\n{content['body']}"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(sender_email, sender_pass)
        server.sendmail(sender_email, receiver, body)
        msg = f"Email sent to {receiver} successfully."
        return newJson(command, confidence, msg)
    except smtplib.SMTPException:
        msg = f"Email was not sent. {smtplib.SMTPException}"
        return newJson(command, confidence, msg)