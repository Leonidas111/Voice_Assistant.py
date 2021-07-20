import speech_recognition as sr
import pyttsx3


name = "alexa"
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice",voices[2].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def funlisten(rec):
    with sr.Microphone() as source:
        voice = listener.listen(source)
        rec = listener.recognize_google(voice)
        if name in rec:
            talk("Estoy a sus ordenes mi Lord")
            print("listening...")
    with open ("./historysearchs.txt","a",encoding="utf-8") as history:
        history.write("\n")
        history.write(rec) 

def run():
    reproduce = lambda:funlisten("Reproduce")
    talk(reproduce)
    print("reproduciendo....")

if __name__=="__main__":
    run()
