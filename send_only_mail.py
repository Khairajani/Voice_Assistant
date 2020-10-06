# Importing Libraries
import os
import smtplib
from email.message import EmailMessage

# Initilization of variables
msg = EmailMessage()
SENDER_EMAIL_ADDRESS = os.environ.get('Email_User')
SENDER_EMAIL_PASSWORD = os.environ.get('Email_Pass')
RECEIVER_EMAIL_ADDRESS = SENDER_EMAIL_ADDRESS
port =  465 # 587  # For starttls
smtp_server = "smtp.gmail.com"


# Speech-to-Text
text_subject = "Test"
text_body = "Its working, kudos!"


# Setting mail for sending
msg['From'] = SENDER_EMAIL_ADDRESS
msg['To'] = RECEIVER_EMAIL_ADDRESS
msg['Subject'] = text_subject
msg.set_content(text_body)

# Sending mail
with smtplib.SMTP_SSL(smtp_server, port) as smtp:
    # smtp.ehlo()
    # smtp.starttls()
    # smtp.ehlo()

    smtp.login(SENDER_EMAIL_ADDRESS, SENDER_EMAIL_PASSWORD)
    smtp.send_message(msg)