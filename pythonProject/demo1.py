
import cv2
video = cv2.VideoCapture("皮带大颗粒10.mp4")
frame_Num=1
while video.isOpened():
    retval, image = video.read()
    cv2.namedWindow("video", 0)
    cv2.resizeWindow("video", 1024, 580)
    if retval == True:
        cv2.imshow("video", image)
    else:
        break
    key = cv2.waitKey(10)# 循环等待用户输入，没有输入就继续循环10ms执行等待
    if key == 32:
        cv2.waitKey(0)#用户按空格键，暂停，无限等
        continue
    frame_Num+=1
    if key == 27:#按esc退出
        break
video.release()

