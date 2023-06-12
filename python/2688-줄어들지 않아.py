import sys

input = sys.stdin.readline

dp = [[0 for _ in range(10)] for _ in range(65)]

# 한 자리수일 떄의 경우를 정의
for i in range(0, 10):
    dp[1][i] = 1


for i in range(2, 65):
    for k in range(0, 10):
        temp = 0
        for j in range(0, k + 1):
            temp += dp[i - 1][j]
        dp[i][k] = temp


t = int(input())
for _ in range(t):
    n = int(input())
    print(sum(dp[n]))
