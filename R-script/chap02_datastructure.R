# DataStructure

# 자료구조의 유형
# 1) Vector - 동일한 자료형을 가지는 1차원 배열 구조.
# 생성 함수: c() / seq() / rep()

x<- c(1,3,5,7)
y<- c(3,5)
length(x)

# 집합 관련 함수
union(x,y) #합집합
setdiff(x,y) # 차집합
intersect(x,y) #교집합

# 벡터 변수 유형
num <- 1:5
num
num <-c(-10:5)
num

# 벡터 원소 이름 지정
names <- c("kim","park","uk")
age <- c(27,25,31)
names(age) <- names
age
names

>str(age)

#object의 자료구조를 알려준다. 아래와 같다면 vector 형식
#Named num [1:3] 27 25 31
#- attr(*, "names")= chr [1:3] "kim" "park" "uk"

#seq()