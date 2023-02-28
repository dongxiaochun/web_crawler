# -*- coding:utf8 -*-
# 此为更新视频名字的脚本，算法测试集的视频均可以用此脚本更新
import os

# video_dir = '/data/mining/huoqiu/data/videos/垂直管道2/'
# video_dir_out = '/data/mining/huoqiu/data/videos/垂直管道1/'

video_dir = 'd:\\workbase\\测试视频'  # 视频文件所在路径
listdir = os.listdir(video_dir)
print(listdir)
# 将视频名字按数字排序，按照自己需求决定是否执行，不需要执行时请注掉；需要执行时也请按照自己实际情况更改函数中int(x[5:-4])值
# 例如一个文件夹下有以下几个文件：[皮带大颗粒5.dav,皮带大颗粒1.dav,皮带大颗粒4.dav],排序后为[皮带大颗粒1.dav,皮带大颗粒4.dav,皮带大颗粒5.dav]
#listdir.sort(key=lambda x: int(x[5:-4])) # 将文件名按数字排序,请按自己需要更改

# 更新视频文件名
i = 1
for file_name in listdir:

    houzhui = file_name.split(".")[-1]
    file_name_new = "霍邱铁矿_皮带大颗粒_" + file_name.split(".")[-2] + "_正样本" + str(i) + ".mp4"
    print("file_name_new"+file_name_new)
    i = i + 1
    print(file_name)
    os.rename(video_dir+"\\" + file_name, video_dir+"\\" + file_name_new)  # 将视频名字从file_name，更新成file_name_new

