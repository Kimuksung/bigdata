import sys
import math

from decimal import *

n , m = map(int,input().split())

arr = list(map(int,input().split()))

answer = Decimal('inf')

# 시작점 변경
for i in range(n-m+1):
    sum1 = sum(v for v in arr[i:i+m-1])
    var = sum(v**2 for v in arr[i:i+m-1])

    for j in range(i+m,n+1):
        sum1+= arr[j-1]
        var += arr[j-1]**2
        avg= sum1 / (j-i)

        std = round((var/(j-i) - avg**2)**(1/2),11)
        answer = min(answer , std)

print(answer)

