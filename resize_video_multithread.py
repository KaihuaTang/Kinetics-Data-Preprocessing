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

class myThread (threading.Thread):
    def __init__(self, threadID, name, video_list):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.video_list = video_list
    def run(self):
        print("Start Thread: " + self.name)
        resize_videos(self.name, self.video_list)
        print("Exit Thread: " + self.name)


def resize_videos(threadName, video_list):
    for item in video_list:
        if not os.path.isfile(item):
            print("%s-%s: %s" % (threadName, time.ctime(time.time()), 'Cannot Find: ' + item))
            continue

        try:
            clip = mp.VideoFileClip(item)
            w, h = clip.size
            if w > h:
                clip_resized = clip.resize(height=TARGET_SIZE)
            else:
                clip_resized = clip.resize(width=TARGET_SIZE)
        except:
            print("%s-%s: %s" % (threadName, time.ctime(time.time()), 'Fail to process: ' + item))


        try:
            clip_resized.write_videofile(item, logger=None)
            print("%s-%s: %s" % (threadName, time.ctime(time.time()), item + ' is resized to ' + str(clip_resized.size)))
        except:
            print("%s-%s: %s" % (threadName, time.ctime(time.time()), 'Fail to re-write: ' + item))


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
thr_14 = len(video_list) // 4
thr_24 = len(video_list) // 4 * 2
thr_34 = len(video_list) // 4 * 3
video_sublist1 = video_list[:thr_14]
video_sublist2 = video_list[thr_14:thr_24]
video_sublist3 = video_list[thr_24:thr_34]
video_sublist4 = video_list[thr_34:]


# create new threads
thread1 = myThread(1, "Thread-1", video_sublist1)
thread2 = myThread(2, "Thread-2", video_sublist2)
thread3 = myThread(3, "Thread-3", video_sublist3)
thread4 = myThread(4, "Thread-4", video_sublist4)

# start threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
print("Completed!")