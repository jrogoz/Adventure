import speech_recognition as sr
import pyttsx3
import pyaudio
# import engineio

def synthesis(text):

    engineio = pyttsx3.init()

    voices = engineio.getProperty('voices')
    engineio.setProperty('rate', 130)
    engineio.setProperty('voice', voices[1].id)  # 0 - polski, 1 - angielski

    sentence = text

    # print(sentence)
    engineio.say(sentence)
    engineio.runAndWait()

def recognition():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Speak command: ')
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            return text
        except:
            return 'Couldn\'t recognized'
