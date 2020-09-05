import pyttsx3
import speech_recognition as sr
import os
import wikipedia
import datetime
import webbrowser
import smtplib
import bs4
import sys
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from random import randrange
engine =pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")    
    speak("I am jarvis sir. Please tell me how may I help you")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")    
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail','yourpassword')
    server.sendmail('youremail',to,content)
    server.close()

if __name__=="__main__":
    wishMe()
    if 1:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching Wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow")

        elif 'play music' in query:
            music_dir='E:\music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[randrange(3)]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
        elif 'play game' in query:
            codePath="Game File Path"
            os.startfile(codePath)   
        elif 'email to verma' in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to="Receivers email"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Shivesh Sir, I am not able to send this mail")