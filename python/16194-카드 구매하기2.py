import sys

INF = int(10e9)

input = sys.stdin.readline

N = int(input())
p_list = list(map(int, input().split()))  # 1 ~ N
p_list.insert(0, 0)

dp = [INF for _ in range(N + 1)]
dp[0] = 0

for i in range(1, N + 1):
    if i == 1:
        dp[1] = p_list[1]
    else:
        for k in range(1, i + 1):
            dp[i] = min(dp[i], dp[i - k] + p_list[k])

print(dp[N])
