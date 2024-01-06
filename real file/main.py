from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
 

from mic import Ui_SubWindow

class Ui_MainWindow(object):
    def openwindow2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SubWindow()
        self.ui.setupUi(self.window)
        self.window.show()
   
    def openwindow1(self):
        
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

                        takeCommand()
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
                MainWindow.setObjectName("home")
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
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        import image_rc


        if __name__ == "__main__":
            import sys
            app = QtWidgets.QApplication(sys.argv)
            MainWindow = QtWidgets.QMainWindow()
            ui = Ui_SubWindow()
            ui.setupUi(MainWindow)
            MainWindow.show()
            sys.exit(app.exec_())



# create pyqt5 app


# start the app


    def openwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SubWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1059, 585)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(210, 10, 841, 531))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(0, 0, 831, 531))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 171, 121))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.connect(self.openwindow2)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 280, 171, 121))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.clicked.connect(self.openwindow)

        self.pushButton_3.setGeometry(QtCore.QRect(20, 150, 171, 121))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.clicked.connect(self.openwindow1)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 410, 171, 121))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.openwindow1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1059, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "webengine"))
        self.pushButton_4.setText(_translate("MainWindow", "calculator"))
        self.pushButton_3.setText(_translate("MainWindow", "voicemode"))
        self.pushButton_5.setText(_translate("MainWindow", "games"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QApplication.setApplicationName("Gnet")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
  
    MainWindow.show()
    sys.exit(app.exec_())

