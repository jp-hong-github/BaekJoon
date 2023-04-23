import sys

input = sys.stdin.readline

# 이전 기록에서 1,2,3 을 더해서 만들 수 있는 경우의 수
dp = [[0, 0, 0], [1, 0, 0], [1, 1, 0], [1, 1, 1]]  # 0 1 2 3

for i in range(4, 10001):
    temp = [
        dp[i - 1][0],
        dp[i - 2][0] + dp[i - 2][1],
        dp[i - 3][0] + dp[i - 3][1] + dp[i - 3][2],
    ]
    dp.append(temp)


T = int(input())
for _ in range(T):
    n = int(input())
    print(sum(dp[n]))
