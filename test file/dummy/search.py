import pyttsx3

import speech_recognition as sr

import webbrowser

import os

import smtplib

def takeCommand():

        while True:
            r1 = sr.Recognizer()

            with sr.Microphone() as source:

                print("Listening...")

                r1.pause_threshold = 1

                audio = r1.listen(source)


            try:

                print("Recognizing...")    

                query1 = r1.recognize_google(audio, language='en-in')

                print(f"User said: {query1}\n")


            except Exception as e:

                # print(e)    

                speak("Say that again please...")  

                return "None"

            #return query
            search_url = f"https://www.google.com/search?q={query1}"
            webbrowser.open(search_url)

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

        # print(voices[1].id)

engine.setProperty('voice', voices[0].id)



def speak(audio):

            engine.say(audio)

            engine.runAndWait()

    # def search(query):
    #     print('gg')
    #     search_url = f"https://www.google.com/search?q={query}"
    #     webbrowser.open(search_url)
    # takeCommand()
takeCommand()