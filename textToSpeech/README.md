## Getting started
### File System Description
- There are 2 python files ```text_to_speech_api.py``` & ```read_app.py``` and 2 HTML files for rendering the web view
- The ```text_to_speech_api.py``` file uses the flask as backend server which takes the user input files
-  The ```read_app.py``` contains the funtion which reads the input file from storage, and convert it into speech (line-by-line) and then finally returns the converted audio.

#### Requirements
Install the requirements before moving forward using  ```pip install -r requirements.txt```
There after use ```sudo apt install ffmpeg``` to install ffmpeg for merging audio.

### Run
- Simply run the ```text_to_speech_api.py``` file to start the server.
- Upload the file in the dashboard (currently accepting-> text,pdf,word)

### ouput/result
- You will get a speech-ouput in the newly rendered page.
<!-- - An output file named as ```output.txt``` will be formed and all the outputs are appended line-by-line -->


Regards: Himanshu Khairajani