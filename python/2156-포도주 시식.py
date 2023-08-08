import sys

input = sys.stdin.readline

n = int(input())

podoju = [0] * 10000

for i in range(n):
    podoju[i] = int(input())


dp = [0 for _ in range(n + 1000)]

dp[0] = podoju[0]
dp[1] = podoju[0] + podoju[1]
dp[2] = max(podoju[2] + max(podoju[0], podoju[1]), dp[1])


for i in range(3, n):
    # print(i,dp)
    dp[i] = podoju[i] + max(podoju[i - 1] + dp[i - 3], dp[i - 2])
    dp[i] = max(dp[i - 1], dp[i])

# print(dp)
print(max(dp))
