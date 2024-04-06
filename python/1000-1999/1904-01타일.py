import sys

input = sys.stdin.readline

N = int(input())
result = 0
dp = [0, 1, 2, 3]

for i in range(4, 1_000_001):
    dp.append((dp[i - 1] + dp[i - 2]) % 15746)
    # print(i)
print(dp[N] % 15746)
