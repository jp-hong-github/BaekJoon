import sys

input = sys.stdin.readline

n = int(input())

# 경우의 수
# 0 : 올 출석 또는 마지막날은 결석 안함
# 1 : 지각 한번
# 2 : 마지막 날 결석
# 3 : 마지막 날과 이전 날 결석
# 4 : 지각 한 번 + 마지막 날 결석
# 5 : 지각 한 번 + 마지막 날과 이전 날 결석
dp = [[0 for _ in range(6)] for _ in range(1001)]
dp[1] = [1, 1, 1, 0, 0, 0]

for i in range(2, 1001):
    dp[i][0] = dp[i - 1][0] + dp[i - 1][2] + dp[i - 1][3]
    dp[i][1] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4] + dp[i - 1][5]
    dp[i][2] = dp[i - 1][0]
    dp[i][3] = dp[i - 1][2]
    dp[i][4] = dp[i - 1][1]
    dp[i][5] = dp[i - 1][4]

# print(dp[n])
print(sum(dp[n]) % 1000000)
