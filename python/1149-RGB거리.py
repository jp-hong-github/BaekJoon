n = int(input())

rgb = []
for i in range(n):
    rgb.append(list(map(int, input().split())))

dp = []
dp.append(rgb[0])

for i in range(1, n):
    temp = []
    temp.append(min(rgb[i][0] + dp[i - 1][1], rgb[i][0] + dp[i - 1][2]))  # 첫번째
    temp.append(min(rgb[i][1] + dp[i - 1][0], rgb[i][1] + dp[i - 1][2]))  # 두번째
    temp.append(min(rgb[i][2] + dp[i - 1][0], rgb[i][2] + dp[i - 1][1]))  # 세번째
    dp.append(temp)


print(min(dp[n - 1]))
