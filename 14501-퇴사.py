import sys


input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dp = [0 for _ in range(N + 1)]
# 뒤에서부터 거꾸로 계산
for i in range(N - 1, -1, -1):
    if arr[i][0] + i > N:
        dp[i] = dp[i + 1]
    else:
        #
        dp[i] = max(dp[i + 1], dp[arr[i][0] + i] + arr[i][1])

print(dp[0])
