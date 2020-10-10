## Getting started
### File System Description
- There are 2 python files ```speech_to_text_api.py``` & ```mail_app.py``` and 1 HTML file for rendering the web view
- The ```speech_to_text_api.py``` file uses the flask as backend server which takes the user inputs: recorded audio, and receiver's email id.
-  The ```mail_app.py``` contains the funtion which reads the input recording from storage (both subject and body of the mail), and convert it into text and then finally mail the respective receiver.

#### Requirements
Install the requirements before moving forward using  ```pip install -r requirements.txt```
There after use ```sudo apt install ffmpeg``` to install ffmpeg for merging audio.

### Run
- Simply run the ```speech_to_text_api.py``` file to start the server.
- Record the subject and body in the dashboard, and finally upload them.
- Enter Recipient email id (currently only 1)
- Click SEND MAIL

### ouput/result
- You will get a response output, and the recipient would definitely receive the mail.
<!-- - An output file named as ```output.txt``` will be formed and all the outputs are appended line-by-line -->


Regards: Himanshu Khairajani