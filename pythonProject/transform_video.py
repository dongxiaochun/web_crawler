# -*- coding:utf8 -*-
import os
import cv2
import glob

# video_dir = '/data/mining/huoqiu/data/videos/垂直管道2/'
# video_dir_out = '/data/mining/huoqiu/data/videos/垂直管道1/'

# video_dir = '/mnt/d/项目/煤矿/huoqiu/raw'
# video_dir_out = '/mnt/d/项目/煤矿/huoqiu/after'

video_dir = 'd:\\workbase\\测试视频'
video_dir_out = 'd:\\workbase\\测试视频test\\'

width, height = 3840, 2160
fps = 50
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
print(fourcc)

# 当视频输出文件目录不存在时，创建目录
if not os.path.exists(video_dir_out):
    print("ddd")
    os.makedirs(video_dir_out)

for video_file in glob.glob(video_dir + '/*.mp4'):
    videoCapture = cv2.VideoCapture(video_file)
    video_out = video_dir_out + video_file.split('\\')[-1]
    print(video_out)

    out = cv2.VideoWriter(video_out, fourcc, fps, (width, height), True)
    success, frame = videoCapture.read()
    for i in range(fps * 60):
        out.write(frame)

    while success:
        success, frame = videoCapture.read()
        out.write(frame)
    out.release()
    print("111")
