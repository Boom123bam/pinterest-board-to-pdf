from py3pin.Pinterest import Pinterest
import time
import requests
from requests.exceptions import ConnectionError
import os


countrSkip = 0
countrDnld = 0
download_dir = './output/'
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

pinterest = Pinterest()

url = input("input board url: ")
if url.endswith("/"):
  url = url[:-1]
parts = url.split("/")
username = parts[-2]
boardname = parts[-1]

board = None
boards = pinterest.boards_all(username)
for i, b in enumerate(boards):
    if b['name'].lower() == boardname or b['name'].lower() == boardname.replace("-", " "):
        board = b

assert board, "board not found"

# get all pins for the board
board_pins = []
pin_batch = pinterest.board_feed(board_id=board['id'])

while len(pin_batch) > 0:
    board_pins += pin_batch
    pin_batch = pinterest.board_feed(board_id=board['id'])


# this can download images by url
def download_image(url, path):
    global countrSkip
    global countrDnld
    if os.path.isfile(path):
        countrSkip += 1
    else:
        nb_tries = 10
        while True:
            nb_tries -= 1
            try:
                # Request url
                r = requests.get(url=url, stream=True)
                break
            except ConnectionError as err:
                if nb_tries == 0:
                    raise err
                else:
                    time.sleep(1)
        if r.status_code == 200:
            countrDnld += 1
            with open(path, 'wb') as f:
                for chunk in r.iter_content(1024):
                    f.write(chunk)


# download each pin image in the specified directory
for i, pin in enumerate(board_pins):
    if 'images' in pin:
        url = pin['images']['orig']['url']
        print(f"downloading: {i}/{len(board_pins)} ", end="\r")
        download_image(url, download_dir + url.rsplit('/', 1)[-1])

print("Done downloading   ")
print("Existing files:" + str(countrSkip))
print("New files:" + str(countrDnld))
