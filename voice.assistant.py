import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice",voices[2].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
try:
    with sr.Microphone() as source:
        talk("Estoy a sus ordenes mi Lord;lo escucho atentamente")
        print("Listening ...")
        voice = listener.listen(source)
        rec = listener.recognize_google(voice)
        talk(rec)
    with open ("./historysearchs.txt","a",encoding="utf-8") as history:
        history.write("\n")
        history.write(rec)
except:
    pass