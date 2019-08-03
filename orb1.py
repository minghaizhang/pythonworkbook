#!usr/bin/env python
# -*- coding: UTF-8 -*-
#@author by blue
#time 2018
#----------------------

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/home/zhagminghai/zmh/download/images/images.jpg',0)
orb = cv2.ORB_create()
kp = orb.detect(img,None)
print kp
kp,des = orb.compute(img,kp)
img2 = cv2.drawKeypoints(img, kp,img, color=(0,255,0), flags=0)
plt.imshow(img2),plt.show()