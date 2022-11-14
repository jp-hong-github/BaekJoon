import sys

input = sys.stdin.readline

n = int(input())

dp = [1]

for i in range(1, n + 1):
    temp = 0
    for k in range(i):
        temp += dp[k] * dp[i - k - 1]
    dp.append(temp)

print(dp[n])

