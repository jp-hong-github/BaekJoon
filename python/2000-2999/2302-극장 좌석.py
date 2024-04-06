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


# ! 230112 복습
# import sys


# input = sys.stdin.readline

# n = int(input())
# m = int(input())
# vip = [int(input()) for _ in range(m)]

# # x개의 좌석에서 섞어서 않는 경우의 수
# dp = [0, 1, 2, 3]

# for i in range(4, 41):
#     dp.append(dp[i - 1] + dp[i - 2])

# answer = 1
# previous_vip = 0
# for k in vip:
#     if k - previous_vip - 1 != 0:
#         answer *= dp[k - previous_vip - 1]
#     previous_vip = k

# if n - previous_vip != 0:
#     answer *= dp[n - previous_vip]
# print(answer)
