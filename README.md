# Fruit Detection App

This repository contains all of the work conducted in the scope of a Masters Degree in Computer Science @ [UBI](https://www.ubi.pt/) to build an android application capable of detecting fruits while using artificial intelligence, more specificaly object detection frameworks.

---

## 1. **Datasets** - Pre-processing and preparing datasets

[**'dataset_scripts/'**](https://github.com/joselamar/fruit_detection_app/tree/main/dataset_scripts) - In this folder there are scripts to put the annotation format into YOLOv5 from a collection of [datasets](#datasets). There is also a script to transform ***YOLOv5*** annotations to ***PASCAL VOC*** format as well as to the ***COCO*** format. At last, the ['build_dataset.py'](https://github.com/joselamar/fruit_detection_app/tree/main/dataset_scripts/build_dataset.py) splits the dataset into training, validation and testing. In order to replicate the same results it's necessary to change the source and destination folders, on each script.

`NOTE: The dataset used can be obtained through this` [link](https://drive.google.com/drive/folders/1dKVL9DgJ5-_c2TCMWHvfrkvBODwr_pqX?usp=sharing)`, or separately by following the references links.`

## 2. **Object Detection** - Training and Testing Object Detection Frameworks
>  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse id risus fringilla, tristique est id, mattis leo. Proin vulputate dolor a nunc fermentum dapibus. In massa ante, condimentum sit amet ullamcorper quis, elementum a dolor. Suspendisse pretium sapien in accumsan viverra.

[**yolov5_script.py**](https://github.com/joselamar/fruit_detection_app/tree/main/yolov5_script.py) - Is the script to train on the ***YOLOv5*** model. It can also be used to detect fruits 
    
- To train you can use this command and change it accordingly:

        python3 yolov5_script.py --yaml 'yaml_location' --batch_size batch_size --epochs nmbr_epochs --is_training 1 --weights 'weights_location' --project 'save_folder_location'

`NOTE: To test the model you have to switch --is_training 1 for --is_training 0.`

[**fastrcnn_script.py**](https://github.com/joselamar/fruit_detection_app/tree/main/fastrcnn_script.py) - Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse id risus fringilla, tristique est id, mattis leo.

[**ssd_script.py**](https://github.com/joselamar/fruit_detection_app/tree/main/ssd_script.py) - Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse id risus fringilla, tristique est id, mattis leo.

## 3. **Model Conversion** - TensorFlow Lite

> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse id risus fringilla, tristique est id, mattis leo. Proin vulputate dolor a nunc fermentum dapibus. In massa ante, condimentum sit amet ullamcorper quis, elementum a dolor. Suspendisse pretium sapien in accumsan viverra.

## 4. **Mobile Application** - Development

>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse id risus fringilla, tristique est id, mattis leo. Proin vulputate dolor a nunc fermentum dapibus. In massa ante, condimentum sit amet ullamcorper quis, elementum a dolor. Suspendisse pretium sapien in accumsan viverra.

## 5. Replicate Results

## 6. **Screenshots**

## 7. **References**

* #### Datasets
        
* #### Articles