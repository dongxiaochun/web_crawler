import cv2
import os
import random
import glob
video_dir = 'd:\\workbase\\测试视频'

VideoWriter = cv2.VideoWriter("merge .avi", cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'), 50, (3280, 2130))
mp4list = glob.glob(video_dir + '/*.mp4')

for mp4file in mp4list:
    capture = cv2.VideoCapture("../{}".format(mp4file))
    fps = capture.get(cv2.CAP_PROP_FPS)
    if capture.isOpened():
        i = 0
        # 每隔视频提取10秒
        while i < fps * 10:
            i += 1
            ret, prev = capture.read()
            if ret:
                if fps == 24:
                    VideoWriter.write(prev)
                else:

                    # 这里可以写一些丢帧数的条件例如elif fps%2==0
                    VideoWriter.write(prev)
            else:
                break
VideoWriter.release()
cv2.destroyAllWindows()
