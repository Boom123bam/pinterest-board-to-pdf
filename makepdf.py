from reportlab.pdfgen import canvas
import os


c = canvas.Canvas('output.pdf')

for filename in os.listdir("output/"):
    if not filename.endswith(".jpg") and not filename.endswith(".png"):
        continue
    c.drawImage(f'output/{filename}', 0, 0, 595, 842, preserveAspectRatio=True)
    c.showPage()

c.save()

print("Done! generated pdf")
