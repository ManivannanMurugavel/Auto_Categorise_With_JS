import json
import os
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('--images-folder', type=str, required=True, help='Enter the image folder')
parser.add_argument('--annotate-folder', type=str, required=True, help='Enter the annotation image folder')
args=parser.parse_args()
img_dir=args.images_folder
anno_dir=args.annotate_folder
test_dict={}
images=os.listdir(img_dir)
images=sorted(images)
#whole_images=map(lambda x: os.path.join('./plastic',x),images)
wholelist=[]
eachimg={}

wholelist=[{'ori':os.path.join('./'+img_dir,i),'annot':os.path.join('./'+anno_dir,i)} for i in images]
#print (wholelist)

with open('imgpath.json','w') as f:
	f.write(json.dumps(wholelist))

#[{'ori':''path','anno':'path'},
