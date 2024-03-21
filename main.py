import requests
from bs4 import BeautifulSoup
import json

url = "https://www.pinterest.co.uk/btgchf2/animals/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

div = soup.find('script', {"type": "application/ld+json"})
assert div
items = json.loads(div.text)['itemListElement']
for item in items:
    print(item["url"])
