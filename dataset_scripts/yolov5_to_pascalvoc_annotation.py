from yattag import Doc, indent
import cv2, os

image_dataset_folder = "/Users/JoseLamarao/Downloads/DATASET/images/"
annotation_dataset_folder = "/Users/JoseLamarao/Downloads/DATASET/labels/"
output_folder = "/Users/JoseLamarao/Downloads/DATASET_PASCAL/"
method = ['train/','validation/','test/']
fruits = ['mango','almond','apple','avocado','capsicum','orange','rockmelon','strawberry']

def create_folders():
    os.makedirs(output_folder, exist_ok=True)
    os.makedirs(output_folder+'train/', exist_ok=True)
    os.makedirs(output_folder+'validation/', exist_ok=True)
    os.makedirs(output_folder+'test/', exist_ok = True)

create_folders()

for i in range(len(method)):
    for file in os.listdir(image_dataset_folder+method[i]):
        if os.path.exists(annotation_dataset_folder+method[i]+ os.path.splitext(file)[0]+".txt"):
            doc, tag, text = Doc().tagtext()

            im = cv2.imread(image_dataset_folder+method[i]+file)
            h, w, c = im.shape

            with tag('annotation'):
                with tag('folder'):
                    text()
                with tag('filename'):
                    text(file)
                with tag('path'):
                    text(file)
                with tag('source'):
                    with tag ('database'):
                        text('')
                with tag('size'):
                    with tag('width'):
                        text(w)
                    with tag('height'):
                        text(h)
                    with tag('depth'):
                        text(c)
                with tag('segmented'):
                    text('0')
                with open(annotation_dataset_folder+method[i]+ os.path.splitext(file)[0]+".txt" , 'r') as infile:
                    data = infile.readlines()
                    
                    for line in data:
                        splited_line = line.split()
                        with tag('object'):
                            with tag('name'):
                                text(fruits[int(splited_line[0])])
                            with tag('pose'):
                                text('Unspecified')
                            with tag('truncated'):
                                text('0')
                            with tag('difficult'):
                                text('0')
                            with tag('occluded'):
                                text('0')
                            with tag('bndbox'):
                                with tag('xmin'):
                                    text((float(splited_line[1])*w)-((float(splited_line[3])*w)/2))
                                with tag('xmax'):
                                    text((float(splited_line[1])*w)+((float(splited_line[3])*w)/2))
                                with tag('ymin'):
                                    text((float(splited_line[2])*h)-((float(splited_line[4])*h)/2))
                                with tag('ymax'):
                                    text((float(splited_line[2])*h)+((float(splited_line[4])*h)/2))

            result = indent(
                doc.getvalue(),
                indentation = ' '*4,
                newline = '\r\n'
            )

            with open(output_folder+method[i]+os.path.splitext(file)[0]+".xml", "w") as text_file:
                text_file.write(result)
