# 피보나치 수
import sys

input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(n + 10)]  # 넉넉하게

dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 5
for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n] % 10007)
