# Kinetics-Data-Preprocessing

Kinetics-400 and Kinetics-600 are common video recognition datasets used by popular video understanding projects like [SlowFast](https://github.com/facebookresearch/SlowFast) or [PytorchVideo](https://github.com/facebookresearch/pytorchvideo). However, their instruction of dataset preparation is too brief. Therefore, this project provides a more detailed instruction for Kinetics-400/-600 data preprocessing.


## Download the raw videos

There are multiple ways to download the raw videos of Kinetics-400 and Kinetics-600. Here, I list two common choices that I found to be simple and fast: 

1. Download the videos via the official [scripts](https://github.com/activitynet/ActivityNet/tree/master/Crawler/Kinetics). However, I noticed that this option is very slow, so I personally recommend the next choice.

2. Download the compressed videos from the Common Visual Data Foundation Servers following the [repository](https://github.com/cvdfoundation/kinetics-dataset), which is much faster as they organized 650,000 independent video clips into several compressed files.


## Resize the videos

The common data preprocessing of Kinetics requires all videos to be resized to the short edge size of 256. Therefore, I use the [moviepy package](https://zulko.github.io/moviepy/) to do so. The package can be easily installed by the following command:

```
pip install moviepy
```

Then, you can use the [resize_video.py](https://github.com/KaihuaTang/Kinetics-Data-Preprocessing/blob/main/resize_video.py) to resize all the videos within the given folder by following command:

```
python resize_video.py --size 256 --path YOUR_VIDEO_CONTAINER
```

**IMPORTANT! Note that the *resize_video.py* will replace the original mp4 files. If you want to keep the original files, please make copys before resizing.**

## Prepare the csv annotation files

Following [SlowFast](https://github.com/facebookresearch/SlowFast), we also need to prepare the csv annotation files for training, validation, and testing set as `train.csv`, `val.csv`, `test.csv`. The format of the csv file is:

```
path_to_video_1 label_1
path_to_video_2 label_2
path_to_video_3 label_3
...
path_to_video_N label_N
```

The original annotations can be found at the [kinetics website](https://deepmind.com/research/open-source/kinetics), or you can directly use download links of [kinetics-400 annotations](https://storage.googleapis.com/deepmind-media/Datasets/kinetics400.tar.gz) and [kinetics-600 annotations](https://storage.googleapis.com/deepmind-media/Datasets/kinetics600.tar.gz). The official annotations support two different types of files: csv and json. However, both of them don't meet the above format. Therefore, I also provide a python code to transfer json files to the corresponding csv files with correct format. It takes two inputs: the container path of all videos, the path of official json annotation files. The output annotations will be named as 'output_XXX.csv' and located at the same folder. The following command is my example.

```
python kinetics_annotation.py --train_path /home/kaihua/datasets/kinetics-train/ \
    --test_path /home/kaihua/datasets/kinetics-test/ \
    --val_path /home/kaihua/datasets/kinetics-val/ \
    --anno_path /home/kaihua/datasets/kinetics400-anno/
```
