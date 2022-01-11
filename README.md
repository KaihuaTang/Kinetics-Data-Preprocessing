# Kinetics-Data-Preprocessing

Kinetics-400 and Kinetics-600 are common video recognition datasets used by popular video understanding projects like [SlowFast](https://github.com/facebookresearch/SlowFast) or [PytorchVideo](https://github.com/facebookresearch/pytorchvideo). However, their instruction of dataset preparation is too brief. Therefore, this project provides a more detailed instruction for Kinetics-400/-600 data preprocessing.


## Download the raw videos

There are multiple ways to download the raw videos of Kinetics-400 and Kinetics-600. Here, I mainly list two common choices that I tested to be simple and effective: 

1. Download the videos via the official [scripts](https://github.com/activitynet/ActivityNet/tree/master/Crawler/Kinetics). However, I noticed that this option is very slow, so I personally recommend the next choice.

2. Download the compressed videos from the Common Visual Data Foundation Servers following the [repository](https://github.com/cvdfoundation/kinetics-dataset), which is much faster as they organized 650,000 independent video clips into several compressed files.


## Resize the videos

The common data preprocessing of Kinetics requires all videos to be resized to the short edge size of 256. Therefore, I use the [moviepy package](https://zulko.github.io/moviepy/) to do so. The package can be easily installed by the following command:

```
pip install moviepy
```

Then, you can use the resize_video.py to resize all the videos within the given folder by following command:

```
python resize_video.py --size 256 --path YOUR_VIDEO_CONTAINER
```

IMPORTANT! Note that the resize_video.py will replace the original mp4 files. If you want to keep the original files, please make copys before resizing videos.

## Prepare the csv annotation files
