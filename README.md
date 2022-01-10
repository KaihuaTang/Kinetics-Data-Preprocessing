# Kinetics-Data-Preprocessing

Kinetics-400 and Kinetics-600 are common video recognition datasets used by popular video understanding projects like [SlowFast](https://github.com/facebookresearch/SlowFast) or [PytorchVideo](https://github.com/facebookresearch/pytorchvideo). However, their instruction of dataset preparation is too brief. Therefore, this project provides a more detailed instruction for Kinetics-400/-600 data preprocessing.


## Download the raw videos

There are multiple ways to download the raw videos of Kinetics-400 and Kinetics-600. Here, I mainly list two common choices that I tested to be simple and effective: 

1. Download the videos via the official [scripts](https://github.com/activitynet/ActivityNet/tree/master/Crawler/Kinetics). However, I noticed that this option is very slow, so I personally recommend the next choice.

2. Download the compressed videos from the Common Visual Data Foundation Servers following the [repository](https://github.com/cvdfoundation/kinetics-dataset), which is much faster as they organized 650,000 independent video clips into several compressed files.


## Resize the videos

use moviepy package 

To be continued

```
pip install moviepy
```

## Prepare the csv annotation files
