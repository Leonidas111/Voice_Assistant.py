import speech_recognition as sr
import pyttsx3

name = "benjamin"
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice",voices[2].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
try:
    with sr.Microphone() as source:
        voice = listener.listen(source)
        rec = listener.recognize_google(voice)
        rec = rec.lower()
        if name in rec:
            talk("Estoy a sus ordenes mi Lord")
            talk(rec)
    #Guarda en historysearchs.txt:
    with open ("./historysearchs.txt","a",encoding="utf-8") as history:
        history.write("\n")
        history.write(rec)
except:
    pass