import sys

input = sys.stdin.readline

n = int(input())


numbers: list = list(map(int, input().split()))

if n == 1:
    print(numbers[0])
else:
    dp = [[0, 0] for _ in range(n)]
    dp[0][0] = numbers[0]
    result = -float("inf")
    for idx, num in enumerate(numbers):
        if idx == 0:
            continue
        else:
            dp[idx][0] = max(dp[idx - 1][0] + num, num)
            dp[idx][1] = max(dp[idx - 1][0], dp[idx - 1][1] + num)
            result = max(max(dp[idx]), result)
    print(result)
