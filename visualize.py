from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np
from keras.models import Sequential
from keras.layers import *
import pylab
from keras.models import Model
from scipy.misc import imsave
model = VGG16(weights='imagenet', include_top=False)

img_path = '/Users/gxy/Desktop/CS/CNN/Project/keras/neural_transfer/pic/img/Taylor2.jpeg'
img = image.load_img(img_path)
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

features = model.predict(x)
pic=features[0,:,:,128]
# pic = np.clip(pic, 0, 255).astype('uint8')
pylab.imshow(pic)
pylab.gray()
pylab.show()

# img_path = '/Users/gxy/Desktop/CS/CNN/Project/keras/Kexamples2.0/pic/mask/cat10mask.png'
# img = image.load_img(img_path)
# x = image.img_to_array(img)
# x = np.ones_like(x) * (x > 0)
# pass
# input = Input(shape=x.shape)
# y = MaxPooling2D((2, 2), strides=(2, 2), name='block1_pool')(input)
# y = MaxPooling2D((2, 2), strides=(2, 2), name='block2_pool')(y)
# y = MaxPooling2D((2, 2), strides=(2, 2), name='block3_pool')(y)
# y = MaxPooling2D((2, 2), strides=(2, 2), name='block4_pool')(y)
# output = MaxPooling2D((2, 2), strides=(2, 2), name='block3_pool')(y)
# model = Model(inputs=input, outputs=output)
# x = np.expand_dims(x, axis=0)
# features = model.predict(x)
# pylab.imshow(features[0,:,:,1])
# pylab.gray()
# pylab.show()
# imsave('mask1.png', features[0,:,:,1])
