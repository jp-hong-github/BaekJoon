import sys

input = sys.stdin.readline

N = int(input())

if N == 1:
    print(1)
elif N == 2:
    print(1)
elif N == 3:
    print(2)
else:  # 10~ 으로 시작한다. 100,101
    dp = [[0, 0] for _ in range(N)]  # 해당 자리가 0, 해당 자리가 1일 때의 만들 수 있는 이친수
    dp[2][0] = 1  # 100
    dp[2][1] = 1  # 101

    for i in range(N - 3):
        dp[i + 3][0] = dp[i + 2][0] + dp[i + 2][1]
        dp[i + 3][1] = dp[i + 2][0]

    print(sum(dp[N - 1]))
    # print(dp)
