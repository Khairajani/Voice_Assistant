# Voice Assistant
This is yet a simple Voice-Assistant System developed using python packages and Google's speech-recongition API. 

#### Requirements
Install the requirements before moving forward using  ```pip install -r requirements.txt```
There after use ```sudo apt install ffmpeg``` to install ffmpeg for merging audio

### 1) voice_assistant.py
It first listens to the voice inputs using microhpone, Converts audio into text format, extracts various keywords such as 'today's date', 'who is ...' etc. from the text and finally respond via speech output.

### Examples
1) Speech Input: "What is today's date" 
-> Text and Speech Ouput: "Today is Tuesday,  October the 6th ."

2) Speech Input: "Who is Ricky Pointing" 
-> Text and Speech Ouput: "Ricky Thomas Ponting  (born 19 December 1974) is an Australian cricket coach, commentator, and former cricketer. He is considered the most successful captain in international cricket history, with 220 victories in 324 matches with a winning ratio of 67.91%.
High Performance MPEG 1.0/2.0/2.5 Audio Player for Layer 1, 2, and 3."

3) Speech Input: "Exit" 
-> It prints "[Ending]" and stops the system.


### 2) app.py
- Simple voice-to-text and text-to-voice convertor script.
- Simply run the app.py using ```python app.py``` and used the servies.


