# -*- coding:utf8 -*-
import os
import cv2
import glob

video_dir = '/data/mining/huoqiu/data/videos/垂直管道2/' 
video_dir_out = '/data/mining/huoqiu/data/videos/垂直管道1/' 
width,height = 1280,720
fps = 25
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

if not os.path.exists(video_dir_out):
    os.makedirs(video_dir_out)

for video_file in  glob.glob(video_dir +'/*.mp4'):
    videoCapture = cv2.VideoCapture(video_file)
    video_out = video_dir_out + video_file.split('/')[-1]

    out = cv2.VideoWriter(video_out,fourcc, fps, (width,height),True)
    success, frame = videoCapture.read()
    for i in range(fps*60):
        out.write(frame)

    while success:
        success,frame = videoCapture.read()
        out.write(frame)
    out.release()