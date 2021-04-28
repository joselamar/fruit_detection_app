import os

import numpy as np
from PIL import Image

annotationFolder = '/Users/JoseLamarao/Desktop/MineApple Dataset/train/masks/'
finalDataset = '/Users/JoseLamarao/Downloads/DATASET/labels/'
label = 2

for file in os.listdir(annotationFolder):
    if file==".DS_Store":
        continue
    mask = Image.open(annotationFolder+file)
    mask = np.array(mask)
    obj_ids = np.unique(mask)
    obj_ids = obj_ids[1:]
    masks = mask == obj_ids[:, None, None]
    num_objs = len(obj_ids)
    boxes = []
    h, w = mask.shape
    with open(finalDataset+ os.path.splitext(file)[0] + ".txt", "w") as f:
        for ii in range(num_objs):
            pos = np.where(masks[ii])
            xmin = np.min(pos[1])
            xmax = np.max(pos[1])
            ymin = np.min(pos[0])
            ymax = np.max(pos[0])

            if xmin == xmax or ymin == ymax:
                continue

            xmin = np.clip(xmin, a_min=0, a_max=w)
            xmax = np.clip(xmax, a_min=0, a_max=w)
            ymin = np.clip(ymin, a_min=0, a_max=h)
            ymax = np.clip(ymax, a_min=0, a_max=h)

            dx = (xmax - xmin)
            dy = (ymax - ymin)
            x = xmax - (dx/2)
            y = ymax - (dy/2)
            f.write(str(label) + ' ' + str(x / w) + ' ' + str(y / h) + ' ' + str(dx / w) + ' ' + str(dy / h) + '\n')
        f.close()
