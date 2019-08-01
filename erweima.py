#!usr/bin/env python
# -*- coding: UTF-8 -*-
#@author blue
#---------------------

import qrcode

img = qrcode.make("Pattern recognition laboratory plants--Sedum x rubrotinctum Clausen(虹之玉)!")
img.get_image().show
img.save('/media/zhagminghai/32E3-FE21/zhiwutupian/plant.png')
