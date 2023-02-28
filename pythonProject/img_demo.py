import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 1 读取图像
img = cv.imread('logo.png', 1)
# 2 显示图像
# 2.1 利用opencv展示图像
cv.imshow('image', img)

cv.imwrite('messigray.png', img)

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 1 创建一个空白的图像
img = np.zeros((512, 512, 3), np.uint8)
# 2 绘制图形
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
cv.circle(img, (447, 63), 63, (0, 0, 255), -1)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv.LINE_AA)

cv.imwrite('messigray1.png', img)

import cv2 as cv
import matplotlib.pyplot as plt

# 1 读取图像
img1 = cv.imread("logo.png")
img2 = cv.imread("logo.jpg")

# 2 加法操作
img3 = cv.add(img1, img2)

cv.imwrite('messigray1.png', img3)
