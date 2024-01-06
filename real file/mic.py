


from PyQt5 import QtCore, QtGui, QtWidgets
def run():
    import pyttsx3

    import speech_recognition as sr

    import datetime

    import wikipedia

    import webbrowser

    import os

    


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
            speak("Recognizing...")
            query = r.recognize_google(audio, language='en-in')

            print(f"User said: {query}\n")


        except Exception as e:

            # print(e)    

            speak("Say that again please...")  

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
                #pyautogui.hotkey('ctrl', 'w')


            elif 'open youtube' in query:

                webbrowser.open("youtube.com")
                speak('opening youtube')
                #pyautogui.hotkey('ctrl', 'w')

            elif 'open google' in query:

                webbrowser.open("google.com")
                speak('opening google')
              
            elif 'find' in query:

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
            elif 'open stackoverflow' in query:

                webbrowser.open("stackoverflow.com") 
            
            



            # elif 'play music' in query:

            #     '''music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'

            #     songs = os.listdir(music_dir)

            #     print(songs)    

            #     os.startfile(os.path.join(music_dir, songs[0]))'''


            elif 'the time' in query:

                strTime = datetime.datetime.now().strftime("%H:%M:%S")    

                speak(f"mam, the time is {strTime}")


class Ui_SubWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(313, 210)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: run())
        self.pushButton.setGeometry(QtCore.QRect(100, 20, 121, 121))
        self.pushButton.setStyleSheet("image:url(:/menubutton/mic-4.png)")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 313, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "voice_mode"))
import image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_SubWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
