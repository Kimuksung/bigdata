import sys
import math
from decimal import *

n , k = map(int,input().split())

arr = list(map(int,input().split()))
re = Decimal('inf')

# 시작점 변경
for s in range(n - k + 1):
    sum_val = sum(arr[s:s + k - 1])
    sum_val_sq = sum([v * v for v in arr[s:s + k - 1]])

    # 길이 변경
    for l in range(k, n - s + 1):
        sum_val += arr[s + l - 1]
        sum_val_sq += arr[s + l - 1] ** 2
        aver = sum_val / Decimal(l)
        print("avg:",aver)
        std = (sum_val_sq / Decimal(l) - aver ** 2).sqrt()

        re = min(re, std)

print(re)
