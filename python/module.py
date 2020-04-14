'''
package = 폴더 유사함
- 유사한 모듈 파일을 저장하는 공간

module = 파일 유사함
- 파이썬 파일 *.py

클래스 , 함수
- 모듈에 포함되는 단위
'''

#from 패키지명.모듈명 import class or function
from package_test.module1 import Adder
from package_test.module1 import Sub


sum = Adder(10,20)

print(sum)
tmp = Sub(50,sum)
print(tmp.calc())