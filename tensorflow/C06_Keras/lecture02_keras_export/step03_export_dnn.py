'''

tensorflow 2.x 전문가용 DNN model 구축
    - tensorflow 2.0 저수준 API
    - Dataset 클래스 이용 : 공급 data 생성
    - foward propagation = linear equation -> predict -> loss
    - backward propagation = 자동 미분계수 -> Weight update
    - loss function , 최적화 , model evaluate API

'''

import tensorflow as tf 
from tensorflow.python.data import Dataset
from tensorflow.keras.layers import Dense , Flatten # layer 추가
from tensorflow.keras import optimizers , losses , metrics
from tensorflow.keras import datasets

# 1. dataset load
mnist = datasets.mnist
(x_train , y_train) , (x_val , y_val) = mnist.load_data()
x_train.shape # (60000, 28, 28)
y_train.shape # (60000,)

# images 2d -> 1d
x_train = x_train.reshape(-1 , 28 * 28 )
x_val = x_val.reshape(-1 , 784)

# images normalize
x_train = x_train/ 255.
x_val =x_val / 255.
x_val[0].shape

# label
#dataset생성
train_ds = Dataset.from_tensor_slices(( x_train , y_train )).shuffle(10000).batch(32)
test_ds= Dataset.from_tensor_slices(( x_val , y_val )).shuffle(10000).batch(32)

# 3. 순방향 step : 연산 -> 예측치 vs 관측치 -> loss
input_shape = (28 , 28)

class Model(tf.keras.Model) :    
    def __init__(self):
        super().__init__() # 부모 생성자 호출
        #DNN Layer
        self.d0 = Flatten(input_shape = input_shape)
        self.d1 = Dense( 128  , activation = 'relu')
        self.d2 = Dense( 64  , activation = 'relu')
        self.d3 = Dense( 10  , activation = 'softmax')
    
    def call(self , inputs) : # method 재정의
        x = self.d0(inputs)
        x = self.d1(x)
        x = self.d2(x)
        return self.d3(x)

#loss
loss = losses.SparseCategoricalCrossentropy(from_logits = True)
# y_true : int / y_pred : probability
import numpy as np

y_true = np.array([0 , 2]) # 정답 : 10 진수
y_pred = np.array([[0.9,0.02,0.08],[0.1,0.1,0.8]]) # 예측치 : 확률

loss(y_true , y_pred)

y_true = np.array([0 , 1]) # 정답 : 10 진수
y_pred = np.array([[0.9,0.02,0.08],[0.1,0.1,0.8]]) # 예측치 : 확률

loss(y_true , y_pred)

# 4. model & optimizer
model = Model()
optimizer = optimizers.Adam()

# 5. model 평가 : loss , accuracy -> 1epoch
train_loss = metrics.Mean() 
train_acc = metrics.SparseCategoricalAccuracy()

val_loss = metrics.Mean() 
val_acc = metrics.SparseCategoricalAccuracy()

# 6. backpropagation : 자동 미분 계수 계산 -> W , b update

@tf.function # 연산 속도 향상
def train_step(images , labels):
    with tf.GradientTape() as tape:
        # 1) 순방향 : loss 계산
        preds = model(images)
        loss_value = loss(labels , preds)
        # 2) 역방향
        grad = tape.gradient(loss_value, model.trainable_variables)
        #print("grad:",grad)
        optimizer.apply_gradients(zip(grad , model.trainable_variables))
    
        # 1epoch -> loss ,accuarcy
        train_loss(loss_value)
        train_acc(labels , preds)

train_step(x_train , y_train)

@tf.function # 연산 속도 향상
def test_step(images , labels):
    # 1) 순방향 : loss 계산
    preds = model(images)
    loss_value = loss(labels , preds)
    
    # 1epoch -> loss ,accuarcy
    val_loss(loss_value)
    val_acc(labels , preds)

# 7. model training
epochs = 10
for epoch in range(epochs):
    #model train
    train_loss.reset_states()
    train_acc.reset_states()
    val_loss.reset_states()
    val_acc.reset_states()
    for images , labels in train_ds :
        train_step(images , labels)

    #model val
    for images , labels in test_ds :
        test_step(images , labels)
    
    form = "epoch = {} , Train loss ={:.6f} , Train Acc = {:.6f}, val loss ={:.6f} , val Acc = {:.6f}"
    print(form.format(epoch+1 , train_loss.result() , train_acc.result() , val_loss.result(), val_acc.result()))

