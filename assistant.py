import speech_recognition as sr
import pyttsx3
from playsound import playsound

OUTPUT_DIR = "D:\PycharmProjects\Voice_Application\\res\sounds\\beep.mp3"
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


#
def TextToSpeak(Text):
    if engine.inLoop:
        engine.endLoop()
    engine.say(Text)
    engine.runAndWait()


def MediaPlayerToSpeak(Text):
    #   pyttsx3.speak(Text)
        if engine.inLoop:
            engine.endLoop()
        engine.say(Text)
        engine.runAndWait()


def welcomeSpeak():
    engine.say("Hello there you are in assisted mode")
    engine.say("for Instructions you can say \"Help\" command!")
    engine.runAndWait()


def get_audio(wait_seconds):
    rObject = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        rObject.adjust_for_ambient_noise(source)
        playsound(OUTPUT_DIR)
        # recording the audio using speech recognition
        audio = rObject.listen(source, phrase_time_limit=wait_seconds)

    try:
        # keyword = ['search for','exit','1','2','3','4','5','text book','Oliver Twist']
        text = rObject.recognize_google(audio, language='en-US')
        # text1 = rObject.recognize_sphinx(audio, language='en-US',keyword_entries=keyword)
        print("You : ", text)
        return text
    except:
        TextToSpeak("Could not understand your audio, PLease try again !")
        return "all"
