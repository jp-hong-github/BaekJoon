import sys

input = sys.stdin.readline

n = int(input())
box = list(map(int, input().split()))

dp = [1 for _ in range(n)] 


for i in range(1,n):
    for k in range(i):
        if box[i] > box[k]:
            dp[i] = max(dp[i],dp[k]+1)
            
print(max(dp))