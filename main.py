import requests
from bs4 import BeautifulSoup
import json
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
import os

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
    img =  soup.find("img")
    assert img
    return img

def gen_pdf():
    c = canvas.Canvas('output.pdf')

    for filename in os.listdir("output/"):
        if not filename.endswith(".jpg") and not filename.endswith(".png"):
            continue
        print("writing:", filename)
        c.drawImage(f'output/{filename}', 0, 0, 595, 842, preserveAspectRatio=True)
        c.showPage()

    c.save()

url = input("input pinterest board url: ")
print("scraping image urls...")
pinsUrls = getPinUrls(url)
imgs = (list(map(getImgs, pinsUrls)))
print(f"downloading {len(imgs)} images...")

for img in imgs:
    img_data = requests.get(img["src"]).content
    with open(f'output/{img["alt"].replace(" ", "-")}.jpg', 'wb') as handler:
        handler.write(img_data)

print("generating pdf...")
gen_pdf()
print(f"Done!")
