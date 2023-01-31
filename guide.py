import multiprocessing
from time import sleep
from assistant import TextToSpeak
import keyboard
back = False


def mainMenu():
    TextToSpeak("You are in Audi-Max Help Center. Here is categories\n")
    TextToSpeak("1. About commands\n")
    TextToSpeak("2. About Player key Mappings\n")
    TextToSpeak("3. Who are we\n")
    TextToSpeak("4. What is Audi-Max\n")
    TextToSpeak("5. Go Back\n")
    TextToSpeak("Now you can press the number you want to know")


def guide_help():
    global back, speakProcess
    while True:
        key = '0'
        speakProcess = multiprocessing.Process(target=mainMenu, args=())
        while key not in ['1', '2', '3', '4', '5']:
            if not speakProcess.is_alive():
                speakProcess.start()
            key = str(keyboard.read_key())
            if key == 'esc':
                speakProcess.terminate()
                TextToSpeak("Going Back to Main menu")
                return 0
        speakProcess.terminate()

        if key == '1':  # voice command menu voiceover
            TextToSpeak("""
                              Here are the commands in Main-Menu
                        Command \"Search for book\" : this command help to search Audio Books
                        Command \"play a random book\" : this command help to play a random Audio Book
                        Command \"show the books\" : this command help to show recent Audio Books
                        Command \"Help me\" : this command shows help menu
                        Command \"exit from Here\" or \"quit from Here\" : this both commands help you to quit the application 
                        """)

        elif key == '2':  # key binding voiceover
            TextToSpeak("       Here are the Key Mappings")
            TextToSpeak("you can Press \"up arrow key\" for increase volume")
            TextToSpeak("you can Press \"down arrow key\" for decrease volume")
            TextToSpeak("you can Press \"right arrow key\" for forward five seconds in audio")
            TextToSpeak("you can Press \"left arrow key\" for backward five seconds in audio")
            TextToSpeak("you can Press \"Space\" for play or pause")
            TextToSpeak("you can Press \"m\" for mute or unmute sound")
            TextToSpeak("you can Press \"esc\" for stop the audio and navigate to main menu")
            TextToSpeak("you can Press \"page up\" for play next chapter")
            TextToSpeak("you can Press \"page down\" for play previous chapter")

        elif key == '3':  # about us voiceover
            TextToSpeak("""                
            Cloud Gauge is a team of 10 IT students from Sri Lanka Technological Campus, who are 
            passionate about developing cloud application to make a difference in the world. We believe our digital 
            skills, team spirit and dedication will make our products outstanding from one another 
            """)

        elif key == '4':  # about application voiceover
            TextToSpeak("""             
            AudiMax is a digital library which contains audio books and pdfs for the readers. Also, 
            it is a great opportunity for the writers who have a passion to share their ideology with the world,
            because they can easily publish their books to the digital space with our platform Speciality of AudiMax 
            is, this desktop application has voice assistant features and keyboard bound navigation. 
            """)

        elif key == '5':
            TextToSpeak("Going Back to Main menu")
            return 0

        else:
            TextToSpeak("Please Enter valid Command!")
        sleep(0.5)


if __name__ == '__main__':
    guide_help()
