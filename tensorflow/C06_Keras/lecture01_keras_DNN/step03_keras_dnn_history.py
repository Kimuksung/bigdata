'''

    Tensorflow 2.0 Keras + MNIST( 0 ~ 9 ) + flatten layer


first case : one dimesion (28 x 28 ) -> 768

second case : 28 x 28 -> Flatten

'''

import tensorflow as tf
from tensorflow.keras.utils import to_categorical # Y 변수 전처리
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense , Flatten
from tensorflow.keras.models import load_model
from sklearn.metrics import accuracy_score
from tensorflow.keras.datasets.mnist import load_data

# x, y data
(x_train , y_train) , ( x_val , y_val) = load_data() 
x_train.shape # (60000, 28, 28)
y_train.shape # (60000,)

# data normalize & 2d
x_train = x_train / 255.
x_val = x_val / 255.
x_val.shape # (10000, 28, 28)

#x_train = x_train.reshape(-1,784)
#x_val = x_val.reshape(-1,784)


y_train = to_categorical(y_train)
y_val = to_categorical(y_val)
y_val.shape

# 2. Keras Model 생성
model = Sequential()

# 3. model layer
# =============================================================================
# model.add(Dense( 128  , input_shape = (784,) , activation = 'relu')) # hidden layer = [ 784 , 128]
# model.add(Dense( 64  , activation = 'relu'))  # hidden layer = [ 128 , 64 ]
# model.add(Dense( 32  , activation = 'relu'))  # hidden layer = [ 64 , 32 ]
# model.add(Dense( 10 , activation = 'softmax')) # output layer = [ 32 , 3]
# =============================================================================
input_shape = (28 , 28)
model.add(Flatten(input_shape = input_shape )) # flatten layer
model.add(Dense( 128  , activation = 'relu')) # hidden layer = [ 784 , 128]
model.add(Dense( 64  , activation = 'relu'))  # hidden layer = [ 128 , 64 ]
model.add(Dense( 32  , activation = 'relu'))  # hidden layer = [ 64 , 32 ]
model.add(Dense( 10 , activation = 'softmax')) # output layer = [ 32 , 3]


# 4. model compile
model.compile(optimizer = 'adam', loss = 'categorical_crossentropy' , metrics = ['accuracy'])

# layer check
model.summary()

# 5. model training
model_fit = model.fit( x= x_train, y=y_train , epochs=15 , verbose=1 , validation_data = (x_val , y_val))

# 5.5 model history
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



















