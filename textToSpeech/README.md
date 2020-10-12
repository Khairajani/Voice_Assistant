## Getting started
### File System Description
- There are 2 python files ```text_to_speech_api.py``` & ```read_app.py``` and 2 HTML files (in one of the folders above) for rendering the web view
- The ```text_to_speech_api.py``` file uses the flask as backend server which takes the user input files in the dashboard
-  The ```read_app.py``` contains the funtion which reads the input file from storage, and convert it into speech (line-by-line) and then finally returns the converted audio.

#### Requirements
Install the requirements before moving forward using  ```pip install -r requirements.txt```
There after use ```sudo apt install ffmpeg``` to install ffmpeg for merging audio.

### Run
- Simply run the ```text_to_speech_api.py``` file to start the server.
- To Open the dashboard (HTML rendering), goto the localhost IP address, which can be found in terminal as well.
- Upload the file in the dashboard (currently accepting-> text,pdf,word)
- Click the SUBMIT button.

### ouput/result
- You will get a speech-ouput in the newly rendered page.
- You can also download the converted audio using the ```save to disk``` URL.
<!-- - An output file named as ```output.txt``` will be formed and all the outputs are appended line-by-line -->


Regards: Himanshu Khairajani