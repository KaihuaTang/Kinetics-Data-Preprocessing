import argparse
import json
import csv
import os

parser = argparse.ArgumentParser()
parser.add_argument('--data_path', default=None, type=str)
parser.add_argument('--anno_path', default=None, type=str)
args = parser.parse_args()

data_path = args.data_path
anno_path = args.anno_path

#data_path = '/home/kaihua/datasets/kinetics-val/'
#anno_path = '/home/kaihua/datasets/kinetics400-anno/'

annotation_list = ['train', 'test', 'validate']


def get_transferred_anno(org_anno_path, tgt_output_path, label2id):
    print('Transfer original annotation of {} to the required format.'.format(org_anno_path))
    orig_anno = json.load(open(org_anno_path))

    path_label_dict = {}
    for name, anno in orig_anno.items():
        subname_1 = name
        subname_2 = str(int(anno['annotations']['segment'][0])).zfill(6)
        subname_3 = str(int(anno['annotations']['segment'][1])).zfill(6)
        filename = '{}_{}_{}.mp4'.format(subname_1, subname_2, subname_3)
        label = anno['annotations']['label']
    
        if os.path.isfile(os.path.join(data_path, filename)):
            path = os.path.join(data_path, filename)
            path_label_dict[path] = label2id[label]
        
        elif os.path.isfile(os.path.join(data_path, label, filename)):
            path = os.path.join(data_path, label, filename)
            path_label_dict[path] = label2id[label]
        
        else:
            print('Cannnot find file: {}'.format(name))
            pass

    with open(tgt_output_path, 'w') as f:
        writer = csv.writer(f)
        for key, val in path_label_dict.items():
            writer.writerow([key, val])

    return path_label_dict


# get label 2 id mapping
train_anno = json.load(open(os.path.join(anno_path, 'train.json')))
label_list = list(set([anno['annotations']['label'] for name, anno in train_anno.items()]))
label_list.sort()
label2id = {label: i for i, label in enumerate(label_list)}
with open(os.path.join(anno_path, 'label2id.json'), 'w') as outfile:
    json.dump(label2id, outfile)


for item in annotation_list:
    org_anno_path = os.path.join(anno_path, item+'.json')
    tgt_output_path = os.path.join(anno_path, 'output_'+item+'.csv')
    
    # get transferred annotation file
    get_transferred_anno(org_anno_path, tgt_output_path, label2id)

print('Complete!')