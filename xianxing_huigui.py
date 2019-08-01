#!usr/bin/env python
# -*- coding: UTF-8 -*-
#@author by blue
#time 2018
#----------------------

import tensorflow as tf
import numpy as np

# generate fake data
train_X = np.random.rand(100)
train_X2 = np.random.rand(100)
train_Y = train_X2 + train_X

inputdict = {
    'x':tf.placeholder("float"),
    'x2':tf.placeholder("float"),
    'y':tf.placeholder("float")
}

#model parameters
W = tf.Variable(tf.random_normal([1]),name="weight")
b = tf.Variable(tf.zeros([1]),name="bias")

W2 = tf.Variable(tf.random_normal([1]),name="weight2")
b2= tf.Variable(tf.zeros([1]),name="bias2")

#前向结构
z = tf.multiply(inputdict['x'], W) + b + tf.multiply(inputdict['x2'],W2) + b2

#反向优化
cost = tf.reduce_mean(tf.square(inputdict['y'] - z))
learning_rate = 0.01
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

#初始化变量
init = tf.global_variables_initializer()

#参数设置
training_epochs = 2000
display_step = 20

# 启动训练
with tf.Session() as sess:
    sess.run(init)

    for epoch in range(training_epochs):
        for i in range(100):
            sess.run(optimizer, feed_dict={inputdict['x']: train_X,inputdict['x2']: train_X2[i],inputdict['y']: train_Y[i]})

        if epoch % display_step == 0:
            loss = sess.run(cost, feed_dict={inputdict['x']: train_X[i],inputdict['x2']: train_X2[i],inputdict['y']: train_Y[i]})
            print ("Epoch:", epoch+1, "cost=", loss, "W=",sess.run(W),"b=", 'W2',sess.run(b), sess.run(W2), "b=",sess.run(b2))



    print(" finished!")
    print("w=",sess.run(W),"b=",sess.run(b),"w2=",sess.run(W2), "b2=",sess.run(b2))

    xxx = np.random.rand(100)
    xxx2 = np.random.rand(100)
    for i in range(len(xxx)):
        ret = sess.run(z,feed_dict={inputdict['x']: xxx[i],inputdict['x2']: xxx2[i]})
        print('xxx',xxx[i],'xxx2',xxx2[i], '=', ret,xxx[i] + xxx2[i])


print("finished! ===>>")