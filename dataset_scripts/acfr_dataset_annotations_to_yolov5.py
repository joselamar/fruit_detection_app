import os
import numpy as np
import pandas as pd

mango=0
almond=1
apple=2

x='mangoes'
annotationFolder = '/Users/JoseLamarao/Desktop/acfr-fruit-dataset/'+x+'/annotations'
finalDataset = '/Users/JoseLamarao/Downloads/DATASET/labels/'
image_size_x=500
image_size_y=500

#open every csv in annotation
for file in os.listdir(annotationFolder):
    data = pd.read_csv(annotationFolder+'/'+file)
    if data.empty:
        continue # if there is no row in csv continue, since we don't need to create the txt file
    else:
        data=data.drop('#item',1)
        data.label=mango
        data.x=(data.x.add(data.dx.div(2))).div(image_size_x)
        data.y=(data.y.add(data.dy.div(2))).div(image_size_y)
        data.dx = (data.dx).div(image_size_x)
        data.dy = (data.dy).div(image_size_y)
        data.where(data<1.0,1.0,inplace=True)
        cols = list(data.columns)
        cols = [cols[-1]] + cols[:-1]
        data = data[cols]
        f = open(finalDataset+os.path.splitext(file)[0]+".txt", "w")
        f.write(data.to_csv(sep=' ', index=False, header=False))
        f.close()

x='almonds'
annotationFolder = '/Users/JoseLamarao/Desktop/acfr-fruit-dataset/'+x+'/annotations'
image_size_x=300
image_size_y=300

#open every csv in annotation
for file in os.listdir(annotationFolder):
    data = pd.read_csv(annotationFolder+'/'+file)
    if data.empty:
        continue # if there is no row in csv continue, since we don't need to create the txt file
    else:
        data=data.drop('#item',1)
        data.label=almond
        data.x = (data.x.add(data.dx.div(2))).div(image_size_x)
        data.y = (data.y.add(data.dy.div(2))).div(image_size_y)
        data.dx = (data.dx).div(image_size_x)
        data.dy = (data.dy).div(image_size_y)
        data.where(data<1.0,1.0,inplace=True)
        cols = list(data.columns)
        cols = [cols[-1]] + cols[:-1]
        data = data[cols]
        f = open(finalDataset+os.path.splitext(file)[0]+".txt", "w")
        f.write(data.to_csv(sep=' ', index=False, header=False))
        f.close()

x='apples'
annotationFolder = '/Users/JoseLamarao/Desktop/acfr-fruit-dataset/'+x+'/annotations'
image_size_x=308
image_size_y=202

#open every csv in annotation
for file in os.listdir(annotationFolder):
    data = pd.read_csv(annotationFolder+'/'+file)
    if data.empty:
        continue # if there is no row in csv continue, since we don't need to create the txt file
    else:
        data=data.drop('#item',1)
        cols = list(data.columns)
        cols = [cols[-1]] + cols[:-1]
        data = data[cols]
        data['c-x']=data['c-x'].div(image_size_x)
        data['c-y'] = data['c-y'].div(image_size_y)
        data['radius'] = (data['radius'].mul(2)).div(image_size_x)
        data['radius-y'] = data['radius']
        data.where(data<1.0,1.0,inplace=True)
        data.label=apple
        f = open(finalDataset+os.path.splitext(file)[0]+".txt", "w")
        f.write(data.to_csv(sep=' ', index=False, header=False))
        f.close()
