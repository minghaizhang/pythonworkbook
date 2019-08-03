#!usr/bin/env python
# -*- coding: UTF-8 -*-
#@author by blue
#time 2018
#----------------------

import cv2
import numpy as np

filename = '/home/zhagminghai/zmh/download/images/images29.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray,None)

img = cv2.drawKeypoints(gray,kp,img)

cv2.imwrite('sift_keypoint.jpg',img)
cv2.imshow('sift_keypoint.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
