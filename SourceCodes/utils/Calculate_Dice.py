import numpy as np
import os
import cv2

def Dice(mask,prediction):
 intersection = np.logical_and(mask, prediction)
 union = np.logical_or(mask, prediction)
 dice = (2 * np.sum(intersection)) / (np.sum(union) + np.sum(intersection))

 return dice

path = './full_breast/'
mask_path = path + 'mask/'
prediction_path = path + 'pred/'

filenames = os.listdir(mask_path)

Dice_values = []

for img in filenames:

    # read images
    mask = cv2.imread(mask_path + img, 0)
    prediction = cv2.imread(prediction_path + img, 0)

    # threshold images and make them binary
    mask = (mask > 0) * 1
    prediction = (prediction > 0) * 1

    Dice_values.append(Dice(mask, prediction))

Dice_values = np.array(Dice_values)
print(Dice_values)
print(Dice_values.mean())