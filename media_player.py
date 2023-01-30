import json
from time import sleep
from assistant import TextToSpeak
import keyboard
import requests
import vlc

domain = "https://audimax.xyz/"
keyArray = ['up', 'down', 'right', 'left', 'space', 'm', 'esc', 'page down', 'page up']


def player(chapters):
    p = vlc.MediaPlayer()
    currentVolume = 50
    p.audio_set_volume(currentVolume)
    playerIns = vlc.Instance()
    media_list = playerIns.media_list_new()
    i = 0
    for url in chapters:
        media_list.add_media(playerIns.media_new(url['audio_url']))
        i += 1
    p.set_media(media_list[0])
    p.play()
    current_chapter = 0
    print(f"Chapter {current_chapter+1} playing >>>>")
    while True:
        key = keyboard.read_key()
        if key in keyArray:
            if key == "esc":
                p.stop()
                TextToSpeak("Player Stopped")
                break

            elif key == 'page up':
                if (current_chapter + 1) < i:
                    current_chapter += 1
                    p.set_media(media_list[current_chapter])
                    TextToSpeak("Playing Next Chapter")
                else:
                    if i == 1:
                        TextToSpeak("This audio book has only one chapter")
                    else:
                        TextToSpeak("Playing chapter one")
                        current_chapter = 0
                        p.set_media(media_list[current_chapter])
                print(f"Chapter {current_chapter+1} playing >>>>")
                p.play()
                sleep(0.2)

            elif key == 'page down':
                if (current_chapter - 1) >= 0:
                    current_chapter -= 1
                    p.set_media(media_list[current_chapter])
                    TextToSpeak("Playing Previous Chapter")
                else:
                    if i == 1:
                        TextToSpeak("This audio book has only one chapter")
                    else:
                        TextToSpeak("Playing last chapter")
                        current_chapter = i - 1
                        p.set_media(media_list[current_chapter])
                print(f"Chapter {current_chapter+1} playing >>>>")
                p.play()
                sleep(0.2)

            elif key == 'space':
                p.set_pause(p.is_playing())
                sleep(0.2)

            elif key == 'up':
                if currentVolume < 100:
                    currentVolume = currentVolume + 10
                    p.audio_set_volume(currentVolume)
                else:
                    p.audio_set_volume(currentVolume)
                    TextToSpeak("You reached the Maximum")
                sleep(0.2)

            elif key == 'down':
                if currentVolume >= 10:
                    currentVolume = currentVolume - 10
                    p.audio_set_volume(currentVolume)
                else:
                    TextToSpeak("Sound is Muted")
                sleep(0.2)

            elif key == 'm':
                if p.audio_get_volume() == 0:
                    p.audio_set_volume(currentVolume)
                else:
                    p.audio_set_volume(0)
                    TextToSpeak("Sound is Muted")
                sleep(0.2)

            elif key == 'left':
                p.set_time(p.get_time() - 5000)
                sleep(0.2)

            elif key == 'right':
                p.set_time(p.get_time() + 5000)
                sleep(0.2)


if __name__ == "__main__":
    response2 = requests.get(domain + "v1/books/" + str(5) + "/")
    jdata = json.loads(response2.text)
    print(jdata)
    chapters = jdata['books']['chapters']
    print(chapters)
    player(chapters)
