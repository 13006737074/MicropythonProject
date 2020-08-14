import cv2 as cv
import numpy as np

vc = cv.VideoCapture('1.avi')#打开视频
c = 0#累计帧数

timeF = 50#隔5帧截一次图，数字越小，播放越细腻


def binary_image(image):#将图像处理为二值化的程序
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)  #把输入图像灰度化
    h, w =gray.shape[:2]
    m = np.reshape(gray, [1,w*h])
    mean = m.sum()/(w*h)
    print("mean:",mean)
    ret, binary =  cv.threshold(gray, mean, 255, cv.THRESH_BINARY)
    return binary


def access_pixels(image):#相反操作
    height, width, channels = image.shape
    print("width:%s,height:%s,channels:%s" % (width, height, channels))
 
    for row in range(height):
        for list in range(width):
            for c in range(channels):
                pv = image[row, list, c]
                image[row, list, c] = 255 - pv
    return image


if vc.isOpened():  # 判断是否正常打开
    rval, frame = vc.read()
else:
    rval = False

print(rval)

while rval:  # 循环读取视频帧
    rval, frame = vc.read()
    if (c % timeF == 0):  # 每隔timeF帧进行存储操作
        frame = binary_image(frame)#二值化
        frame = cv.bitwise_not(frame)#反相,根据视频内容来定需不需要反相
        frame = cv.resize(frame,(88,64))#调整尺寸
        cv.imwrite('after/' + str(c) + '.pbm',frame)#保存

    c = c + 1
    cv.waitKey(0)

