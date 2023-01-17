# importing speech recognition package from google api
from asyncio import sleep

import speech_recognition as sr
import playsound  # to play saved mp3 file
from gtts import gTTS  # google text to speech
import os  # to save/open files

# import wolframalpha  # to calculate strings into formula
# from selenium import webdriver  # to control browser operations
import requests
import keyboard
import pyttsx3
import json
import vlc

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


#
def TextToSpeak(Text):
    engine.say(Text)
    engine.runAndWait()


def welcomeSpeak():
    engine.say("Hello there you are in assisted mode")
    engine.runAndWait()


# num = 1

# def assistant_speaks(output):
#     global num
#     # num to rename every audio file
#     # with different name to remove ambiguity
#     num += 1
#     print("PerSon : ", output)
#
#     toSpeak = gTTS(text=output, lang='en', slow=False)
#     # saving the audio file given by google text to speech
#     file = str(num) + ".mp3"
#     toSpeak.save(file)
#
#     # playsound package is used to play the same file.
#     playsound.playsound(file, True)
#     os.remove(file)


def get_audio(wait_seconds):
    rObject = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        rObject.adjust_for_ambient_noise(source)
        print("Speak...")
        TextToSpeak("Beeeep")
        # recording the audio using speech recognition
        audio = rObject.listen(source, phrase_time_limit=wait_seconds)
    print("Stop.")  # limit 5 secs

    try:
        # keyword = ['search for','exit','1','2','3','4','5','text book','Oliver Twist']
        text = rObject.recognize_google(audio, language='en-US')
        # text1 = rObject.recognize_sphinx(audio, language='en-US',keyword_entries=keyword)
        print("You : ", text)
        return text

    except:
        TextToSpeak("Could not understand your audio, PLease try again !")
        return "all"


# def listen_audio():
#     rObject = sr.Recognizer()
#     audio = ''
#
#     with sr.Microphone() as source:
#         rObject.adjust_for_ambient_noise(source)
#         print("Listing...")
#         # recording the audio using speech recognition
#         audio = rObject.listen_in_background(source, catch_audio)


# def catch_audio():
#     text = 'stop'
#     try:
#         rObject = sr.Recognizer()
#         text = rObject.recognize_google(self.audio, language='en-US')
#     except:
#         print("small error")
#
#     print("You said: " + text)
#     if text.__contains__('play') or text.__contains__('pause'):
#         vlc.libvlc_media_player_set_pause(p, vlc.libvlc_media_player_is_playing())
#     elif text.__contains__('volume down'):
#         vlc.libvlc_audio_set_volume(p_mi=p, i_volume=(vlc.libvlc_audio_get_volume(p_mi=p) - 25))
#     elif text.__contains__('volume up'):
#         vlc.libvlc_audio_set_volume(p_mi=p, i_volume=(vlc.libvlc_audio_get_volume(p_mi=p) + 25))


# Driver Code
if __name__ == "__main__":
    global p
    welcomeSpeak()
    while (1):
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
                # dataset = response.json()['books']
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
            # print("i = " + str(i))
            value = 9
            digit = range(0, 9)
            while not (value in digit):
                value = int(keyboard.read_key())
                value = value - 1
                # print("Value is " + str(value))
            id = dataset[value]['id']
            response2 = requests.get("http://35.200.151.7/v1/books/" + str(id) + "/")
            jdata = json.loads(response2.text)
            chapters = jdata['books']['chapters']
            print(chapters[0]['audio_url'])
            p = vlc.MediaPlayer("http://35.200.151.7/" + chapters[0]['audio_url'])
            p.play()
            while(True):
                if p.is_playing():
                    if keyboard.is_pressed('a'):
                        p.pause()
                    elif keyboard.is_pressed(hotkey=keyboard.KEY_UP):
                        print(p.audio_get_volume)
                        p.audio_set_volume(100)
                    elif keyboard.is_pressed(hotkey=keyboard.KEY_DOWN):
                        print(p.audio_get_volume)
                        p.audio_set_volume(40)
                elif keyboard.is_pressed('b'):
                    break
                else:
                    p.play()
                sleep(1)

            # while(vlc.libvlc_media_player_is_playing(p_mi=p)):



        elif command.__contains__("exit"):
            TextToSpeak("thank you for using AudiMax!")
            exit(100)
        # else:
        #     TextToSpeak("Please Tell me a Valid Command")

    # while (1):
    #
    #     assistant_speaks("What can i do for you?")
    #     # text = get_audio().lower()
    #     text = "hello guys"
    #     if text == 0:
    #         continue
    #
    #     if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text):
    #         assistant_speaks("Ok bye, " + name + '.')
    #         break
