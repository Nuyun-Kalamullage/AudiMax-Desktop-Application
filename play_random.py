import json
import requests
from assistant import TextToSpeak
import random

domain = "https://audimax.xyz/"


def play_random_book():
    value = 0
    while True:
        response = requests.get(domain + "v1/books/")
        dataset = json.loads(response.text)['books']
        if len(dataset) <= 0:
            TextToSpeak("No matches Found!")
            return 0
        else:
            if len(dataset) == 1:
                value = 0
            else:
                value = random.randint(0, len(dataset)-1)
            id = dataset[value]['id']
            response2 = requests.get(domain + "v1/books/" + str(id) + "/")
            jdata = json.loads(response2.text)
            chapters = jdata['books']['chapters']
            if len(chapters) == 0:
                TextToSpeak("Sorry!! No Chapters found in This audio-book.       searching for new book")
                continue
            else:
                return chapters


if __name__ == '__main__':
    play_random_book()