'''
문자열 처리
- 문자열(String)
- indexing slicing 가능
- 문자열 = 상수 : 수정이 불가능
'''

# 1. 문자열 처리
# 1) 문자열 유형
lineStr = "this is one line string"
print(lineStr.split())

multiStr = """this
is multi line
string"""

multiStr2 = multiStr.strip()

print(multiStr.split())

#sql 문 : 부서번호
'''
deptno = int(input())
query = f"""select * from emp
where deptno={deptno}
order by deptno"""

print(query)
'''
# 2) 문자열 연산 (+ , * )
print('python'+'program')
print('-'*30)

'''
object.member / object.member()
int.member
str.member
'''

# 3) 문자열 처리 함수
print(len(lineStr))
print(lineStr.count('t'))
print(lineStr.index('t'))
print(lineStr.rfind('t'))
print(lineStr.startswith('this'))
print(lineStr.split())
print(lineStr.upper())
print(multiStr.split("\n"))
print("-"*20)
# 4) indexing , slicing
print(lineStr[0])
print(lineStr[-1])

print(lineStr[:12])
print(lineStr[-6:])