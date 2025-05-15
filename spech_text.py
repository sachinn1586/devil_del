import pyttsx3
import os
start = pyttsx3.init()
start.say("Hello World Sachin Kumar what the fuck")
start.runAndWait()


import os
directory = '/Applications'
content = os.listdir(directory)
for i in content:
    print(i)
