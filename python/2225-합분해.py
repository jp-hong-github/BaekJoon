import sys

input = sys.stdin.readline

N, K = 200, 200
dp = [[0 for _ in range(N + 1)] for _ in range(K + 1)]

# 숫자 1개로만 만들 수 있는 경우를 초기화
for i in range(N + 1):
    dp[1][i] = 1

# 숫자 0을 만드는 방법은 갯수와 상관없이 늘 1개뿐이다
for i in range(1, K + 1):
    dp[i][0] = 1

# dp 테이블 초기화
for q in range(2, K + 1):
    for i in range(1, N + 1):
        for j in range(0, i + 1):
            dp[q][i] += dp[q - 1][i - j]

n, k = map(int, input().split())
print(dp[k][n] % 1000000000)
