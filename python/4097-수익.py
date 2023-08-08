import sys

input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    su_ik = [int(input()) for _ in range(n)]
    dp = [0] * n
    dp[0] = su_ik[0]
    for i in range(1, n):
        dp[i] = max(su_ik[i], dp[i - 1] + su_ik[i])
    print(max(dp))
