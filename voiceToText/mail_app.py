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


port =  465 # 587  # For starttls
smtp_server = "smtp.gmail.com"
text_subject = ""
text_body = ""
result = ""

def mail_app(subject_path,body_path,mailId):

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
        result = "Sorry could not recognize what you said"
        print("Sorry could not recognize what you said")
        return result

    except sr.RequestError as e :
        result = 'Request results from google speechrecognition service error' +e
        print('Request results from google speechrecognition service error' +e)
        return result

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
        result = "Sorry could not recognize what you said"
        print("Sorry could not recognize what you said")
        return result

    except sr.RequestError as e :
        result = 'Request results from google speechrecognition service error' +e
        print('Request results from google speechrecognition service error' +e)
        return result

    # Setting mail for sending
    RECEIVER_EMAIL_ADDRESS = mailId
    msg['From'] = SENDER_EMAIL_ADDRESS
    msg['To'] = RECEIVER_EMAIL_ADDRESS
    msg['Subject'] = text_subject
    msg.set_content(text_body)

    # Sending mail
    print("\nSending mail...")
    try:
        with smtplib.SMTP_SSL(smtp_server, port) as smtp:
            # smtp.ehlo()
            # smtp.starttls()
            # smtp.ehlo()
            smtp.login(SENDER_EMAIL_ADDRESS, SENDER_EMAIL_PASSWORD)
            smtp.send_message(msg)
            print("Mail Sent")
            result = "Mail Sent"

    except Exception as e:
        result = e
        print(e)
        return result
    
    del msg['From'] 
    del msg['To'] 
    del msg['Subject']  
    return result 

if __name__ == '__main__':
    #read the file name
    
    subject_path = "./upload/subject.wav"
    body_path = "./upload/body.wav"
    mailId = SENDER_EMAIL_ADDRESS

    if os.path.isfile(subject_path) and os.path.isfile(body_path):
        mail_app(subject_path,body_path,mailId)
    
    else:
        print("files doesn't exist")

    # audio = AudioSegment.from_wav(body_path)
    # audio.export(body_dst, format="mp3")
    # audio = AudioSegment.from_mp3(body_dst)