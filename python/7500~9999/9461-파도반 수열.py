import sys

input = sys.stdin.readline

T = int(input())

dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]


for i in range(10, 103):
    dp.append(dp[i - 1] + dp[i - 5])

for _ in range(T):
    n = int(input())
    print(dp[n - 1])
