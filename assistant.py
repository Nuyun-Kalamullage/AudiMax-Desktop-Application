from time import sleep

import speech_recognition as sr
import requests
import keyboard
import pyttsx3
import json
import vlc

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


#
def TextToSpeak(Text):
    engine.say(Text)
    engine.runAndWait()


def welcomeSpeak():
    engine.say("Hello there you are in assisted mode")
    engine.say("Instructions")
    engine.runAndWait()


def get_audio(wait_seconds):
    rObject = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        rObject.adjust_for_ambient_noise(source)
        print("Speak...")
        TextToSpeak("Beeeep")
        # recording the audio using speech recognition
        audio = rObject.listen(source, phrase_time_limit=wait_seconds)
    print("Stop.")  # limit secs you pass

    try:
        # keyword = ['search for','exit','1','2','3','4','5','text book','Oliver Twist']
        text = rObject.recognize_google(audio, language='en-US')
        # text1 = rObject.recognize_sphinx(audio, language='en-US',keyword_entries=keyword)
        print("You : ", text)
        return text

    except:
        TextToSpeak("Could not understand your audio, PLease try again !")
        return "all"


def assistant():
    global p
    back = False
    welcomeSpeak()
    while True:
        TextToSpeak("Tell the command after Beep Sound")
        command = get_audio(5)
        if command.__contains__("search for"):
            while True:
                TextToSpeak("Please Tell me the book name after Beep Sound")
                bookName = get_audio(8)
                parameters = {
                    "query": bookName
                }
                response = requests.get("http://35.200.151.7/v1/books/", params=parameters)
                dataset = json.loads(response.text)['books']
                print(type(dataset))
                if len(dataset) > 0:
                    break
                else:
                    TextToSpeak("No matches Found!")

            i = 1
            for tempBook in dataset:
                title = tempBook['title']
                print(str(i) + ". Book Name is " + title)
                TextToSpeak(str(i) + ". Book Name is " + title)
                i = i + 1
            TextToSpeak("Please Select your Audio Book Number in key board")
            value = 9
            digit = range(0, 9)
            while not (value in digit):
                value = int(keyboard.read_key())
                if value == 0:
                    back = True
                    print("Boolean True")
                    break
                value = value - 1
            if back:
                print("Back triggers")
                back = False
                continue
            id = dataset[value]['id']
            response2 = requests.get("http://35.200.151.7/v1/books/" + str(id) + "/")
            jdata = json.loads(response2.text)
            chapters = jdata['books']['chapters']
            print(chapters[0]['audio_url'])
            p = vlc.MediaPlayer("http://35.200.151.7/" + chapters[0]['audio_url'])
            p.play()
            currentVolume = 30
            p.audio_set_volume(currentVolume)
            while True:
                if keyboard.is_pressed('esc'):
                    p.stop()
                    break
                elif p.is_playing():
                    if keyboard.is_pressed('space'):
                        p.pause()
                        sleep(0.3)

                    elif keyboard.is_pressed('up'):
                        if currentVolume < 100:
                            currentVolume = currentVolume + 10
                            p.audio_set_volume(currentVolume)
                            sleep(0.2)
                        else:
                            TextToSpeak("You reached the Maximum")

                    elif keyboard.is_pressed('down'):
                        if currentVolume > 10:
                            currentVolume = currentVolume - 10
                            p.audio_set_volume(currentVolume)
                            sleep(0.2)
                        else:
                            TextToSpeak("Sound is Muted")

                    elif keyboard.is_pressed('m'):
                        if p.audio_get_volume() == 0:
                            p.audio_set_volume(currentVolume)
                            sleep(0.2)
                        else:
                            p.audio_set_volume(0)
                            TextToSpeak("Sound is Muted")
                            sleep(0.2)

                    elif keyboard.is_pressed('left'):
                        p.set_time(p.get_time() - 5000)
                        sleep(0.2)

                    elif keyboard.is_pressed('right'):
                        p.set_time(p.get_time() + 5000)
                        sleep(0.2)

                else:
                    if keyboard.is_pressed('space'):
                        p.play()
                        p.audio_set_volume(currentVolume)
                        sleep(0.2)

            TextToSpeak("Player Stopped")
            print("Player Stopped")
        elif command.__contains__("exit"):
            TextToSpeak("thank you for using AudiMax!")
            exit(100)


# Driver Code
if __name__ == "__main__":
    assistant()