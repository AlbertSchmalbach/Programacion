import pyttsx3
import speech_recognition as sr
import webbrowser as wb

r = sr.Recognizer()
engine = pyttsx3.init()

def talk():
    mic = sr.Microphone()
    with mic as source:
        audio = r.listen(source)
    text = r.recognize_google(audio, lenguaje="es-ES")
    print(f'Has dicho: {text}')
    return text.lower()

if 'jw.org' in talk():
    engine.say("¿Que quieres buscar en JW.ORG?")
    engine.runAndWait()
    text = talk()
    wb.open(f'https://www.jw.org.es/s?k={text}')