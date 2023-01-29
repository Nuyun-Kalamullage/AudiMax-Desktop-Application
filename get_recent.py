import json
import requests
from assistant import TextToSpeak
from search import get_id

domain = "https://audimax.xyz/"


def recent_book():
    value = 0
    response = requests.get(domain + "v1/books/")
    dataset = json.loads(response.text)['books']
    print(type(dataset))
    if len(dataset) <= 0:
        TextToSpeak("No matches Found!")
        return 0
    else:
        rcResult = get_id(dataset)
        print(rcResult)
        if rcResult[0] == 0:
            value = rcResult[1]
        else:
            return 0
        id = dataset[value]['id']
        response2 = requests.get(domain + "v1/books/" + str(id) + "/")
        jdata = json.loads(response2.text)
        chapters = jdata['books']['chapters']
        print(chapters[0]['audio_url'])
        return chapters


if __name__ == "__main__":
    recent_book()
