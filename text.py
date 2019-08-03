#the code can cometrue image prossising smooth
# date 2017.9.25
#author : minghai zhang

#!usr/bin/env python
# -*- coding: UTF-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/home/zhagminghai/zmh/download/images/images.jpg')
blur = cv2.blur(img,(3,3))
edges = cv2.Canny(blur,100,200)
plt.subplot(131),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(edges),plt.title('canny')
plt.xticks([]), plt.yticks([])
plt.show()
