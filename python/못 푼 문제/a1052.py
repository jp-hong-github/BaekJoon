# 1052번(물병)
import sys
input = sys.stdin.readline

n,k = map(int,input().split())

result = 0#가게에서 가져올 물병의 개수
water_L = 1#현재 물병의 리터
while n>=k:
    if n%2==0:
        n = (int)(n//2)
        water_L+=1
    else:
        result += water_L
        n = (int)((n+water_L)//2)
        
print(result)