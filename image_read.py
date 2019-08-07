#!usr/bin/env python
# -*- coding: UTF-8 -*-
#@author by blue
#time 2018.02.02
#----------------------

#程序实现图片打读入，显示，保存功能。

import numpy as np
import cv2

#load an  color image in grayscale
img = cv2.imread('/home/zhagminghai/zmh/workbook/opencv/images9.jpg')
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

