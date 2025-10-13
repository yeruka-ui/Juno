import pywhatkit as kit
import os
from .command_helper import newJson

def get_email(command, confidence, user_args):
    try:
        sender_email = os.getenv("EMAIL_USER") 
        sender_pass = os.getenv("EMAIL_PASS")  

        receiver_email = user_args.get("to")
        subject = user_args.get("subject", "No Subject")
        message = user_args.get("message", "")

        if not all([receiver_email, subject, message]):
            return newJson(command, confidence, "Missing recipient, subject, or message fields.")

        kit.send_mail(sender_email, sender_pass, subject, message, receiver_email)
        return newJson(command, confidence, f"Email sent successfully to {receiver_email}!")

    except Exception as e:
        return newJson(command, confidence, f"Failed to send email: {e}")
