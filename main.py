import requests
from bs4 import BeautifulSoup
import json


def write(s):
    with open("output.txt", "w") as file:
        file.write(s)

def getPinUrls(boardUrl) -> list:
    response = requests.get(boardUrl)
    soup = BeautifulSoup(response.content, "html.parser")
    div = soup.find('script', {"type": "application/ld+json"})
    assert div
    items = json.loads(div.text)['itemListElement']
    return list(map(lambda i:i["url"], items))

def getImgs(pinUrl):
    response = requests.get(pinUrl)
    soup = BeautifulSoup(response.content, "html.parser")
    write(soup.prettify())
    img =  soup.find("img")
    assert img
    return img

url = "https://www.pinterest.co.uk/btgchf2/animals/"
pinsUrls = getPinUrls(url)
imgs = (list(map(getImgs, pinsUrls)))

for img in imgs:
    img_data = requests.get(img["src"]).content
    with open(f'output/{img["alt"].replace(" ", "-")}.jpg', 'wb') as handler:
        handler.write(img_data)

# download(img_urls, 10, "output")
