'''

- Keras CNN model + cifar10 

1. image dataset load
2. image preprocessing : 실수형 , 정규화 , one-hot-encoding
3. Keras Model
4. Model evaluate
5. Model history

'''

# keras dataset 적용
import tensorflow as tf
from tensorflow.keras.datasets.cifar10 import load_data
from tensorflow.keras import Sequential
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Conv2D , MaxPooling2D
from tensorflow.keras.layers import Dense , Flatten , Dropout


# 1. dataset load
(x_train , y_train ) , (x_val , y_val) = load_data()
x_train.shape # (50000, 32, 32, 3)
y_train.shape # (50000, 1)

# image 전처리 : 실수형 -> 정규화
x_train[0] # 0 ~ 255 : 정수형
x_train = x_train.astype("float32")
x_val = x_val.astype("float32")

# 정규화
x_train = x_train / 255
x_val = x_val / 255
x_train[0]

# label 전처리 : one-hot
y_train = to_categorical(y_train)
y_val = to_categorical(y_val)

# 2. Model
# [5,5,3,32] : kernel_size -> Filter
input_shape = (x_train.shape[1] , x_train.shape[2], x_train.shape[3])

# conv layer1
model = Sequential()
model.add(Conv2D( 32 , kernel_size = (5,5) , input_shape = input_shape , activation = "relu" ))
model.add(MaxPooling2D(pool_size=(3,3), strides = (2,2)))
model.add(Dropout(0.2))

# conv layer2 : [5,5,32,64]
model.add(Conv2D( 64 , kernel_size = (5,5) , activation = "relu" ))
model.add(MaxPooling2D(pool_size=(3,3), strides = (2,2)))
model.add(Dropout(0.2))

# Flatten : 3d -> 1d
model.add(Flatten())

# DNN layer
model.add(Dense(64, activation = "relu" ))

# DNN output layer
model.add(Dense(10, activation = "softmax" ))

# 3. Model evnironment setting
model.compile(optimizer = 'adam', loss = 'categorical_crossentropy' , metrics = ['accuracy'])
model.summary()

# 4. model training
model_fit = model.fit( x= x_train, y=y_train , batch_size = 100 ,epochs=10 , verbose=1 , validation_data = (x_val , y_val))

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

# 7. model test ( new data set )
from sklearn.metrics import classification_report

import numpy as np
idx = np.random.choice(a = x_val.shape[0] ,size = 100 , replace = False)
x_test = x_val[idx] # new dataset images
y_test = y_val[idx] # new dataset labels

y_pred = model.predict(x_test)
y_pred = np.argmax(y_pred , 1)
y_true = np.argmax(y_test , 1)

report = classification_report(y_true, y_pred  )
print(report)

# 성공 여부
for i in range(100):
    if y_true[i] == y_pred[i]:
        print("success : " , labels[y_true[i]])
    else: 
        print("fail : real ({}) -> pred({})".format(labels[y_true[i]] ,labels[ y_pred[i]]))










