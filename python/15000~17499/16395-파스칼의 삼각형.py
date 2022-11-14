import sys

input = sys.stdin.readline

n, k = map(int, input().split())

result = 0
dp = [[1], [0, 1]]  # 가상의 0번째 행, 1번째 행
for line in range(2, n + 1):
    temp = [0]
    for num in range(1, line + 1):
        if num == 1:
            temp.append(1)
        elif num == line:
            temp.append(1)
        else:
            temp.append(dp[line - 1][num - 1] + dp[line - 1][num])
    dp.append(temp)

result = dp[n][k]

print(result)
