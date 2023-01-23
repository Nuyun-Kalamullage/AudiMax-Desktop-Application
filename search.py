import json
import keyboard
import requests

from assistant import TextToSpeak, get_audio

domain = "http://35.200.151.7/"


def get_id(dataset):
    back = False
    i = 1
    for tempBook in dataset:
        title = tempBook['title']
        print(str(i) + ". Book Name is " + title)
        TextToSpeak(str(i) + ". Book Name is " + title)
        i = i + 1

    TextToSpeak('Please Select your Audio Book Number in key board')
    value = 9
    digit = range(0, 9)
    while (value not in digit) or (value >= i - 1):
        value = int(keyboard.read_key())
        if value == 0:
            back = True
            print("Boolean True")
            break
        value = value - 1
    if back:
        print("Back triggers")
        back = False
        return -1, 0
    return 0, value


def search():
    value = 0
    while True:
        TextToSpeak("Please Tell me the book name after Beep Sound")
        bookName = get_audio(8)
        if bookName.__contains__("go back"):
            return 0
        parameters = {
            "query": bookName
        }
        response = requests.get(domain + "v1/books/", params=parameters)
        dataset = json.loads(response.text)['books']
        print(type(dataset))
        if len(dataset) > 0:
            break
        else:
            TextToSpeak("No matches Found!")
    result = get_id(dataset)
    # print(result)
    if result[0] == 0:
        value = result[1]
    else:
        return 0
    id = dataset[value]['id']
    response2 = requests.get(domain + "v1/books/" + str(id) + "/")
    jdata = json.loads(response2.text)
    chapters = jdata['books']['chapters']
    print(chapters[0]['audio_url'])
    return chapters
