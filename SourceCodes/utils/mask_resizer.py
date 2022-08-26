# resize Ground turth masks to 256*256

import os
import cv2

path = './tight_breast/mask/'

filenames = os.listdir(path)

for img in filenames:
    original = cv2.imread(path + img, 0)

    print(f"Image {img} shape {original.shape}")

    # resize image
    resized = cv2.resize(original, (256,256), interpolation = cv2.INTER_AREA)

    cv2.imwrite(path + 'resized/' + img, resized)

