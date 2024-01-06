

#import smtplib


def run():
    import pyttsx3

    import speech_recognition as sr

    import datetime

    import wikipedia

    import webbrowser

    import os

    import smtplib


    engine = pyttsx3.init('sapi5')

    voices = engine.getProperty('voices')

    # print(voices[1].id)

    engine.setProperty('voice', voices[0].id)



    def speak(audio):

        engine.say(audio)

        engine.runAndWait()



    def wishMe():

        hour = int(datetime.datetime.now().hour)

        if hour>=0 and hour<12:

            speak("Good Morning!")


        elif hour>=12 and hour<18:

            speak("Good Afternoon!")  


        else:

            speak("Good Evening!")  


        speak("Please tell me how may I help you")      


    def takeCommand():


        r = sr.Recognizer()

        with sr.Microphone() as source:

            print("Listening...")

            r.pause_threshold = 1

            audio = r.listen(source)


        try:

            print("Recognizing...")    

            query = r.recognize_google(audio, language='en-in')

            print(f"User said: {query}\n")


        except Exception as e:

            # print(e)    

            print("Say that again please...")  

            return "None"

        return query


    '''def sendEmail(to, content):

        server = smtplib.SMTP('smtp.gmail.com', 587)

        server.ehlo()

        server.starttls()

        server.login('youremail@gmail.com', 'your-password')

        server.sendmail('youremail@gmail.com', to, content)

        server.close()'''


    def add(x, y):

        results=x+y

        print(results)

        speak(results)


    if __name__ == "__main__":

        wishMe()

        while True:

        # if 1:

            query = takeCommand().lower()


            # Logic for executing tasks based on query

            if 'wikipedia' in query:

                speak('Searching Wikipedia...')

                query = query.replace("wikipedia", "")

                results = wikipedia.summary(query, sentences=2)

                speak("According to Wikipedia")

                print(results)

                speak(results)


            elif 'open youtube' in query:

                webbrowser.open("youtube.com")


            elif 'open google'  in query or 'open chrome':

                webbrowser.open("google.com")
            elif 'website' in query:
                speak('start to say the website')
                rs = sr.Recognizer()
                with sr.Microphone() as source:

                    print("Listening...")

                    rs.pause_threshold = 1

                    audio = rs.listen(source)


                try:

                    print("Recognizing...")    
                    speak('Recognizing...')
                    query1 = rs.recognize_google(audio, language='en-in')

                    if query == True:
                        
                        search_url = f"https://www.google.com/search?q={query1}"
                        webbrowser.open(search_url)
                    
                except Exception as e:

                    # print(e)    

                    speak("Say that again please...")  

                    return "None"

            # elif 'open chrome' in query:

            #     webbrowser.open("google.com")
            # # elif 'open stackoverflow' in query:

            #     webbrowser.open("stackoverflow.com")  



            elif 'play music' in query:

                '''music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'

                songs = os.listdir(music_dir)

                print(songs)    

                os.startfile(os.path.join(music_dir, songs[0]))'''


            elif 'the time' in query:

                strTime = datetime.datetime.now().strftime("%H:%M:%S")    

                speak(f"mam, the time is {strTime}")


            '''elif 'email to halima' in query:

                try:

                    speak("What should I say?")

                    content = takeCommand()

                    to = "yourEmail@gmail.com"    

                    sendEmail(to, content)

                    speak("Email has been sent!")

                except Exception as e:

                    print(e)

                    speak("Sorry my friend . I am not able to send this email")

            elif "add" in query:

                x=int(input("x : "))

                y=int(input("y : "))

                add(x, y)'''
run()
