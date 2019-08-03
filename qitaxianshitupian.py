#!usr/bin/env python
# -*- coding: UTF-8 -*-
#@author by blue
#time 2018
#----------------------

#othor ways to show an image

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('/home/zhagminghai/zmh/workbook/opencv/images9.jpg')
plt.imshow(img,cmap = 'gray',interpolation = 'bicubic')
plt.xticks([],plt.yticks([])) #to hide tick values on x and y axis
plt.show()

#image is GBR not show as RGB,so looks have some terrible#------------
