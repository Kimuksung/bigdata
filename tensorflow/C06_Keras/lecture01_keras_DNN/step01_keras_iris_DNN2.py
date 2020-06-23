'''

    - Tensorflow 2.x Keras + iris
    - Keras : Model 생성을 위한 고수준 API
    - Y 변수 : integer(10 진수)
    loss = 'sparse_categorical_crossentropy'
    metrics - ['sparse_categorical_accuracy']

'''

import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import minmax_scale 
from tensorflow.keras.utils import to_categorical # Y 변수 전처리
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense 
from tensorflow.keras.models import load_model
from sklearn.metrics import accuracy_score

# x, y data
iris = load_iris() 
x_data = iris.data

X_data = minmax_scale(x_data)
X_data.shape # (150, 4)

y_data = iris.target
y_data = y_data.reshape(-1,1)

'''
y_data = to_categorical(y_data)
y_data.shape # (150, 3)
'''

x_train , x_val , y_train , y_val = train_test_split( x_data , y_data)
x_train.shape # (112, 4)

# 2. Keras Model 생성
model = Sequential()

# 3. model layer
model.add(Dense( 12  , input_shape = (4,) , activation = 'relu')) # hidden layer = [ 4 , 12]
model.add(Dense( 6  , activation = 'relu'))  # hidden layer = [ 12 , 6 ]
model.add(Dense( 3 , activation = 'softmax')) # output layer = [ 6 , 3]

'''
model.add(Dense( node 수 , input_shape , activation = 'relu' / 'softmax' / 'sigmoid'))
model.add(Dense( node 수 , activation = 'relu' / 'softmax' / 'sigmoid'))
model.add(Dense( node 수 , activation = 'relu' / 'softmax' / 'sigmoid'))
'''

# 4. model compile
#model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy' , metrics = ['sparse_categorical_accuracy'])
#model.compile(optimizer = 'adam', loss = 'categorical_crossentropy' , metrics = ['accuracy'])

# class 변경
from tensorflow.keras import optimizers , losses , metrics
model.compile(optimizer = optimizers.Adam()
              , loss = losses.SparseCategoricalCrossentropy(from_logits = True)
              , metrics = [metrics.SparseCategoricalAccuracy()] )

# layer check
model.summary()

# 5. model training
model.fit( x= x_train, y=y_train , epochs=300 , verbose=1 , validation_data = (x_val , y_val))

# 6. model evaluation
model.evaluate( x = x_val , y=y_val)

y_pred = model.predict(x_val)

















