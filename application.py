from time import sleep
from assistant import welcomeSpeak, TextToSpeak, get_audio
import search as sh
import get_recent as rc
import media_player


def assistant():
    global p
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

        elif command.__contains__("play recent"):
            print("play random book")
            chapters = sh.search()
            media_player.player(chapters)

        elif command.__contains__("show"):
            print("show recent book")
            chapters = rc.recent_book()
            if chapters == 0:
                continue
            else:
                media_player.player(chapters)

        elif command.__contains__("help"):
            print("play guide text via assistant")
        elif command.__contains__("exit"):
            TextToSpeak("thank you for using AudiMax!")
            exit(100)


# Driver Code
if __name__ == "__main__":
    assistant()
