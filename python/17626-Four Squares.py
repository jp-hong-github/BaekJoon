import sys

input = sys.stdin.readline

n = int(input())

# 1 ~ 50,000까지 전부 만들기
dp = [float("inf") for _ in range(50001)]
dp[0] = 0
dp[1] = 1
for i in range(2, 50001):
    for k in range(1, int(i ** (1 / 2)) + 1):
        dp[i] = min(dp[i - k**2] + 1, dp[i])


print(dp[n])
