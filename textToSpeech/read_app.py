import os
from gtts import gTTS
import docx
import PyPDF2
from pydub import AudioSegment

language = 'en'

def read_app(fname):
    if '.txt' in fname:
        file_input = open(fname, "r")
        combined = AudioSegment.from_file("./static/start.mp3")

        #looping through file lines
        for input_line in file_input:
            #print(input_line)
            if input_line!='':
                myobj = gTTS(text=input_line, lang=language, slow=False)
                myobj.save("./static/audio.mp3") 
                audio = AudioSegment.from_file("./static/audio.mp3")
                combined+= audio
        
        combined.export("./static/final_audio.mp3", format='mp3')
        #os.system("mpg321 ./static/finish.mp3")
        try:
            os.remove('./static/audio.mp3')
        except:
            pass
        
        print("[Done]")


    elif '.docx' in fname:
        file_input = docx.Document(fname)
        combined = AudioSegment.from_file("./static/start.mp3")

        #looping through file lines
        for input_line in file_input.paragraphs:
            
            if input_line!='':
                #print(input_line.text)
                myobj = gTTS(text=input_line.text, lang=language, slow=False)
                myobj.save("./static/audio.mp3") 
                audio = AudioSegment.from_file("./static/audio.mp3")
                combined+= audio
        
        combined.export("./static/final_audio.mp3", format='mp3')
        #os.system("mpg321 ./static/finish.mp3")
        try:
            os.remove('./static/audio.mp3')
        except:
            pass
            
        print("[Done]")

    elif '.pdf' in fname:
        pdfFileObj = open(fname,'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pages = pdfReader.numPages
        combined = AudioSegment.from_file("./static/start.mp3")

        for i in range(pages):
            pageObj = pdfReader.getPage(i)

            # Extracting text from page
            # And splitting it into chunks of lines
            text = pageObj.extractText().split("  ")

            # Finally the lines are stored into list
            # For iterating over list a loop is used
            for i in range(len(text)):
                input_line = text[i]
                if input_line!='':
                    #print(input_line)
                    myobj = gTTS(text=input_line, lang=language, slow=False)
                    myobj.save("./static/audio.mp3") 
                    audio = AudioSegment.from_file("./static/audio.mp3")
                    combined+= audio

            # For Seprating the Pages   
            #print()
        
        combined.export("./static/final_audio.mp3", format='mp3')
        # os.system("mpg321 ./static/finish.mp3")
        try:
            os.remove('./static/audio.mp3')
        except:
            pass

        print("[Done]")

        # closing the pdf file object
        pdfFileObj.close()

    else:
        print("\nPlease enter a valid file name (including the extension '.txt' or '.docx' or '.pdf') that exist.")

if __name__ == '__main__':
    #read the file name
    fname = input("Enter Input File Name: ")
    read_app(fname)

   