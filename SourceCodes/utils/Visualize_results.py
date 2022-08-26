import numpy as np
import cv2
import matplotlib.pyplot as plt

# '2_20586960.jpeg' loose
# '2_22580367.jpeg' tight
# '22427751.jpeg' full
mask_path = './tight/mask/20587928.jpeg'
pred_path = './tight/pred/20587928.jpeg'

mask = cv2.imread(mask_path, 0)
pred = cv2.imread(pred_path, 0)

# threshold images and make them binary
mask = (mask > 0) * 1
pred = (pred > 0) * 1

visual_result = np.zeros((mask.shape[0], mask.shape[1], 3))

for i in range(mask.shape[0]):
    for j in range(mask.shape[1]):

        if((mask[i,j] == 0) and (pred[i,j] == 1)):
            # FP -> blue
            visual_result[i,j] = [0, 0, 1]
        
        elif((mask[i,j] == 1) and (pred[i,j] == 0)):
            # FN -> red
            visual_result[i,j] = [1, 0, 0]

        elif((mask[i,j] == 1) and (pred[i,j] == 1)):
            # TP -> green
            visual_result[i,j] = [0, 1, 0]

plt.imsave('LinkNet_tight_20587928.jpg', visual_result, dpi = 400)

