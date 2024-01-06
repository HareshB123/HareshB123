print('working')
import speech_recognition
import pyttsx3
import webbrowser

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
            a=10
            print(f"rec: {text}")
            if qtext == True:
                        
                search_url = f"https://www.google.com/search?q={qtext}"
                webbrowser.open(search_url)
                    
    except speech_recognition.UnknownValueError:
        recognizer= speech_recognition.Recognizer()
    except:
        print("error")
        ask = input('do you want ot continue:')
        if ask == 'yes' or ask == 'Yes':
            print()
        else:
            break