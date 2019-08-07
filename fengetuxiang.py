#!usr/bin/env python
# -*- coding: UTF-8 -*-
#@author by blue
#time 2018
#----------------------

import cv2
import numpy as np


img = cv2.imread('/home/zhagminghai/zmh/download/images/images9.jpg')
cv2.imshow('orginal_image',img)
crop_img = img[150:200, 120:300]
cv2.imshow('crop_img',crop_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
