from time import sleep
from assistant import welcomeSpeak, TextToSpeak, get_audio
import search as sh
import get_recent as rc
import media_player
import play_random as pr
import guide as gd

def assistant():
    back = False
    welcomeSpeak()
    while True:
        TextToSpeak("Tell the command after Beep Sound")
        command = get_audio(5)
        if command.__contains__("search for"):
            chapters = sh.search()
            if chapters == 0:
                continue
            else:
                media_player.player(chapters)

        elif command.__contains__("play") and command.__contains__("book"):
            print("play random book")
            chapters = pr.play_random_book()
            if chapters == 0:
                continue
            else:
                media_player.player(chapters)

        elif command.__contains__("show") and command.__contains__("book"):
            print("show recent book")
            chapters = rc.recent_book()
            if chapters == 0:
                continue
            else:
                media_player.player(chapters)

        elif command.__contains__("help"):
            print("play guide text via assistant")
            return_result = gd.guide_help()
            if return_result == 0:
                continue
        elif command.__contains__("exit") or command.__contains__("quit"):
            TextToSpeak("thank you for using AudiMax!")
            exit(100)


# Driver Code
if __name__ == "__main__":
    assistant()
