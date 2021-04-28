import json
import os

trainAnnotation = '/Users/JoseLamarao/Desktop/Fuji-SfM_datasetFuji-SfM_datasetasd/1-Mask-set/training_images_and_annotations/training_set_masks.json'
testAnnotation = '/Users/JoseLamarao/Desktop/Fuji-SfM_datasetFuji-SfM_datasetasd/1-Mask-set/validation_images_and_annotations/validation_set_masks.json'
finalDataset = '/Users/JoseLamarao/Downloads/DATASET/labels/'
label = 2
img_size = 1024

with open(trainAnnotation, "r") as read_file:
    data = json.load(read_file)
    for key in data:
        if data[key]['regions'] == {}:
            continue
        else:
            filename = os.path.splitext(data[key]['filename'])[0] + '.txt'
            with open(finalDataset + filename, 'w') as f:
                nmr_bboxes=max(data[key]['regions'])
                for i in range(int(nmr_bboxes)+1):
                    dx = max(data[key]['regions'][str(i)]['shape_attributes']['all_points_x']) - min(data[key]['regions'][str(i)]['shape_attributes']['all_points_x'])
                    dy = max(data[key]['regions'][str(i)]['shape_attributes']['all_points_y']) - min(data[key]['regions'][str(i)]['shape_attributes']['all_points_y'])
                    x= max(data[key]['regions'][str(i)]['shape_attributes']['all_points_x'])-(dx/2)
                    y = max(data[key]['regions'][str(i)]['shape_attributes']['all_points_y'])-(dy/2)
                    f.write(str(label) + ' ' + str(x/img_size) + ' ' + str(y/img_size) + ' ' + str(dx/img_size) + ' ' + str(dy/img_size) + '\n')

with open(testAnnotation, "r") as read_file:
    data = json.load(read_file)
    for key in data:
        if data[key]['regions'] == {}:
            continue
        else:
            filename = os.path.splitext(data[key]['filename'])[0] + '.txt'
            with open(finalDataset + filename, 'w') as f:
                nmr_bboxes=max(data[key]['regions'])
                for i in range(int(nmr_bboxes)+1):
                    dx = max(data[key]['regions'][str(i)]['shape_attributes']['all_points_x']) - min(data[key]['regions'][str(i)]['shape_attributes']['all_points_x'])
                    dy = max(data[key]['regions'][str(i)]['shape_attributes']['all_points_y']) - min(data[key]['regions'][str(i)]['shape_attributes']['all_points_y'])
                    x = max(data[key]['regions'][str(i)]['shape_attributes']['all_points_x']) - (dx/2)
                    y = max(data[key]['regions'][str(i)]['shape_attributes']['all_points_y']) - (dy/2)
                    f.write(str(label) + ' ' + str(x / img_size) + ' ' + str(y / img_size) + ' ' + str(dx / img_size) + ' ' + str(dy / img_size) + '\n')
