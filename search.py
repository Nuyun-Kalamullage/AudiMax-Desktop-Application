import json
import multiprocessing

import keyboard
import requests

from assistant import TextToSpeak, get_audio

domain = "https://audimax.xyz/"


def speakMenu(dataset):
    global i
    i = 1
    for tempBook in dataset:
        title = tempBook['title']
        print(str(i) + ". Book Name is " + title)
        TextToSpeak(str(i) + ". Book Name is " + title)
        i = i + 1
    TextToSpeak('Please Select your Audio Book Number in key board')


def get_id(dataset):
    back = False
    speakBgProcess = multiprocessing.Process(target=speakMenu, args=(dataset,))
    speakBgProcess.start()
    value = 9
    digit = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    while (value not in digit) or (value >= len(dataset)):
        value = str(keyboard.read_key())
        if value == "esc":
            back = True
            speakBgProcess.terminate()
            break
        if value.isnumeric():
            value = int(value) - 1
    if back:
        back = False
        speakBgProcess.terminate()
        return -1, 0
    speakBgProcess.terminate()
    return 0, value


def search():
    value = 0
    while True:
        TextToSpeak("Please Tell me the book name after Beep Sound")
        bookName = get_audio(8)
        if bookName.__contains__("go back"):
            TextToSpeak("Going Back to Main menu")
            return 0
        parameters = {
            "query": bookName
        }
        response = requests.get(domain + "v1/books/", params=parameters)
        dataset = json.loads(response.text)['books']
        if len(dataset) > 0:
            result = get_id(dataset)
            if result[0] == 0:
                value = result[1]
            else:
                return 0
            id = dataset[value]['id']
            response2 = requests.get(domain + "v1/books/" + str(id) + "/")
            jdata = json.loads(response2.text)
            chapters = jdata['books']['chapters']
            if len(chapters) == 0:
                TextToSpeak("No Chapters found in This audio-book ")
            else:
                return chapters
        else:
            TextToSpeak("No matches Found!")

