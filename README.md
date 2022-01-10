# Kinetics-Data-Preprocessing

Kinetics-400 and Kinetics-600 are common video recognition datasets used by popular video understanding projects [SlowFast](https://github.com/facebookresearch/SlowFast) and [PytorchVideo](https://github.com/facebookresearch/pytorchvideo). However, their dataset preparation is too brief. Therefore, this project provides a more detailed instruction for Kinetics data preprocessing.


## Download the raw videos

There are multiple ways to download the raw videos of Kinetics-400 and Kinetics-600. Here I list two common choices that I tested to be simple and effective: 

1. Download the videos via the official [scripts](https://github.com/activitynet/ActivityNet/tree/master/Crawler/Kinetics). However, I noticed that this option is much slow, so I personally recommend the next choice.

2. Download the compressed videos from the Common Visual Data Foundation Servers following the [repository](https://github.com/cvdfoundation/kinetics-dataset), which is much faster as they organized 650,000 independent video clips into several compressed files.


## Resize the videos


## Prepare the csv annotation files
