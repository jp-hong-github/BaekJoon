#사선 공식은 모든 다각형에 적용 가능하다.
import sys
input =sys.stdin.readline

n = int(input())

data = []

for i in range(n):
    data.append(list(map(int,input().split())))
    
data.append(data[0])


result = 0 
for k in range(n):
    result += data[k][0] * data[k+1][1] - data[k][1] * data[k+1][0]

import math
result = abs(result * 1/2)


print("%.1f"%(result))