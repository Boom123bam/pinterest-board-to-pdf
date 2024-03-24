from reportlab.pdfgen import canvas
import os
from PIL import Image


rows = 9
cols = 8

pdf_width = 595
pdf_height = 842

w = pdf_width/cols
h = pdf_height/(rows)

c = canvas.Canvas('output.pdf')
imgs = [filename for filename in os.listdir("output/") if filename.endswith(".jpg") or filename.endswith(".png")]

def cropAr(targetAr, img:Image.Image):
    w, h = img.size
    imgAr = w/h
    if imgAr > targetAr:
        widthDiff = w * (1 - targetAr/imgAr)
        return img.crop((0 + widthDiff / 2, 0, w - widthDiff / 2, h))
    else:
        heightDiff = h * (1 - imgAr/targetAr)
        return img.crop((0, 0 + heightDiff / 2, w, h - heightDiff / 2))


def drawImg(imgPath, imgTo, x, y):
    xPos = int(x/cols * pdf_width)
    yPos = int(y/rows * pdf_height)
    img = Image.open(imgPath)
    img = cropAr(w/h, img).resize((int(w), int(h)))
    imgTo.paste(img, (xPos, yPos))


def drawLinkBox(filename, x, y):
    xPos = x/cols * pdf_width
    yPos = (1 - y/rows) * pdf_height
    c.linkAbsolute(filename,filename, (xPos, yPos, xPos+w, yPos-h))


i = 0
page = 0

while i < len(imgs):
    grid_image = Image.new("RGB", (pdf_width, pdf_height))
    for y in range(rows):
        for x in range(cols):
            if i < len(imgs):
                drawLinkBox(imgs[i], x,y)
                drawImg(f'output/{imgs[i]}', grid_image,x,y)
                i += 1
    grid_image.save(f"grid-{page}.jpg")
    c.drawImage(f"grid-{page}.jpg", 0, 0, pdf_width, pdf_height)
    c.showPage()
    page += 1
    # put on page1


for filename in imgs:
    c.bookmarkPage(filename)
    if not filename.endswith(".jpg") and not filename.endswith(".png"):
        continue
    c.drawImage(f'output/{filename}', 0, 0, pdf_width, pdf_height, preserveAspectRatio=True)
    c.showPage()

c.save()

print("Done! generated pdf")
