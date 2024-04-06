import sys

input = sys.stdin.readline

n = int(input())

stairs = [int(input()) for _ in range(n)]

dp = [0 for _ in range(n)]
if n >= 1:
    dp[0] = stairs[0]
    if n >= 2:
        dp[1] = stairs[0] + stairs[1]
        if n >= 3:
            dp[2] = stairs[2] + max(stairs[0], stairs[1])

for i in range(3, n):
    # print(i,dp)
    dp[i] = stairs[i] + max(stairs[i - 1] + dp[i - 3], dp[i - 2])

print(dp[n - 1])
