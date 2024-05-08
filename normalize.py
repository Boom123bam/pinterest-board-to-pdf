# Normalize images that are too dark
# So that they are easier to view on kindle

import os
import cv2
import numpy as np

folder_path = "output"

# Loop over files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if not os.path.isfile(file_path):
        continue
    img = cv2.imread(file_path)
    contrast = img.std()
    brightness = np.mean(img)
    if brightness < 120:
        print(file_path)
        while brightness < 120:
            img = cv2.normalize(
                img, None, alpha=0, beta=300, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U
            )
            brightness = np.mean(img)
        cv2.imwrite(file_path, img)
