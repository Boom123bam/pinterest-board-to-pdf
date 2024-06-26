import math
from reportlab.pdfgen import canvas
import os
from PIL import Image

rows = 9
cols = 8

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
    img = Image.open(imgPath)
    img = cropAr(w/h, img).resize((w, h))
    imgTo.paste(img, (x, y))


def makeContentsGrid():
    i = 0
    page = 0
    if not os.path.exists("grid"):
        os.makedirs("grid")

    while i < len(imgs):
        grid_image = Image.new("RGB", (pdf_width, pdf_height))
        for row in range(rows):
            for col in range(cols):
                if i < len(imgs):
                    x = int(col/cols * pdf_width)
                    y = int(row/rows * pdf_height)
                    # from bl
                    c.linkAbsolute("",imgs[i], (x, pdf_height-y-h, x+w, pdf_height-y))
                    # from tl
                    drawImg(f'output/{imgs[i]}', grid_image,x,y)
                    i += 1
        grid_image.save(f"grid/grid-{page}.jpg")
        c.drawImage(f"grid/grid-{page}.jpg", 0, 0, pdf_width, pdf_height)
        c.showPage()
        page += 1


pdf_width = 595
pdf_height = 842

w = math.ceil(pdf_width/cols)
h = math.ceil(pdf_height/rows)

c = canvas.Canvas('output.pdf')
imgs = [filename for filename in os.listdir("output/") if filename.endswith(".jpg") or filename.endswith(".png")]

makeContentsGrid()

for filename in imgs:
    c.bookmarkPage(filename)
    if not filename.endswith(".jpg") and not filename.endswith(".png"):
        continue
    c.drawImage(f'output/{filename}', 0, 0, pdf_width, pdf_height, preserveAspectRatio=True)
    c.showPage()

c.save()

print("Done! generated pdf")
