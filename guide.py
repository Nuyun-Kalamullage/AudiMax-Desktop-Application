from threading import Thread
from time import sleep

from assistant import TextToSpeak
import keyboard
back = False


def guide_help():
    global back
    while True:
        # TextToSpeak("You are in Audi-Max Help Center. Here is categories\n"
        #             "1. About commands\n"
        #             "2. About Player key Mappings\n"
        #             "3. Who are we\n"
        #             "4. What is Audi-Max\n"
        #             "5. Go Back\n")
        TextToSpeak("Now you can press the number you want to know")
        key = '0'

        while key not in ['1', '2', '3', '4', '5']:
            print("foo")
            key = str(keyboard.read_key())
            print(key)

        if key == '1':
            TextToSpeak("Command \"Search for\" : this command help to search Audio Books")
        elif key == '2':
            TextToSpeak("you can Press \"Space\" for play or pause")
        elif key == '3':
            TextToSpeak(
                "We are 3rd year undergraduates who are willing to help vision impaired people who like to listening to audio books")
        elif key == '4':
            TextToSpeak(
                "Audi-max is a Web Application for those who are like to listening audio books. apart from that this is the desktop version of our product. here we mainly focus on vision impaired that need assistant")
        elif key == '5':
            return 0
        else:
            TextToSpeak("Please Enter valid Command!")
        sleep(0.5)


if __name__ == '__main__':
    guide_help()
