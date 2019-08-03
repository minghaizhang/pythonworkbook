#!usr/bin/env python
# -*- coding: UTF-8 -*-
#@author by blue
#time 2018
#----------------------

# capture an video and show on a screen

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    #capture frame by frame
    ret,frame = cap.read()
    #our operation on the frame come here
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(30):
        break
#when everying done ,release the capture
cap.release()
cv2.destroyAllWindows()



#=========================================================
import cv2
vc = cv2.VideoCapture('driveway-320x240.avi') #读入视频文件
c=0
rval=vc.isOpened()
#timeF = 1  #视频帧计数间隔频率
while rval:   #循环读取视频帧
    c = c + 1
    rval, frame = vc.read()
#    if(c%timeF == 0): #每隔timeF帧进行存储操作
#        cv2.imwrite('smallVideo/smallVideo'+str(c) + '.jpg', frame) #存储为图像
    if rval:
        cv2.imwrite('driveway-320x240/driveway-320x240'+str(c).zfill(8) + '.jpg', frame) #存储为图像
        cv2.waitKey(1)
    else:
        break
vc.release()

#==========================================================
