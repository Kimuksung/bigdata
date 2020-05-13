# -*- coding: utf-8 -*-
"""
sklearn logistic regression model

    - y variable is category
    
"""

from sklearn.datasets import load_breast_cancer , load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score  , confusion_matrix# model의 평가 도구

# 1. discrete classfy modeling

# 1. dataset load
breast = load_breast_cancer()

X = breast.data # x 변수
y = breast.target

X.shape
y.shape

# 2. model create
help(LogisticRegression)

'''
random_state=None, # 난수 seed값 지정
solver='lbfgs',  # 알고리즘
max_iter=100,    # 반복 학습 횟수
multi_class='auto'  # 다항 분류 지정

EX)
normal data , descrete classfy : default
normal data , multi classfy(more than 3) : solver = 'lbfgs' , multi_class = 'multinomial'
big data , descrete classfy : solver = 'sag' / 'saga'
big data , multi classfy : solver = 'sag' / 'saga' , multi_class = 'multinomial'

'''

lr = LogisticRegression(random_state = 123)
model = lr.fit(X = X,y = y)

# 3. model평가
acc = model.score(X,y)
acc # 0.9472759226713533

y_pred = model.predict(X)

accuracy_score(y,y_pred) # 0.9472759226713533

con_max = confusion_matrix(y, y_pred)
'''
[[193,  19],
[ 11, 346]]
'''
(con_max[0,0] + con_max[1,1]) / con_max.sum()

tab = pd.crosstab(y,y_pred ,rownames=['관측치'] , colnames=['예측치'])
acc = (tab.loc[0,0] +tab.loc[1,1]) / len(y)


################
# multi classfy
################
iris = load_iris()
iris.target_names
X , y = load_iris(return_X_y=True)

y # 0~2

lr = LogisticRegression(random_state=123 ,solver = 'lbfgs' , multi_class = 'multinomial')
# multi_class = 'multinomial' -> softmax
'''
sigmoid function : 0 ~ 1  확률 -> cutoff = 0.5 -> discrete classfy
softmax function : 0 ~ 1  확률 -> 전체합 = 1 -> multi classfy
'''

model = lr.fit(X,y)
y_pred = model.predict(X) #class
y_pred2 = model.predict_proba(X) # 확률 값

arr = np.array([9.81797141e-01, 1.82028445e-02, 1.44269293e-08])
arr

# model 평가
acc = accuracy_score(y , y_pred)
acc # 0.9733333333333334

con_max = confusion_matrix( y , y_pred)
con_max
'''
[[50,  0,  0],
 [ 0, 47,  3],
 [ 0,  1, 49]]
'''
acc = (con_max[0,0] + con_max[1,1] + con_max[2,2]) / con_max.sum()
acc # 0.9733333333333334

# 히트맵 시각화
import seaborn as sn # heatmap - Accuracy Score

# confusion matrix heatmap 
plt.figure(figsize=(6,6)) # chart size
sn.heatmap(con_max, annot=True, fmt=".3f", linewidths=.5, square = True);# , cmap = 'Blues_r' : map »ö»ó 
plt.ylabel('Actual label');
plt.xlabel('Predicted label');
all_sample_title = 'Accuracy Score: {0}'.format(acc)
plt.title(all_sample_title, size = 18)
plt.show()

###########################
# digits : multi class
###########################

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
# 1. dataset load
digits = load_digits()
digits.target_names
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

X = digits.data
y = digits.target
X.shape # (1797, 64)

# 2. data split
img_train , img_test , label_train , label_test = train_test_split(X, y , test_size = 0.25)

img2d = img_train.reshape(-1 , 8 , 8)  # all image
img2d.shape
plt.imshow(img2d[0])
img2d[0]
label_train[0]

# 3. model 생성
lr = LogisticRegression(solver = 'lbfgs' , multi_class = 'multinomial')
model = lr.fit(img_train , label_train )

y_pred = model.predict( img_test)

accuracy_score(label_test , y_pred)
# 0.98

result = label_test == y_pred
result
false_img = img_test[result == False]
false_img

false_index = [i for i, x in enumerate(result) if not x]
plt.imshow(digits.images[82])
digits.images[82]

for img in false_img:
    tmp=img.reshape(8,8)
    plt.imshow(tmp)



fig = plt.figure(figsize=(10, 5))
plt.subplots_adjust(top=1, bottom=0, hspace=0, wspace=0.05)
cnt = 1
for i in false_index:
    ax = fig.add_subplot(8, 8, cnt)
    ax.imshow(digits.images[i], cmap=plt.cm.bone, interpolation="none")
    ax.grid(False)
    ax.xaxis.set_ticks([])
    ax.yaxis.set_ticks([])
    plt.title(digits.target_names[digits.target[i]])
    #plt.title(i)
    cnt = cnt +1
plt.tight_layout()
plt.show()


















