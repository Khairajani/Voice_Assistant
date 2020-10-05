# Import packages
import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia

warnings.filterwarnings('ignore')

r = sr.Recognizer()
flag = 0
language = 'en'

# lang_dict ={1:'en',2:'hi'}
# n = int(input("Enter the language you want to talk:\n1: English\n2: Hindi\n"))
# lang = lang_dict[n-1]

#A functions to get persons name from text
def getPerson(text):

    wordList = text.split() #splits the text to words

    for i in range(0, len(wordList)):
        if i+3 <= len(wordList)-1 and wordList[i].lower() == 'who' and wordList[i+1].lower() == 'is':
            return wordList[i+2] + ' '+ wordList[i+3]

# Date function
def getDate():

    now  = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()] #sunday
    monthNum = now.month
    dayNum = now.day

    #A list of months
    month_names = ['January', 'February', 'March', ' April', 'May', 'June', 'July','August', 'September', ' October', 'November', 'December']

    #A list of ordinal Numbers
    ordinalNumbers = [ '1st', '2nd', '3rd', ' 4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th',
    '17th', '18th', '19th', '20th', '21st', '22nd', '23rd','24rd', '25th', '26th', '27th', '28th', '29th', '30th', '31st']

    return 'Today is '+weekday+', '+month_names[monthNum - 1]+' the '+ ordinalNumbers[dayNum -1]+' .'


while True:

    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            mytext=text.lower()
            print("You said : {}".format(text))
            
            # Exit keyword
            if mytext=='exit' or mytext=='chup' or mytext=='shutdown' or mytext=='nikal':
                print("[Ending..]")
                break

            # Today's Date
            if "today's date" in mytext or "aaj ki tarikh" in mytext:
                #print("Todays date")    
                get_date = getDate()
                mytext = get_date

            #check to see if the user said 'who is' 
            elif 'who is' in mytext:
                person = getPerson(text) 
                wiki = wikipedia.summary(person, sentences=2)
                mytext = wiki

        except sr.UnknownValueError:
            flag+=1
            print("Sorry could not recognize what you said")

        except sr.RequestError as e :
            print('Request results from google speechrecognition service error' +e)
            break       

    if flag ==2:
        print("[Ending..]")
        break

    elif flag!=0:
        continue

    else:
        print("Reply:", mytext)
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("voice.mp3") 
        os.system("mpg321 voice.mp3") 	 
        #print("You said : {}".format(mytext))
