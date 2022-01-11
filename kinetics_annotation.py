import argparse
import json
import csv
import os

parser = argparse.ArgumentParser()
parser.add_argument('--data_path', default=None, type=str)
parser.add_argument('--anno_path', default=None, type=str)
parser.add_argument('--output_path', default=None, type=str)
args = parser.parse_args()

data_path = args.data_path
anno_path = args.anno_path
output_path = args.output_path

#data_path = '/home/kaihua/datasets/kinetics-val/'
#anno_path = '/home/kaihua/datasets/kinetics400-anno/validate.json'
#output_path = '/home/kaihua/datasets/kinetics400-anno/post_val.csv'

print('Transfer original annotation of {} to the required format.'.format(anno_path))

orig_anno = json.load(open(anno_path))

path_label_dict = {}

for name, anno in orig_anno.items():
    subname_1 = name
    subname_2 = str(int(orig_anno[name]['annotations']['segment'][0])).zfill(6)
    subname_3 = str(int(orig_anno[name]['annotations']['segment'][1])).zfill(6)
    filename = '{}_{}_{}.mp4'.format(subname_1, subname_2, subname_3)
    label = orig_anno[name]['annotations']['label']
    
    if os.path.isfile(os.path.join(data_path, filename)):
        path = os.path.join(data_path, filename)
        path_label_dict[path] = label
        
    elif os.path.isfile(os.path.join(data_path, label, filename)):
        path = os.path.join(data_path, label, filename)
        path_label_dict[path] = label
        
    else:
        print('Cannnot find file: {}'.format(name))

with open(output_path, 'w') as f:
    writer = csv.writer(f)
    for key, val in path_label_dict.items():
        writer.writerow([key, val])

print('Complete!')