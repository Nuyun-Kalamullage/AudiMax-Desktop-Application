import json
from time import sleep

import keyboard
import requests
domain = "http://35.200.151.7/"
from assistant import TextToSpeak, get_audio
from search import get_id
def recentbook():
    value = 0
    response = requests.get(domain + "v1/books/")
    dataset = json.loads(response.text)['books']
    print(type(dataset))
    if len(dataset) <= 0:
        TextToSpeak("No matches Found!")
        return 0
    result = get_id(dataset)
    if result[0] == 0:
        value = result[1]
    else:
        return 0
    id = dataset[value]['id']
    response2 = requests.get(domain + "books/" + str(id) + "/")
    jdata = json.loads(response2.text)
    chapters = jdata['books']['chapters']
    print(chapters[0]['audio_url'])
    return chapters

