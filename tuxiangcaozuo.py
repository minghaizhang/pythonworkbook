#!usr/bin/env python
# -*- coding: UTF-8 -*-
#@author by blue
#time 2018
#----------------------

import cv2
import numpy as np

img = cv2.imread('/home/zhagminghai/zmh/download/images/images.jpg')
px = img[150,150]
print px

blue = img[150,150,0]
print blue

imred = img.itemset((10,10,2),100)
print imred
print img.shape
print (img.size)
print (img.dtype)
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))
print img

