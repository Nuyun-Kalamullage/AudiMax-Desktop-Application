import speech_recognition as sr
import pyttsx3
from beep import play


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


#
def TextToSpeak(Text):
    # if engine.inLoop:
    #     engine.endLoop()
    engine.say(Text)
    engine.runAndWait()


def welcomeSpeak():
    engine.say("Hello there you are in assisted mode")
    engine.say("for Instructions you can say \"Help me\" command!")
    engine.runAndWait()


def get_audio(wait_seconds):
    rObject = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        rObject.adjust_for_ambient_noise(source)
        play()
        audio = rObject.listen(source, phrase_time_limit=wait_seconds)

    try:
        text = rObject.recognize_google(audio, language='en-US')
        print("You : ", text)
        return text
    except Exception as e:
        TextToSpeak("Could not understand your audio, PLease try again !")
        return "all"
