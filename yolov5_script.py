#!/usr/bin/env python3
import argparse
import os
import torch

ap = argparse.ArgumentParser()
ap.print_help()

ap.add_argument('--yaml', required=True, help='yaml location')
ap.add_argument('--batch_size', required=True, help='Batch size')
ap.add_argument('--epochs', required=True, help='Number of epochs')
ap.add_argument('--is_training', required=True, help='1 to train model, 0 to test model, 2 to infere')
ap.add_argument('--weights', required=True, help='weights location from the trained model ')
ap.add_argument('--save', required=True, help='Save Folder location')

args = vars(ap.parse_args())

os.system("pip3 install -qr yolov5/requirements.txt")   # install dependencies

print('Setup complete. Using torch %s %s' % (torch.__version__,
      torch.cuda.get_device_properties(0) if torch.cuda.is_available() else 'CPU'))

if args['is_training'] == '1':
      # Train YOLOv5s
      os.system('python3 yolov5/train.py --data %s --batch %s --epochs %s --weights %s --cache --project %s' % (args['yaml'], args['batch_size'] , args['epochs'] , args['weights'], args['save'] ))
elif args['is_training'] == '0':
      # Detect YOLOv5s
      os.system("python '/content/yolov5/detect.py' --source '/content/Apple-tree-with-fruit-1.jpg' --weights '/content/drive/MyDrive/exp/weights/best.pt' --conf 0.25")
else:
      print ("Insert a valid value between 1 to train and 0 to test the model")