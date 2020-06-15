import matplotlib.image as img 
import matplotlib.pyplot as plt 
import tensorflow as tf

filename = "C:/ITWILL/6_Tensorflow/data/packet.jpeg"
input_image = img.imread(filename)

print('input dim =', input_image.ndim) #dimension
print('input shape =', input_image.shape) #shape

# image 원본 출력 
plt.subplot(1,2,1)
plt.imshow(input_image)
plt.show() 

# image 축 변경
plt.subplot(1,2,2)
plt.imshow(tf.transpose(a = input_image , perm = [1,0,2]))


































