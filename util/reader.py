import pyttsx3
import os
import re


os.chdir("C:\\Users\\location to output.txt")

engine = pyttsx3.init()

voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)

rate = engine.getProperty('rate')
engine.setProperty('rate', 125)

count = 0
start = 412
# pdf page = 25
with open("output.txt", 'rb') as fp:
    strList = fp.readlines()
    decodedList = [ line.decode("utf-8").strip() for line in strList ]
    bigString = " ".join(decodedList)
    sentenceSplit = re.split("\. |\? |\! ", bigString)

    for line in sentenceSplit:
        count+=1
        if count >= start:
            engine.say(line.strip())
            engine.runAndWait()
            print(count)


