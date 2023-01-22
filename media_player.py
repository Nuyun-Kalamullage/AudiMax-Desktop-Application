import json
from time import sleep
from assistant import TextToSpeak
import keyboard
import requests
import vlc
domain = "http://35.200.151.7/"

def player(chapters):
    p = vlc.MediaPlayer(domain + chapters[0]['audio_url'])
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