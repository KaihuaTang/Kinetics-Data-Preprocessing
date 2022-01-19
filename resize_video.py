import moviepy.editor as mp
import threading
import time
import os
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument('--size', default=256, type=int)
parser.add_argument('--path', default=None, type=str)
args = parser.parse_args()

TARGET_SIZE = args.size
MAIN_PATH = args.path

print('Resize all mp4 videos in {} to the short edge size of {}'.format(MAIN_PATH, TARGET_SIZE))
time.sleep(3)


def resize_videos(video_list):
    total_num = len(video_list)
    for i, item in enumerate(video_list):
        progress = str(i) + '/' + str(total_num)

        if not os.path.isfile(item):
            print("%s-%s: %s" % (progress, time.ctime(time.time()), 'Cannot Find: ' + item))
            continue

        try:
            clip = mp.VideoFileClip(item)
            w, h = clip.size
            if w > h:
                clip_resized = clip.resize(height=TARGET_SIZE)
            else:
                clip_resized = clip.resize(width=TARGET_SIZE)

            clip_resized.write_videofile(item, logger=None)
            clip_resized.close()
            clip.close()
            print("%s-%s: %s" % (progress, time.ctime(time.time()), item + ' is resized to ' + str(clip_resized.size)))
            
        except Exception as e:
            print("%s-%s: %s Due to %s" % (threadName, time.ctime(time.time()), 'Fail to process: ' + item, e))


# iteratively search all mp4 videos within the current folder or sub-folders
def get_video_list(main_path):
    video_list = []
    for file in os.listdir(main_path):
        if file.endswith('mp4'):
            video_list.append(os.path.join(main_path, file))
        elif os.path.isdir(os.path.join(main_path, file)):
            child_list = get_video_list(os.path.join(main_path, file))
            video_list = video_list + child_list
        else:
            pass
    return video_list


# get video lists
video_list = get_video_list(MAIN_PATH)

# resize all videos
resize_videos(video_list)
print("Completed!")
