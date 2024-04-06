# 다이내믹 프로그래밍
import sys

input = sys.stdin.readline

dp = [0, 1]
n = int(input())
for k in range(2, n + 1):
    dp.append((dp[k - 1] + dp[k - 2]) % 1000000007)

print(dp[n])
