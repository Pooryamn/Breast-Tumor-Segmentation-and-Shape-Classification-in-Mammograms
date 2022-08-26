import numpy as np
import os
import matplotlib.pyplot as plt

path = './full_breast/'
mask_path = path + 'mask/'
prediction_path = path + 'pred/'

filenames = os.listdir(mask_path)

for img in filenames:

    mask = plt.imread(mask_path + img)
    prediction = plt.imread(prediction_path + img)

    #DEBUG
    print(mask.shape)
    print(prediction.shape)
    print('=================================')

def IOU(mask, prediction):
    mask_area = np.count_nonzero(mask == 1)
    prediction_area = np.count_nonzero(prediction == 1)

    intersection = np.count_nonzero(np.logical_and(mask, prediction))

    IoU = intersection / (mask_area + prediction_area - intersection)

    return IoU