numImgs = 18
rows = 3
cols = 4



pdf_width = 595
pdf_height = 842

import math
w = math.ceil(pdf_width/cols)
h = math.ceil(pdf_height/rows)

from pypdf import PdfReader, PdfWriter
from pypdf.annotations import Link
import os

pdf_path = os.path.join("output.pdf")
reader = PdfReader(pdf_path)
writer = PdfWriter(clone_from=reader)

numIndexPages = math.ceil(numImgs/(rows*cols))

def drawLinkBox(page_number, target_page_index, x, y):
    xPos = math.floor(x/cols * pdf_width)
    yPos = math.floor((1 - y/rows) * pdf_height)
    annotation = Link(
        rect=(xPos, yPos - h, xPos+w, yPos), target_page_index=target_page_index
    )
    writer.add_annotation(page_number, annotation=annotation)

    #good
    # annotation = Link(
    #     rect=(50, 500, 700, 650), target_page_index=3
    # )
    #bad
    # annotation = Link(
    #     rect=(0.0, 842.0, 148.75, 561.3333333333333), target_page_index=3
    # )
    #bad
    # annotation = Link(
    #     rect=(0, 842, 148, 561), target_page_index=3
    # )
    #good
    # annotation = Link(
    #     rect=(0, 561, 148, 842), target_page_index=3
    # )


i = 0
page = 0
while i < numImgs:
    for y in range(rows):
        for x in range(cols):
            if i < numImgs:
                drawLinkBox(page, i + numIndexPages, x,y)
                i += 1
    page += 1


with open("annotated-pdf.pdf", "wb") as fp:
    writer.write(fp)


# print("Done! generated pdf")
