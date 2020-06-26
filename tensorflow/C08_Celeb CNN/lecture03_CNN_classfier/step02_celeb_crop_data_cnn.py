'''

1. numpy file load
2. CNN layer
3. CNN model
4. model save

'''

import tensorflow as tf
from tensorflow.keras.datasets.cifar10 import load_data
from tensorflow.keras import Sequential
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Conv2D , MaxPooling2D
from tensorflow.keras.layers import Dense , Flatten , Dropout
import numpy as np

# file load
x_train , y_train , x_val , y_val = np.load( file ="C:/ITWILL/6_Tensorflow/workspace/C08_Celeb CNN/lecture03_CNN_classfier/create_file/image_train_test.npy", allow_pickle=True)
x_train.shape # (740, 150, 150, 3)
y_train.shape # (740, 5)

x_val.shape # (250 , 150 , 150 , 3)


# 2. Model
# [5,5,3,32] : kernel_size -> Filter
input_shape = (x_train.shape[1] , x_train.shape[2], x_train.shape[3])

# conv layer1
model = Sequential()
model.add(Conv2D( 32 , kernel_size = (5,5) , input_shape = input_shape , activation = "relu" ))
model.add(MaxPooling2D(pool_size=(3,3), strides = (2,2)))

# conv layer2 : [5,5,32,64]
model.add(Conv2D( 64 , kernel_size = (5,5) , activation = "relu" ))
model.add(MaxPooling2D(pool_size=(3,3), strides = (2,2)))

# Flatten : 3d -> 1d
model.add(Flatten())

# DNN layer
model.add(Dense(256, activation = "relu" ))

# DNN output layer
model.add(Dense(5, activation = "softmax" ))

# 3. Model evnironment setting
model.compile(optimizer = 'adam', loss = 'categorical_crossentropy' , metrics = ['accuracy'])
model.summary()

# 4. model training
model_fit = model.fit( x= x_train, y=y_train ,epochs=15 , verbose=1 , validation_data = (x_val , y_val))

# 5. model evaluation
model.evaluate( x = x_val , y=y_val)



labels = [ "airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]

# 6. model history
model_fit.history.keys()
train_loss = model_fit.history['loss']
train_acc = model_fit.history['accuracy']
val_loss = model_fit.history['val_loss']
val_acc = model_fit.history['val_accuracy']

import matplotlib.pyplot as plt
plt.plot(train_loss , label = 'train loss',color = 'y' )
plt.plot(val_loss , label = 'val loss' , color='r')
plt.legend(loc='best')
plt.show


plt.plot(train_acc , label = 'train_acc loss',color = 'y' )
plt.plot(val_acc , label = 'val val_acc' , color='r')
plt.legend(loc='best')
plt.show

# 7. model save
model.save("./create_file/celeb_CNN_model.h5")















