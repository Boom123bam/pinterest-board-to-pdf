from reportlab.pdfgen import canvas
import os

rows = 9
cols = 8

pdf_width = 595
pdf_height = 842

w = pdf_width/cols
h = pdf_height/(rows)

c = canvas.Canvas('output.pdf')
imgs = os.listdir("output/")

def drawThumbnail(filename, x, y):
    if not filename.endswith(".jpg") and not filename.endswith(".png"):
        return
    xPos = x/cols * pdf_width
    yPos = y/rows * pdf_height
    c.drawImage(f'output/{filename}', xPos, yPos - h, w, h, preserveAspectRatio=True)
    c.linkAbsolute(filename,filename, (xPos, yPos, xPos+w, yPos-h))


i = 0
while i < len(imgs):
    for y in range(rows, 0 ,-1):
        for x in range(cols):
            if i < len(imgs):
                drawThumbnail(imgs[i], x,y)
                i += 1
    c.showPage()

for filename in imgs:
    c.bookmarkPage(filename)
    if not filename.endswith(".jpg") and not filename.endswith(".png"):
        continue
    c.drawImage(f'output/{filename}', 0, 0, pdf_width, pdf_height, preserveAspectRatio=True)
    c.showPage()

c.save()

print("Done! generated pdf")
