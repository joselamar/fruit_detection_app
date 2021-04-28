import os
import random 

image_dataset_folder = '/Users/JoseLamarao/Downloads/DATASET/images/'
annotation_dataset_folder = '/Users/JoseLamarao/Downloads/DATASET/labels/'
filenames = []

def create_folders():
    os.makedirs(image_dataset_folder+'train', exist_ok=True)
    os.makedirs(image_dataset_folder+'validation', exist_ok=True)
    os.makedirs(image_dataset_folder+'test', exist_ok=True)
    os.makedirs(annotation_dataset_folder+'train', exist_ok=True)
    os.makedirs(annotation_dataset_folder+'validation', exist_ok=True)
    os.makedirs(annotation_dataset_folder+'test', exist_ok=True)

for file in os.listdir(image_dataset_folder):
    filenames.append(file)

filenames.sort() 
random.seed(1)
random.shuffle(filenames) 

split_1 = int(0.8 * len(filenames))
split_2 = int(0.9 * len(filenames))
train_filenames = filenames[:split_1]
val_filenames = filenames[split_1:split_2]
test_filenames = filenames[split_2:]

create_folders()

for file in train_filenames:
    annotation_file = os.path.splitext(file)[0]+".txt"
    os.rename(image_dataset_folder+file,image_dataset_folder+'train/'+file)
    if os.path.exists(annotation_dataset_folder+annotation_file):
        os.rename(annotation_dataset_folder+annotation_file,annotation_dataset_folder+'train/'+annotation_file)

for file in val_filenames:
    annotation_file = os.path.splitext(file)[0]+".txt"
    os.rename(image_dataset_folder+file,image_dataset_folder+'validation/'+file)
    if os.path.exists(annotation_dataset_folder+annotation_file):
        os.rename(annotation_dataset_folder+annotation_file,annotation_dataset_folder+'validation/'+annotation_file)

for file in test_filenames:
    annotation_file = os.path.splitext(file)[0]+".txt"
    os.rename(image_dataset_folder+file,image_dataset_folder+'test/'+file)
    if os.path.exists(annotation_dataset_folder+annotation_file):
        os.rename(annotation_dataset_folder+annotation_file,annotation_dataset_folder+'test/'+annotation_file)
