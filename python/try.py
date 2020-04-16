'''
예외 처리 : 프로그램 샐행 상태에서 예기치 않는 상황(오류)
try:
    예외 발생 코드
except:
    예외 처리 코드
finally:
    항상 처리 되는 코드
'''

print('start')
x = [1,2,5.6,4,'123']
y = [1,2,3]
try:
    print(list(map(lambda x:x**2,y)))
except:
    print("need no str")
print('end')

# 유형별 예외 처리
print("-"*30)

try:
    div = 1000 / 2.5
    #f= open('c:/text.txt')
    num = int(input())

except ZeroDivisionError as e:
    print('except :',e)

except FileNotFoundError as e :
    print('except :', e )

except Exception as e:
    print('etc except : ' , e)
finally:
    print('program end')