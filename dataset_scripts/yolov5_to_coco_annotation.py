import cv2, os, json


image_dataset_folder = "/Users/JoseLamarao/Downloads/DATASET/images/"
annotation_dataset_folder = "/Users/JoseLamarao/Downloads/DATASET/labels/"
output_folder = "/Users/JoseLamarao/Downloads/DATASET_COCO/"
method = ['train/','validation/','test/']
fruits = ['mango','almond','apple','avocado','capsicum','orange','rockmelon','strawberry']

def create_folders():
    os.makedirs(output_folder, exist_ok=True)
    os.makedirs(output_folder+'train/', exist_ok=True)
    os.makedirs(output_folder+'validation/', exist_ok=True)
    os.makedirs(output_folder+'test/', exist_ok = True)

create_folders()

for i in range(len(method)):
    image_id = 0
    annotation_id = 0
    data = {}
    data['info'] = { "year" : 2021, "version" : 1 , "description" : "" , "contributor" : "" , "url" : "" , "date_created" : ""}
    data['licenses'] = [{ "id" : 1, "url" : "" , "name" : "" }]
    data['categories'] = []
    data['images'] = []
    data['annotations'] = []

    for j in range (len(fruits)):
        data['categories'].append({ "id" : j , "name" : fruits[j], "supercategory" : "fruit"})

    for file in os.listdir(image_dataset_folder+method[i]):
        if file == '.DS_Store':
            continue
        im = cv2.imread(image_dataset_folder+method[i]+file)
        h, w, c = im.shape
        data['images'].append({"id" : image_id , "license" : 1 , "file_name" : file , "height" : h , "width" : w , "date_captured" : "" })
        
        if os.path.exists(annotation_dataset_folder+method[i]+ os.path.splitext(file)[0]+".txt"):
            with open(annotation_dataset_folder+method[i]+ os.path.splitext(file)[0]+".txt" , 'r') as infile:
                lines = infile.readlines()
            
                for line in lines:
                    splited_line = line.split()
                    xmin = (float(splited_line[1])*w)-((float(splited_line[3])*w)/2)
                    xmax = (float(splited_line[1])*w)+((float(splited_line[3])*w)/2)
                    ymin = (float(splited_line[2])*h)-((float(splited_line[4])*h)/2)
                    ymax = (float(splited_line[2])*h)+((float(splited_line[4])*h)/2)
                    o_width = xmax - xmin
                    o_height = ymax - ymin
                    area = o_width * o_height
                    data['annotations'].append({ "id" : annotation_id,  "image_id" : image_id, "category_id" : int(splited_line[0]), "bbox" : [xmin, ymin, o_width, o_height] , "area" : area , "segmentation" : [] , "iscrowd" : 0})

                    annotation_id = annotation_id + 1
        
        image_id = image_id + 1


    with open(output_folder+method[i]+'_annotations.coco.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)