import sys
input = sys.stdin.readline


n = int(input())



cardPack = list(map(int,input().split()))
cardPack.insert(0,0)
dp = [0] * 1005

dp[1] = cardPack[1]#카드 1장
if n>1:
    dp[2] = max(cardPack[1]*2,cardPack[2])#카드 2장
if n>2:
    dp[3] = max(cardPack[1]*3,cardPack[1]+cardPack[2],cardPack[3])#카드 3장
    
for i in range(4,n+1):
    mid = i//2
    temp = 0
    for k in range(1,mid+1):
        temp = max(temp,dp[k]+dp[i-k])
    dp[i] = max(temp,cardPack[i])

print(dp[n])