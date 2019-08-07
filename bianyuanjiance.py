#!usr/bin/env python
# -*- coding: UTF-8 -*-
#@author by blue
#time 2018
#----------------------

import cv2
import numpy as np
# from matplotlib import pyplot as plt

# img=cv2.imread('/home/zhagminghai/zmh/download/images/images13.jpg',0)
# cv2.imshow('raw image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# edges = cv2.Canny(img,100,200)
# plt.subplot(121)
# plt.imshow(img,cmap='gray')
# plt.title('oringal image')
# plt.xticks([])
# plt.yticks([])
# plt.subplot(122)
# plt.imshow(edges,cmap='gray')
# plt.title('edge image')
# plt.xticks([])
# plt.yticks([])
#
# plt.show()
#==========================================================================

img=cv2.imread('/home/zhagminghai/zmh/download/maomaochong/1.jpg')
cv2.imshow('raw image', img)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray image', img_gray)
ret,thresh = cv2.threshold(img_gray,127,225,0)
image,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img1 = cv2.drawContours(img,contours,-1,(0,225,0),2)
cv2.imshow('contours image', img1)
cv2.imwrite('/home/zhagminghai/zmh/download/maomaochong/result/1bianyuanjiance.jpg',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

