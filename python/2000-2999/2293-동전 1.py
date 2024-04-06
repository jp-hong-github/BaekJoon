import sys

input = sys.stdin.readline

N, K = map(int, input().split())
coins: list = [int(input()) for _ in range(N)]
dp: list = [0 for _ in range(K + 1)]
dp[0] = 1

for j in range(N):
    for i in range(1, K + 1):
        if i - coins[j] < 0:
            continue

        dp[i] += dp[i - coins[j]]

print(dp[-1])
