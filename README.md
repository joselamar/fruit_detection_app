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

## 5. **Replicate Results**
1. - Download datasets separately and run for each one the correspoding script inside the dataset_scripts folder
2. - Run build_dataset.py to separate the dataset into train/test/validation
3. - If you wish to train other than the YOLOv5 model you have to run the scripts yolov5_to_coco_annotation (Faster-RCNN) andyolov5_to_pascalvoc_annotation (SSD) accordingly.
You can also download the datasets already prepared from this links:
        * YOLOv5 Dataset - https://drive.google.com/drive/folders/1LdwV9_crsCVKZmVJ6Bbqc4Hh_FztxMZi?usp=sharing
        * Faster-RCNN Dataset - https://drive.google.com/drive/folders/1UPXAOUFu2JZEwaQ1RJbGzDvLMANZ0fvn?usp=sharing
        * SSD Dataset - https://drive.google.com/drive/folders/1KxaPXDuw5zRSuuXRAVizH_l7OkhbTJ7O?usp=sharing


## 6. **Screenshots**

## 7. **References**

* #### Datasets
    * Suchet Bargoti and James Underwood. Deep fruit detection in orchards. In 2017 IEEE International Conference on Robotics and Automation (ICRA), pages 3626–3633. IEEE, 2017. 1, 13, 15, 18

      **_Obtain here_** : http://data.acfr.usyd.edu.au/ag/treecrops/2016-multifruit/
        
    * Inkyu Sa, Zongyuan Ge, Feras Dayoub, Ben Upcroft, Tristan Perez, and Chris McCool. Deepfruits: A fruit detection system using deep neural networks. Sensors, 16(8), 2016. Available from: https://www.mdpi. com/1424-8220/16/8/1222. 12, 13, 18

        **_Obtain here_** : http://enddl22.net/wordpress/datasets/deepcrops-datasets-and-annotation-tool

    * Nicolai Hani, Pravakar Roy, and Volkan Isler. Minneapple: A bench­ mark dataset for apple detection and segmentation. IEEE Robotics and Automation Letters, 5(2):852–858, Apr 2020. Available from: http: //dx.doi.org/10.1109/LRA.2020.2965061.

        **_Obtain here_** : http://rsn.cs.umn.edu/index.php/MinneApple

   * Jordi Gené­Mola, Ricardo Sanz­Cortiella, Joan R. Rosell­Polo, Josep­ Ramon Morros, Javier Ruiz­Hidalgo, Verónica Vilaplana, and Ed­ uard Gregorio. Fruit detection and 3d location using instance seg­ mentation neural networks and structure­from­motion photogramme­ try. Computers and Electronics in Agriculture, 169:105165, 2020. Available from: http://www.sciencedirect.com/science/article/ pii/S0168169919321507.

        **_Obtain here_** : https://zenodo.org/record/3712808#.XnD82iNCe01
* #### Articles