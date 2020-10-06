import os
from gtts import gTTS
import docx

language = 'en'

#read the file name
fname = input("Enter Input File Name: ")
flag = 0

if '.docx' in fname:
    file_input = docx.Document(fname)
    
    #looping through file lines
    for input_line in file_input.paragraphs:
        print(input_line.text)
        myobj = gTTS(text=input_line.text, lang=language, slow=False)
        myobj.save("voice.mp3") 
        os.system("mpg321 voice.mp3")
    
    try:
        os.remove('voice.mp3')
    except:
        pass
        
    print("[Done]")

elif '.txt' in fname:
    file_input = open(fname, "r")
    #looping through file lines

    for input_line in file_input:
        print(input_line)
        myobj = gTTS(text=input_line, lang=language, slow=False)
        myobj.save("voice.mp3") 
        os.system("mpg321 voice.mp3")
    
    try:
        os.remove('voice.mp3')
    except:
        pass
    
    print("[Done]")

else:
    print("\nPlease enter a valid file name (including the extension '.txt' or '.docx') that exist.")