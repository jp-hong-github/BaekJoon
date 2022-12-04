import sys
import math 

input = sys.stdin.readline

r, g = map(int, input().split())

result = []

gcd = math.gcd(r,g)

divisor_lst = []
for i in range(1,int(gcd**(1/2))+1):
    if gcd%i==0:
        divisor_lst.append(i)
        if i**2!=gcd:
            divisor_lst.append(gcd//i)

for k in divisor_lst:
    result.append((k,r//k,g//k))
    
for case in result:
    print(*case)