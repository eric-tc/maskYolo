# file to convert xml annotation to yolo annotation

import os
import xml.etree.ElementTree as ET



PATH= "archive/annotations/"

OUT_FOLDER="yolo-txt/"

list_file = os.listdir(PATH)

if(os.path.isdir(OUT_FOLDER)):
    pass
else:
    os.makedirs(OUT_FOLDER)

print(list_file[0])

for path in list_file:

    #apro il documento xml
    tree = ET.parse(PATH+path)
    root = tree.getroot()

    print(len(root))
    
    filename= os.path.splitext(root[1].text)[0]

    f= open(OUT_FOLDER+ filename +".txt","w+")

    width=root[2][0].text
    height=root[2][1].text
    
    for i in range(4,len(root),1):

        # print(root[i][0].text)
        # print(root[i][5][0].text)
        # print(root[i][5][1].text)
        # print(root[i][5][2].text)
        # print(root[i][5][3].text)

        width_bbox= float(float(root[i][5][2].text) -float(root[i][5][0].text))
        height_bbox= float(float(root[i][5][3].text) -float(root[i][5][1].text))

        x_center= float(root[i][5][0].text) + float(width_bbox/2)
        y_center= float(root[i][5][1].text) + float(height_bbox/2)

        x_yolo=float(x_center/float(width))
        y_yolo=float(y_center/float(height))

        width_yolo=float(width_bbox/float(width))
        height_yolo=float(height_bbox/float(height))

        class_id=None

        if (root[i][0].text=="without_mask"):
            class_id=0
        if (root[i][0].text=="with_mask"):
            class_id=1

        print(x_yolo,y_yolo,width_yolo,height_yolo,class_id)
        
        str_to_write=str(class_id) + " " + str(x_yolo) + " " + str(y_yolo) +" " + str(width_yolo) +" " + str(height_yolo) + "\n"
        f.write(str_to_write)

        
    #input()
    f.close()
        
