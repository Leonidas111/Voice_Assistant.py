import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

engine.say("Buen dia Jefe")
engine.runAndWait()
try:
    with sr.Microphone() as source:
        print("Listening ...")
        voice = listener.listen(source)
        rec = listener.recognize_google(voice)
        print(rec)
    with open ("./historysearchs.txt","a",encoding="utf-8") as history:
        history.write("\n")
        history.write(rec)
except:
    pass