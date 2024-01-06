print('working')
import speech_recognition
import pyttsx3
recognizer= speech_recognition.Recognizer()

while True:
    try:
            with speech_recognition.Microphone() as source:
                print("started")
                recognizer.adjust_for_ambient_noise(source, duration=0.10)
                print("ready")
                audio = recognizer.listen(source)
                print("listening")
                text = recognizer.recognize_google(audio)
                print("converting")
                qtext = text.lower()
                print(f"rec: {qtext}")
    except speech_recognition.UnknownValueError:
            recognizer= speech_recognition.Recognizer()
    except:
            print("error")
            ask = input('do you want ot continue:')
            if ask == 'yes' or ask == 'Yes':
                print()
            else:
                break
ass="heelefsghsjk"