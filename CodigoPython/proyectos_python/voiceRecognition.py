import speech_recognition as sr  

recognizer = sr.Recognizer()

mic = sr.Microphone()

with mic as source:

    audio = recognizer.listen(source)

text = recognizer.recognize_google(audio, language = 'Es')

print(f'Has dicho: {text}')