import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

name = "alexa"
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice",voices[2].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice)
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, "")
                print(rec)
    except:
        pass
    return rec

def run():
    rec = listen()
    if "reproduce" in rec:
        music = rec.replace("reproduce"," ")
        talk("reproduciendo" + rec)
        pywhatkit.playonyt(music)
    if "hora" in rec:
        hora = datetime.datetime().now().strftime("%I:%M %p")
        talk("son las" + hora)
    elif "busca" in rec:
        order = rec.replace("busca","")
        info = wikipedia.summary(order,1)
        talk(info)
run()
