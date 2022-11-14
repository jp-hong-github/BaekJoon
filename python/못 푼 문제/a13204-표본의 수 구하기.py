import sys
from decimal import Decimal

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    case = Decimal(input())
    #예가 한 명만 있다고 판단
    result = 0
    start = 1
    end = 70000
    while start <=end :
        mid = (start+end)//2
        percent = Decimal(1/Decimal(mid) * 100)
        print(percent,mid,start,end)
        if percent >= case+Decimal('0.0005'):
            reuslt = mid
            start = mid + 1
        elif  percent <= case-Decimal('0.0005'):
            end = mid -1
    print(mid+1)