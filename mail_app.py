# Importing Libraries
import os
import smtplib
from email.message import EmailMessage
import speech_recognition as sr
from gtts import gTTS
import time

# Initialize the speech recognizer with language
r = sr.Recognizer()
language = 'en'

# Initilization of variables
msg = EmailMessage()
SENDER_EMAIL_ADDRESS = os.environ.get('Email_User')
SENDER_EMAIL_PASSWORD = os.environ.get('Email_Pass')
RECEIVER_EMAIL_ADDRESS = SENDER_EMAIL_ADDRESS
port =  465 # 587  # For starttls
smtp_server = "smtp.gmail.com"
text_subject = ""
text_body = ""

flag = 2
while flag == 2:

    # Speech-to-Text
    with sr.Microphone() as source:

        print("\nTaking voice inputs...")
        # Enter SUBJECT of the mail
        print("\nEnter the subject, using voice :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            text_subject=text.lower()
            print("Subject recorded successfully\n")
            #print("You said : {}".format(text_subject))

        except sr.UnknownValueError:
            print("Sorry could not recognize what you said")

        except sr.RequestError as e :
            print('Request results from google speechrecognition service error' +e)

    time.sleep(1)

    with sr.Microphone() as source:
        # Enter BODY of the mail
        print("\nEnter the body, using voice :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            text_body=text.lower()
            print("Body recorded successfully\n")
            #print("You said : {}".format(text_body))

        except sr.UnknownValueError:
            print("Sorry could not recognize what you said")

        except sr.RequestError as e :
            print('Request results from google speechrecognition service error' +e)

    print("\nSelect from the below options:\n1) Send\n2) Re-enter the voice data.")
    flag = int(input("Enter 1 or 2, from the above choice: "))

# Setting mail for sending
msg['From'] = SENDER_EMAIL_ADDRESS
msg['To'] = RECEIVER_EMAIL_ADDRESS
msg['Subject'] = text_subject
msg.set_content(text_body)

# Sending mail
print("\nSending mail...")
with smtplib.SMTP_SSL(smtp_server, port) as smtp:
    # smtp.ehlo()
    # smtp.starttls()
    # smtp.ehlo()
    smtp.login(SENDER_EMAIL_ADDRESS, SENDER_EMAIL_PASSWORD)
    smtp.send_message(msg)

print("[SENT]")