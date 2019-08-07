#!usr/bin/env python
# -*- coding: UTF-8 -*-
#@author by blue
#time 2018
#----------------------

#实现窗口打创建，大小调整，显示图片功能。

import numpy as np
import cv2

img = cv2.imread('/home/zhagminghai/zmh/workbook/opencv/images9.jpg')
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.destroyAllWindows()
cv2.waitKey(0)
cv2.destroyAllWindows()