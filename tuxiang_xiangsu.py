#!usr/bin/env python
# -*- coding:UTF-8 -*-
#@author by blue
#time 2018
#----------------------

import cv2
import numpy as np

img = cv2.imread('/home/zhagminghai/zmh/download/images/images13.jpg')
size = img.shape
print size
print img
cv2.imshow("image",img)
box = (100, 100, 150, 230)
print box
