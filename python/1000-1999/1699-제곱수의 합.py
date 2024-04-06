import sys

input = sys.stdin.readline

n = int(input())

dp = [float("inf") for _ in range(100001)]
dp[0] = 0
dp[1] = 1

for i in range(100001):
    for k in range(1, int(i ** (1 / 2)) + 1):
        dp[i] = min(dp[i], dp[i - k**2] + 1)

print(dp[n])
