import requests
from bs4 import BeautifulSoup
import json

def getPinUrls(boardUrl) -> list:
    response = requests.get(boardUrl)
    soup = BeautifulSoup(response.content, "html.parser")
    div = soup.find('script', {"type": "application/ld+json"})
    assert div
    items = json.loads(div.text)['itemListElement']
    return list(map(lambda i:i["url"], items))

def getImgUrl(pinUrl):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    img =  soup.find("img")
    assert img
    return img['src']

url = "https://www.pinterest.co.uk/btgchf2/animals/"
pinsUrls = getPinUrls(url)
print(list(map(getImgUrl, pinsUrls)))
