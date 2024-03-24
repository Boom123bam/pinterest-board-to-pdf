from PIL import Image

def cropAr(targetAr, img:Image.Image):
    w, h = img.size
    imgAr = w/h
    if imgAr > targetAr:
        widthDiff = w * (1 - targetAr/imgAr)
        return img.crop((0 + widthDiff / 2, 0, w - widthDiff / 2, h))
    else:
        heightDiff = h * (1 - imgAr/targetAr)
        return img.crop((0, 0 + heightDiff / 2, w, h - heightDiff / 2))


def drawImg(imgPath, imgTo, x, y, w, h):
    img = Image.open(imgPath)
    img = cropAr(w/h, img).resize((w, h))
    imgTo.paste(img, (x, y))

grid_image = Image.new("RGB", (400, 400))
drawImg("1.jpg", grid_image, 0, 0, 200, 200)
drawImg("2.jpg", grid_image, 200, 0, 200, 200)
drawImg("3.jpg", grid_image, 0, 200, 200, 200)
drawImg("4.jpg", grid_image, 200, 200, 200, 200)

grid_image.save("combined_grid.jpg")
