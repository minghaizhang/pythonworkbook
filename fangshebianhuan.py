#!usr/bin/env python
# -*- coding: UTF-8 -*-
#@author by blue
#time 2018
#----------------------

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('/home/zhagminghai/zmh/download/images/images30.png')
rows,cols,ch = img.shape

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2)

dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('1',img)
cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
