import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia


name = "sirvienta"
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice",voices[2].id)
engine. setProperty('rate', 178)
engine.setProperty('volume', 0.7)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def funlisten(rec):
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-ES')
            if name in rec:
                talk("Estoy a sus ordenes mi Lord")
                print("Escuhando...")
                rec = rec.replace(name, '')
            else:
                talk("Solo atiendo al llamado por mi nombre")
        with open ("./historysearchs.txt","a",encoding="utf-8") as history:
            history.write("\n")
            history.write(rec)
    except:
        pass 
def run():
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')
        talk('Reproduciendo ' + music)
        pywhatkit.playonyt(music)
    elif 'hora' in rec:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        talk("Son las " + hora)
    elif 'busca' in rec:
        order = rec.replace('busca', '')
        wikipedia.set_lang("es")
        info = wikipedia.summary(order, 1)
        talk(info)
run()