import sys

input = sys.stdin.readline
N = int(input())
M = int(input())

vip = [0]
for _ in range(M):
    vip.append(int(input()))
vip.append(N + 1)

# vip가 없이 좌석의 개수가 N개일 때 가능한 경우의 수
dp = [1, 1, 2]
for i in range(3, 41):
    dp.append(dp[i - 1] + dp[i - 2])


if M > 0:
    result = 1
    for k in range(len(vip) - 1):
        num = vip[k + 1] - vip[k] - 1
        if num > 1:
            result *= dp[num]

    print(result)
else:
    print(dp[N])
