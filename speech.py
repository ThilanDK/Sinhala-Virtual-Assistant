import speech_recognition as sr
from selenium import webdriver
from googletrans import Translator
from googlesearch import search
import re
import subprocess
import time
import pyaudio

found=False
import os
translator = Translator()
r=sr.Recognizer()

try:
    with sr.Microphone() as source:
        print("say something")
        audio = r.listen(source)
        print("Time over, Thanks")
    #name=r.recognize_google(audio,language="si")
    name = r.recognize_google(audio, language="si")
    print("Text: %s" % name)
    siri=translator.translate(name, dest='en').text
    mystr = siri.lower()
    wordList = re.sub("[^\w]", " ", mystr).split()
    print(wordList)
    if('open' in wordList):
        #wordList.remove('open')
        print(wordList)
        for i in range(len(wordList)):
            print("found")
            if(os.path.exists("C:\Program Files (x86)\R.G. Mechanics\Blur\Blur.exe" )):
                print("und")
                #subprocess.Popen(r"C:\Program Files (x86)\R.G. Mechanics\Blur\Blur.exe",shell=True)
                os.popen("G:/New folder (4)/Call of duty 4 Multiplayer/ iw3mp.exe")
                found=True
            else:
                i=i+1
        if(found==False):
            print("sorry your app not found")

        print("ss")

    else:
        for j in search(siri, tld="com", num=10, stop=1, pause=2):
            driver = webdriver.Firefox()
            driver.get(j)
            print(j)
except Exception as e:
    print(e)