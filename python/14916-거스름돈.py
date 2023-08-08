import sys

input = sys.stdin.readline

n = int(input())
INF = int(10e9)
dp = [INF for _ in range(n + 1)]
dp[0] = 0

for i in range(n + 1):
    if i - 2 >= 0 and dp[i - 2] != INF:
        dp[i] = min(dp[i], dp[i - 2] + 1)
    if i - 5 >= 0 and dp[i - 5] != INF:
        dp[i] = min(dp[i], dp[i - 5] + 1)

if dp[n] != INF:
    print(dp[n])
else:
    print(-1)
