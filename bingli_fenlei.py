#!usr/bin/env python
# -*- coding: UTF-8 -*-
#@author by blue
#time 2018
#----------------------

import tensorflow as tf
from matplotlib import pyplot as plt
import numpy as np
import random

def generate(sample_size,mean,cov,diff,regression):
    num_classes=2
    sample_per_class=int(sample_size/2)

    X0 = np.random.multivariate_normal(mean,cov,sample_per_class)
    Y0 = np.zeros(sample_per_class)

    for ci,d in enumerate(diff):
        X1 = np.random.multivariate_normal(mean+d,cov,sample_per_class)
        Y1 = (ci+1)*np.ones(sample_per_class)

        X0 = np.concatenate((X0,X1))
        Y0 = np.concatenate((Y0,Y1))

    if regression==False:
        class_ind = [Y==class_number for class_number in range(num_classes)]
        Y = np.ndarray(np.hstack(class_ind), dtype=np.float32)
    X, Y = random.shuffle(X0,Y0)
    return X,Y

np.random.seed(10)
num_classes = 2
mean = np.random.randn(num_classes)
cov = np.eye(num_classes)
X,Y = generate(1000, mean, cov, [3.0], True)
colors = ['r'if l == 0 else 'b' for l in Y[:]]
plt.scatter(X[:,0],X[:,1], c=colors)
plt.xlabel("Scatter age ( in yrs)")
plt.ylabel("Tumor size (in cm)")
plt.show()
lab_dim = 1

