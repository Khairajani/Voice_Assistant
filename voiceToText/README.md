## Getting started
### File System Description
- There are 2 python files ```speech_to_text_api.py``` & ```mail_app.py``` and 1 HTML file (in one of the folders above) for rendering the web view
- The ```speech_to_text_api.py``` file uses the flask as backend server which takes the user inputs(in the dashboard): recorded audio, and receiver's email id.
- The ```mail_app.py``` contains the funtion which reads the input recording (After clicking of the submit button) from storage (both subject and body of the mail), and convert it into text and then finally send the mail to respective receiver.

#### Requirements
Install the requirements before moving forward using  ```pip install -r requirements.txt```
There after use ```sudo apt install ffmpeg``` to install ffmpeg for merging audio.
- Before moving forward run ```. ./cred.sh``` so that the environment variable is having with sender Email-ID and Password. 

### Run
- Simply run the ```speech_to_text_api.py``` file to start the server.
- To Open the dashboard (HTML rendering), goto the localhost IP address, which can be found in terminal as well.
- Record the subject and body of the mail in the dashboard, and finally upload both of them.
- Enter Recipient email id (currently accepting only 1)
- Click the SEND MAIL button

### ouput/result
- If anything is missing, like subject or body recording, you will get the response output as FILE MISSING or  FAILED. 
- Else, you will get a response output of SUCCESS i.e. MAIL SENT, and the recipient would receive the mail.
<!-- - An output file named as ```output.txt``` will be formed andll the outputs are appended line-by-line -->


Regards: Himanshu Khairajani