import os
from PIL import Image

datasetFolder = '/Users/JoseLamarao/Desktop/deepFruits_dataset/datasets/'
finalDataset = '/Users/JoseLamarao/Downloads/DATASET/labels/'

def writeLabel(fruit,label,j):
    with open(datasetFolder + fruit + '/train_RGB.txt', 'r') as infile:
        data = infile.readlines()
        for line in data:
            line = line.split()
            img = Image.open(datasetFolder+fruit +'/'+ line[0])
            w= img.width
            h= img.height
            filename = os.path.splitext(line[0].split('/')[1])[0] + '.txt'
            with open(finalDataset+filename, 'w') as f:
                for i in range(int(line[1]), 0, -1):
                    if fruit == 'capsicum':
                        dx = abs((float(line[(i * 4)]) - float(line[(i * 4) - 2])))
                        dy = abs((float(line[(i * 4)+1]) - float(line[(i * 4) - 1])))
                        x = float(line[(i * 4)]) - (dx/2)
                        y = float(line[(i * 4)+1]) - (dy/2)
                        f.write(str(label) + ' ' + str(x / w) + ' ' + str(y / h) + ' ' + str(dx / w) + ' ' + str(dy / h) + '\n')
                    else:
                        dx = abs((float(line[(i * j) - 2]) - float(line[(i * j) - 4])))
                        dy = abs((float(line[(i * j) - 1]) - float(line[(i * j) - 3])))
                        x = float(line[(i * j) - 2]) - (dx/2)
                        y = float(line[(i * j) - 1]) - (dy/2)
                        f.write(str(label)+' '+str(x/w)+' '+str(y/h)+' '+str(dx/w)+' '+str(dy/h)+'\n')
    with open(datasetFolder + fruit + '/test_RGB.txt', 'r') as infile:
        data = infile.readlines()
        for line in data:
            line = line.split()
            img = Image.open(datasetFolder + fruit + '/TEST_RGB/' + line[0].split('/')[1])
            w = img.width
            h = img.height
            filename = os.path.splitext(line[0].split('/')[1])[0] + '.txt'
            with open(finalDataset + filename, 'w') as f:
                for i in range(int(line[1]), 0, -1):
                    dx = abs((float(line[(i * j) - 2]) - float(line[(i * j) - 4])))
                    dy = abs((float(line[(i * j) - 1]) - float(line[(i * j) - 3])))
                    x = float(line[(i * j) - 2]) - (dx/2)
                    y = float(line[(i * j) - 1]) - (dy/2)
                    if(x/w)>1.0 or (x/w)<0.0:
                        print(filename)
                        print(w, h)

                    f.write(str(label)+' '+str(x/w)+' '+str(y/h)+' '+str(dx/w)+' '+str(dy/h)+'\n')

for fruit in os.listdir(datasetFolder):
    if fruit == 'apple':
        label=2
        writeLabel(fruit,label,6)
    elif fruit == 'avocado':
        label=3
        writeLabel(fruit, label,6)
    elif fruit == 'capsicum':
        label = 4
        writeLabel(fruit, label,6)
    elif fruit == 'mango':
        label = 0
        writeLabel(fruit, label,6)
    elif fruit == 'orange':
        label = 5
        writeLabel(fruit, label,6)
    elif fruit == 'rockmelon':
        label = 6
        writeLabel(fruit, label,6)
    elif fruit == 'strawberry':
        label = 7
        writeLabel(fruit, label,6)
