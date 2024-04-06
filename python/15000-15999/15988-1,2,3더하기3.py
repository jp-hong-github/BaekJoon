import sys

input = sys.stdin.readline

t = int(input())
case = []
for i in range(t):
    case.append(int(input()))

max_num = max(case) + 1

dp = [0 for _ in range(1000001)]

dp[1] = 1
dp[2] = 2
dp[3] = 4


for i in range(4, 1000001):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009


for num in case:
    print(dp[num] % 1000000009)
