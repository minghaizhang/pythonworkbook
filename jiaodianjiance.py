#!usr/bin/env python
# -*- coding: UTF-8 -*-
#@author by blue
#time 2018
#----------------------

import cv2
import numpy as np

filename = '/home/zhagminghai/zmh/download/maomaochong/1.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)

#输入图像必须是float32,最后一个参数在0.04-0.05之间
dst = cv2.cornerHarris(gray,2,3,0.04)

#result is dilated for making the corners ,not important
dst = cv2.dilate(dst,None)
#threshold for an optimal value ,it may vary depending on the image

img[dst>0.01*dst.max()] = [0,0,225]

cv2.imshow('dst',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
