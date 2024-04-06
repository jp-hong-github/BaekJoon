import sys

input = sys.stdin.readline
N = int(input())

# 3*N = 홀수를 2로 나누어 떨어지지 않기 때문에 N이 홀수인 경우 채울 수가 없음

if N % 2 != 0:
    print(0)
    sys.exit()

dp = [0 for _ in range(31)]
dp[0] = 1
dp[2] = 3

for i in range(4, N + 1, 2):
    dp[i] = 3 * dp[i - 2]
    for j in range(4, i + 1, 2):
        dp[i] += dp[i - j] * 2

print(dp[N])
