# Importing Libraries
import os
import smtplib
from email.message import EmailMessage
import speech_recognition as sr
from gtts import gTTS
import time
from pydub import AudioSegment

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

def mail_app(subject_path,body_path):

    # Speech-to-Text
    # SUBJECT of the text
    print("\nTaking the subject voice inputs...")
    with sr.AudioFile(subject_path) as source:
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

    # BODY of the text
    print("\nTaking the body voice inputs...")

    with sr.AudioFile(body_path) as source:
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        text_body=text.lower()
        print("Body recorded successfully\n")
        #print("You said : {}".format(text_subject))

    except sr.UnknownValueError:
        print("Sorry could not recognize what you said")

    except sr.RequestError as e :
        print('Request results from google speechrecognition service error' +e)

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

    del msg['From'] 
    del msg['To'] 
    del msg['Subject'] 

if __name__ == '__main__':
    #read the file name
    
    subject_path = "./upload/subject.wav"
    body_path = "./upload/body.wav"

    if os.path.isfile(subject_path) and os.path.isfile(body_path):
        mail_app(subject_path,body_path)
    
    else:
        print("files doesn't exist")

    # audio = AudioSegment.from_wav(body_path)
    # audio.export(body_dst, format="mp3")
    # audio = AudioSegment.from_mp3(body_dst)