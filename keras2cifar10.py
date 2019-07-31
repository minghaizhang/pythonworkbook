#!usr/bin/enev python
# -*- coding:UTF-8 -*- 
# author@blue 
#time:2019.06.14

from __future__ import print_function
import keras
from keras.datasets import cifar10
from keras.preprocessing.image import ImageDataGenerator
from keras.models import  Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D

import os

batch_size = 32 
num_classes = 10
epoch = 100
data_augmentation = True
num_predictationds =  20
save_dir = os.path.join(os.getcwd(), 'save_models')
model_name = 'keras_cifar10_trained_model.h5'

(x_train, y_train), (x_test, y_test) = cifar10.load_data()
print('x_train shape:',x_train.shape)
print(x_train.shape[0],'train samples')
print(x_test.shape[0], 'test samples')


y_train = keras.utils.to_categorical(y_train,num_classes)
y_test = keras.utils.to_categorical(y_test,num_classes)

model = Sequential()
model.add(Conv2D(32,(3, 3),padding='same',
                 input_shape=x_train.shape[1:]))
model.add(Activatation('relu'))
model.add(Conv2D(32, (3,3)))
model.add(Activatation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Conv2D(64,(3,3),padding='same'))
model.add(Activation('relu'))
model.add(Conv2D(64,(3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model,ass(Dense(num_classes))
model.add(Activation('softmax'))

opt = kears.optimizers.rmsprop(lr=0.0001,decay=1e-6)

model.compile(loss='categorical_crossentropy',
              optimizer=opt,
              metrics=['accuracy'])

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /=255
x_test /=255

if not data_augmentation:
    print('Not using data augmentation.')
    model.fit(x_train,y_train,
              batch_size=batch_size,
              epochs=epochs,
              validation_data=(x_test,y_test),
              shuffle=True)

else :
    print('using real-time data augmentation.')
    datagen = ImageDataGenerator(
        featurewise_centure=False,
        samplewise_center=Flase,
        featurewise_std_normalization=False,
        samplewise_std_normalization=False,
        zca_epsilon=1e-06,
        rotation_range=0.1,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.,
        zoom_range=0.,
        channle_shift_range=0.,
        fill_mode='nearst',
        cval=0.,
        horization_filp=True,
        vertical_flip=False,
        rescale=None,
        preprocessing_functuion=None,
        data_format=None,
        validation_split=0.0
    )

    datagen.fit(x_train)

    model.fit_generator(datagen.flow(x_train,y_train,
                                     batch_size=batch_size),
                        epochs=epochs,
                        validation_data=(x_test,y_test),
                        workers=4
                        )

if not os.path.isdir(save_dir):
    os.makedirs(save_dir)
model_path = os.path.join(save_dir,model_name)
model.save(model_path)
print('Save trained model at %s' %model_path)

scores  = model.evaluate(x_test,y_test,verbose=1)
print('test loss:',scores[0])
print('tset accuracy:',scorse[1])


print ('ok im fine')
