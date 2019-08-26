import os
import sys

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


def parse_rec(filename):
    """parse a pascal voc xml file"""
    tree = ET.parse(filename) # 
    lss = []
    for obj in tree.findall('object'):
        obj_struct = {}
        #obj_struct['name'] = obj.find('name').text
        obj_struct['name'] = 'trafficlight'
        bbox = obj.find('bndbox')
        obj_struct['bbox'] = [int(bbox.find('xmin').text),
                              int(bbox.find('ymin').text),
                              int(bbox.find('xmax').text),
                              int(bbox.find('ymax').text)]
        a = str(obj_struct['name'])+' '+str(obj_struct['bbox'][0])+' '+str(obj_struct['bbox'][1])+' '+str(obj_struct['bbox'][2])+' '+str(obj_struct['bbox'][3])
        lss.append(a)
    for i in range(len(lss)):
        print(lss[i])
    with open("ground_truth_output/"+str(filename).split('x',1)[0]+"txt", "w") as output:
        for i in range(len(lss)):
            output.write(str(lss[i])+"\n")
    return None

ls = []
ls = os.listdir("Test_annotations")
ls.sort()
# print(ls)

for file in ls:
    parse_rec('Test_annotations/'+file)
    # print(objects)


# object1 = parse_rec("1_5.mp4_01001.xml")
# print(object1)

# draw ----------------------------------------------------------------------------------------

# import matplotlib.pyplot as plt
# from PIL import Image
# image = Image.open('1_4.mp4_00904.jpg')
# fig, ax = plt.subplots(figsize=(12, 12))
# ax.imshow(image, aspect='equal')
# for i in range(len(object1)):
#     bbox = object1[i]['bbox']
#     name = object1[i]['name']
#     ax.add_patch(
#         plt.Rectangle((bbox[0], bbox[1]),
#                         bbox[2] - bbox[0],
#                         bbox[3] - bbox[1], fill=False,
#                       edgecolor='red', linewidth=3.5
#         )
#     )#draw rectangular
#     ax.text(bbox[0], bbox[1] - 2,
#             '{:s}'.format(name),
#             bbox=dict(facecolor='blue', alpha=0.5),
#             fontsize=14, color='white')#rectangular lable

# ax.set_title('parse image ')
# plt.axis("off")
# plt.tight_layout()
# plt.show()

