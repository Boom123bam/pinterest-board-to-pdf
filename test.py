import requests
from bs4 import BeautifulSoup
import json

url = "https://www.pinterest.co.uk/pin/1100637596421018163/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
img =  soup.find("img")
assert img
print(img['src'])
