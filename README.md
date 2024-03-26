# Pinterest board to PDF

A tool to convert a pinterest board to a PDF where each image takes up one page.

I use it to compile reference images to a PDF so I can view it on my kindle

### How to use

1. Clone the repo and install all dependencies with pip/pip3

2. Run the download script, it will ask for a link to the board and download images into the /output directory so you can do this for multiple boards to combine them into one pdf

```
python3 download.py
```

3. Run the makepdf script, it will use all the images in the /output directory to make a pdf called output.pdf

```
python3 makepdf.py
```

Done!

### Features

Automatically generate "contents pages", which are grids of mini preview images that, when clicked, will take you to the larger image
