# Import packages
import speech_recognition as sr
import os
from gtts import gTTS

# Initialize the speech recognizer with language
r = sr.Recognizer()
language = 'en'

# lang_dict ={1:'en',2:'hi'}
# n = int(input("Enter the language you want to talk:\n1: English\n2: Hindi\n"))
# lang = lang_dict[n-1]

while True:
    print("Choose from below option:\n1) Voice-to-text\n2) Text-to-voice\n3) Exit")
    n = int(input())
    try:
        if n==1:
            with sr.Microphone() as source:
                print("Speak Anything :")
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                    mytext=text.lower()
                    print("You said : {}".format(text))
                    
                    # Exit keyword
                    if mytext=='exit' or mytext=='shutdown':
                        print("[Ending..]")
                        break

                except sr.UnknownValueError:
                    print("Sorry could not recognize what you said")

                except sr.RequestError as e :
                    print('Request results from google speechrecognition service error' +e)

        elif n==2:
                s = input("Type Anything :")

                if s=='exit' or s=='shutdown':
                    print("[Ending..]")
                    break
                
                myobj = gTTS(text=s, lang=language, slow=False)
                myobj.save("voice.mp3") 
                os.system("mpg321 voice.mp3")
                os.remove('voice.mp3')
                #print("You said : {}".format(mytext))

        elif n==3:
            print("[Ending..]")
            break

        else:
            print("Please Enter a valid input")
    
    except Exception as e:
        print(e)
        exit()