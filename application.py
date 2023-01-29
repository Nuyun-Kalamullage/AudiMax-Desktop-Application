from assistant import welcomeSpeak, TextToSpeak, get_audio
import search as sh
import get_recent as rc
import media_player
import play_random as pr
import guide as gd


def assistant():
    welcomeSpeak()
    while True:
        TextToSpeak("Tell the command after Beep Sound")
        command = get_audio(7)
        if command.__contains__("search"):
            chapters = sh.search()
            if chapters == 0:
                continue
            else:
                TextToSpeak("Playing Selected Book")
                media_player.player(chapters)

        elif command.__contains__("play") and command.__contains__("book"):
            chapters = pr.play_random_book()
            if chapters == 0:
                continue
            else:
                TextToSpeak("Playing Random Book")
                media_player.player(chapters)

        elif command.__contains__("show") and command.__contains__("book"):
            chapters = rc.recent_book()
            if chapters == 0:
                continue
            else:
                TextToSpeak("Playing Selected Book")
                media_player.player(chapters)

        elif command.__contains__("help"):
            return_result = gd.guide_help()
            if return_result == 0:
                continue
        elif command.__contains__("exit") or command.__contains__("quit"):
            TextToSpeak("thank you for using AudiMax!")
            exit(100)


# Driver Code
if __name__ == "__main__":
    assistant()
