#!usr/bin/env python
# -*- coding: UTF-8 -*-
#@author by blue
#time 2018
#----------------------

import numpy as np
import cv2

img = cv2.imread('/home/zhagminghai/zmh/workbook/opencv/images9.jpg')
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'opencv',(10,200),font,2,(255,255,255),2)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()