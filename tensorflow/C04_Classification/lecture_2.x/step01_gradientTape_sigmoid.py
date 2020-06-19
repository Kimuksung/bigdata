"""

    - GradientTape + Sigmoid

"""

import tensorflow as tf
tf.executing_eagerly() 
import numpy as np
# 1. input/output 변수 정의 
inputs = [[1., 2.], [2, 3], [3, 1], [4, 3], [5, 3], [6, 2]] # [6,2]
outputs = [[0.], [0], [0], [1], [1], [1]]  # [6,1]
type(outputs)
inputs = np.array(inputs)

print("outputs type :" , type(outputs))
# 2. model : model class

class Model(tf.keras.Model) :    
    def __init__(self):
        super().__init__() # 부모 생성자 호출
        self.W = tf.Variable(tf.random.normal([2,1])) # 기울기(가중치)
        self.B = tf.Variable(tf.random.normal([1])) # bias
    
    def call(self , inputs) : # method 재정의
        print("inputs : ",inputs.dtype)
        print("W type : " , self.W.dtype)
        print("B type : " , self.B.dtype)
        return tf.matmul( tf.cast(inputs,dtype = tf.float32), self.W) + self.B # 회귀 방정식(예측치)
             
# 3. 손실 함수
def loss(model, inputs, outputs):
    sigmoid = tf.sigmoid(model(inputs))    
    print("loss shape :" ,sigmoid.shape)
    print("loss type :" ,sigmoid.dtype)
    print("check this2 : " , (1-outputs) )
    return -tf.reduce_mean(outputs * tf.math.log(sigmoid)  )#+ (1-outputs) * tf.math.log(1-sigmoid)) # Cross entropy

# 4. 미분계수(기울기) 계산 
def gradient(model , inputs , outputs):
    with tf.GradientTape() as tape:
        loss_value = loss(model, inputs, outputs) # 손실함수 호출  
        grad = tape.gradient(loss_value, [model.W, model.B])
    return grad

# 5. model 생성
model = Model() # 생성자

# 6. model 최적화 객체
opt = tf.keras.optimizers.SGD(learning_rate = 0.01)

print( "초기 손실값 : {:.6f}".format(loss(model , inputs , outputs)))
print("w : {} , b:{}".format(model.W.numpy() , model.B.numpy()))

# 7. 반복 학습
for step in range(300):
    grad = gradient(model , inputs , outputs)
    opt.apply_gradients(zip(grad , [model.W , model.B]))
    
    print("step ={} , loss = {:6f} ".format(step+1 , loss(model , inputs , outputs)))

# model 최적화
print( "최종 손실값 : {:.6f}".format(loss(model , inputs , outputs)))
print("w : {} , b:{}".format(model.W.numpy() , model.B.numpy()))

# model test
sigmoid =tf.sigmoid(model.call(inputs))
pred = tf.cast(sigmoid > 0.5 , tf.float32)













