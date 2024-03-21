import requests
from bs4 import BeautifulSoup

def write(s):
    with open("output.txt", "w") as file:
        file.write(s)


def getImgs(pinUrl):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    # write(soup.prettify())
    img =  soup.find("img")
    assert img
    return img

print(getImgs("https://www.pinterest.co.uk/pin/1100637596421034651/"))
